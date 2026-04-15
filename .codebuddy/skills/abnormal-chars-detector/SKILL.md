---
name: abnormal-chars-detector
description: 扫描 Android 工程中所有 module 的 res/values*/strings.xml 文件，检测异形字符、零宽字符、全角字符等异常内容，生成 Markdown 汇总报告。适用于 Android 字符串资源质量检查场景。
---

# Android 异形字符检测 Skill

## 用途

扫描 Android 工程中所有 module 内 `res/values*/strings.xml` 文件，检测以下异常字符：

- 康熙部首字符 (CJK Radicals)
- CJK 兼容表意文字
- 全角/半角形式字符
- 私有区字符
- 零宽/不可见字符
- 控制类/格式类字符
- NFKC 规范化后发生变化的字符

**注意**：不报告标点符号和空格等常规异常。

## 触发条件

- 用户要求检测 Android 字符串资源中的异常字符
- 用户要求扫描 strings.xml 中的异形字符
- 用户要求检查全角字符、零宽字符等问题
- 用户提到"异形字符"、"异常字符"、"全角字符"、"零宽字符"等关键词

## 工作流程

### 1. 扫描 strings.xml 文件

使用 `scripts/detect_abnormal_chars.py` 脚本扫描项目：

```bash
python3 scripts/detect_abnormal_chars.py --project-root <项目根目录> --output <输出文件路径>
```

参数说明：
- `--project-root`：Android 项目根目录，默认为当前工作目录
- `--output`：输出 Markdown 报告的文件路径，默认为 `abnormal-chars-report.md`

### 2. 解析 strings.xml

脚本会自动：
1. 查找所有 `res/values*/strings.xml` 文件
2. 解析 XML 提取 `<string>` 标签内容
3. 对每个字符串值进行异形字符检测

### 3. 生成报告

输出 Markdown 表格报告，包含：
- 文件路径
- 字符串名称 (name 属性)
- 异常字符位置和详情
- Unicode 码点、名称、区块信息
- NFKC 归一化结果
- 触发原因

## 输出格式

报告以 Markdown 格式输出，结构如下：

```markdown
# Android 异形字符检测报告

- 扫描时间：YYYY-MM-DD HH:MM:SS
- 扫描文件数：N
- 异常文件数：M
- 异常字符总数：X

## 异常详情

| 文件 | 字符串名称 | 位置 | 字符 | 码点 | Unicode 名称 | 区块 | 类别 | NFKC 归一化 | 原因 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
```

## 使用示例

```bash
# 扫描当前项目
python3 scripts/detect_abnormal_chars.py

# 指定项目路径
python3 scripts/detect_abnormal_chars.py --project-root /path/to/android/project

# 指定输出文件
python3 scripts/detect_abnormal_chars.py --output report.md
```

## 依赖

- Python 3.6+
- 无需额外安装第三方库（仅使用标准库）

## 注意事项

1. 脚本会递归扫描所有子目录中的 `res/values*/strings.xml` 文件
2. 仅检测 `<string>` 标签的内容，不检测其他资源类型
3. 报告文件默认输出到当前工作目录