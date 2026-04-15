#!/usr/bin/env python3
"""
Android strings.xml 异形字符检测脚本

扫描 Android 工程中所有 module 的 res/values*/strings.xml 文件，
检测异形字符、零宽字符、全角字符等异常内容，生成 Markdown 汇总报告。
"""

import argparse
import re
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
import unicodedata


def get_unicode_block(cp):
    """粗略判断 Unicode 区块"""
    ranges = [
        (0x2E80, 0x2EFF, "CJK Radicals Supplement"),
        (0x2F00, 0x2FDF, "Kangxi Radicals"),
        (0x3000, 0x303F, "CJK Symbols and Punctuation"),
        (0xF900, 0xFAFF, "CJK Compatibility Ideographs"),
        (0xFF00, 0xFFEF, "Halfwidth and Fullwidth Forms"),
        (0x200B, 0x200D, "Zero Width Characters"),
        (0xFE00, 0xFE0F, "Variation Selectors"),
        (0xE000, 0xF8FF, "Private Use Area"),
    ]
    for start, end, name in ranges:
        if start <= cp <= end:
            return name
    return "Other"


def detect_abnormal_chars(text):
    """检测文本中的异常字符（排除标点、空格等正常字符）"""
    results = []

    for idx, ch in enumerate(text):
        cp = ord(ch)
        name = unicodedata.name(ch, "<UNKNOWN>")
        category = unicodedata.category(ch)
        normalized = unicodedata.normalize("NFKC", ch)
        block = get_unicode_block(cp)

        reasons = []

        # 1. 康熙部首（异常）
        if 0x2F00 <= cp <= 0x2FDF:
            reasons.append("康熙部首字符")

        # 2. CJK 兼容表意文字（异常）
        if 0xF900 <= cp <= 0xFAFF:
            reasons.append("CJK兼容表意文字")

        # 3. 全角/半角区（排除全角空格 U+3000，它是 CJK 标点）
        if 0xFF00 <= cp <= 0xFFEF:
            reasons.append("全角/半角形式字符")

        # 4. 私有区字符（异常）
        if 0xE000 <= cp <= 0xF8FF:
            reasons.append("私有区字符")

        # 5. 零宽字符（异常，不可见）
        if cp in (0x200B, 0x200C, 0x200D, 0xFEFF):
            reasons.append("零宽/不可见字符")

        # 6. 控制字符（排除零宽字符已处理的）
        if category.startswith("C") and cp not in (0x200B, 0x200C, 0x200D, 0xFEFF):
            reasons.append("控制类/格式类字符")

        # 注意：不检测以下内容（这些是正常字符）：
        # - NO-BREAK SPACE (U+00A0) - 正常排版字符
        # - 正常语言字符的 NFKC 变化（如泰语字符）- 这是兼容性分解，不是异常

        if reasons:
            results.append(
                {
                    "index": idx,
                    "char": ch,
                    "codepoint": f"U+{cp:04X}",
                    "name": name,
                    "block": block,
                    "category": category,
                    "normalized": normalized,
                    "reasons": reasons,
                }
            )

    return results


def _escape_markdown_cell(value):
    """转义 Markdown 表格单元格内容"""
    return (
        str(value)
        .replace("|", "\\|")
        .replace("`", "\\`")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def find_strings_files(project_root):
    """查找所有 strings.xml 文件"""
    project_root = Path(project_root)
    pattern = re.compile(r"values(-[a-z]{2,3}(-[A-Z]{2,4})?)?(/|\\)?strings\.xml$")
    
    strings_files = []
    for f in project_root.rglob("strings.xml"):
        # 检查路径是否匹配 res/values*/strings.xml
        if pattern.search(str(f)):
            strings_files.append(f)
    
    return sorted(strings_files)


def parse_strings_xml(file_path):
    """解析 strings.xml 文件，提取字符串名称和内容"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        strings = []
        for string_elem in root.findall(".//string"):
            name = string_elem.get("name", "")
            # 获取完整文本内容（包括子元素）
            text = "".join(string_elem.itertext())
            if text:
                strings.append({"name": name, "text": text})
        
        return strings
    except ET.ParseError as e:
        return None, str(e)
    except Exception as e:
        return None, str(e)


def generate_report(results, project_root):
    """生成 Markdown 汇总报告"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total_files = len(results)
    files_with_issues = sum(1 for r in results if r["issues"])
    total_issues = sum(len(r["issues"]) for r in results)
    
    lines = [
        "# Android 异形字符检测报告",
        "",
        f"- 扫描时间：{timestamp}",
        f"- 项目路径：{project_root}",
        f"- 扫描文件数：{total_files}",
        f"- 异常文件数：{files_with_issues}",
        f"- 异常字符总数：{total_issues}",
        "",
    ]
    
    if total_issues == 0:
        lines.append("✅ 未检测到异形字符。")
        return "\n".join(lines)
    
    lines.append("## 异常详情")
    lines.append("")
    lines.append(
        "| 文件 | 字符串名称 | 位置 | 字符 | 码点 | Unicode 名称 | 区块 | 类别 | NFKC 归一化 | 原因 |"
    )
    lines.append(
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    )
    
    for file_result in results:
        if not file_result["issues"]:
            continue
        
        file_path = file_result["file"]
        for issue in file_result["issues"]:
            string_name = issue["string_name"]
            char_info = issue["char_info"]
            
            char_cell = f"`{_escape_markdown_cell(char_info['char'])}`"
            normalized_cell = _escape_markdown_cell(repr(char_info["normalized"]))
            reasons_cell = _escape_markdown_cell("；".join(char_info["reasons"]))
            
            lines.append(
                "| {file} | {name} | {pos} | {char} | {codepoint} | {uname} | {block} | {category} | {normalized} | {reasons} |".format(
                    file=_escape_markdown_cell(str(file_path)),
                    name=_escape_markdown_cell(string_name),
                    pos=char_info["index"],
                    char=char_cell,
                    codepoint=char_info["codepoint"],
                    uname=_escape_markdown_cell(char_info["name"]),
                    block=_escape_markdown_cell(char_info["block"]),
                    category=char_info["category"],
                    normalized=normalized_cell,
                    reasons=reasons_cell,
                )
            )
    
    lines.append("")
    
    # 添加按文件分组的摘要
    lines.append("## 按文件汇总")
    lines.append("")
    lines.append("| 文件 | 异常字符串数 | 异常字符数 |")
    lines.append("| --- | --- | --- |")
    
    for file_result in results:
        if file_result["issues"]:
            unique_strings = set(i["string_name"] for i in file_result["issues"])
            lines.append(
                f"| {_escape_markdown_cell(str(file_result['file']))} | {len(unique_strings)} | {len(file_result['issues'])} |"
            )
    
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="扫描 Android 工程中 strings.xml 文件的异形字符"
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Android 项目根目录，默认为当前目录",
    )
    parser.add_argument(
        "--output",
        default="abnormal-chars-report.md",
        help="输出 Markdown 报告路径，默认为 abnormal-chars-report.md",
    )
    args = parser.parse_args()
    
    project_root = Path(args.project_root).resolve()
    output_path = Path(args.output)
    
    print(f"扫描项目：{project_root}")
    
    # 查找所有 strings.xml 文件
    strings_files = find_strings_files(project_root)
    print(f"找到 {len(strings_files)} 个 strings.xml 文件")
    
    if not strings_files:
        print("未找到任何 strings.xml 文件")
        return
    
    # 检测每个文件
    results = []
    for file_path in strings_files:
        parsed = parse_strings_xml(file_path)
        
        if isinstance(parsed, tuple):
            # 解析错误
            results.append({
                "file": file_path,
                "issues": [],
                "error": parsed[1]
            })
            continue
        
        strings = parsed
        file_issues = []
        
        for string_item in strings:
            detected = detect_abnormal_chars(string_item["text"])
            for char_info in detected:
                file_issues.append({
                    "string_name": string_item["name"],
                    "char_info": char_info
                })
        
        results.append({
            "file": file_path,
            "issues": file_issues
        })
    
    # 生成报告
    report = generate_report(results, str(project_root))
    output_path.write_text(report, encoding="utf-8")
    
    total_issues = sum(len(r["issues"]) for r in results)
    print(f"检测完成，共发现 {total_issues} 个异常字符")
    print(f"报告已生成：{output_path.resolve()}")


if __name__ == "__main__":
    main()