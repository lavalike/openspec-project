# Android 异形字符检测报告

- 扫描时间：2026-04-15 17:54:59
- 项目路径：/Users/wangzhen/android/git/openspec-project
- 扫描文件数：3
- 异常文件数：3
- 异常字符总数：51

## 检测方法

使用 Unicode NFKC 归一化对比检测 CJK 相关异常字符：
- 康熙部首字符 (Kangxi Radicals: 0x2F00-0x2FDF)
- CJK 兼容表意文字 (Compatibility Ideographs: 0xF900-0xFAFF)
- 全角字符 (Fullwidth Forms: 0xFF00-0xFFEF)

## 异常详情

| 文件 | 字符串名称 | 位置 | 字符 | 码点 | Unicode 名称 | 区块 | 类别 | NFKC 归一化 | 原因 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | subtitles_fun_des | 25 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | subtitles_fun_des | 42 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | subtitles_fun_des | 53 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | subtitles_fun_no_translation_des | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | subtitles_permissions_conflict_tip | 9 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | permissions_conflict_tip | 7 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | permissions_denied_tip | 6 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | network_exception_switched_offline | 1 | `⽹` | U+2F79 | KANGXI RADICAL NET | Kangxi Radicals | So | '网' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | network_exception_switched_offline | 5 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_exception_switched_offline | 6 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_input_error | 3 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_input_error | 4 | `⽆` | U+2F46 | KANGXI RADICAL NOT | Kangxi Radicals | So | '无' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_input_error | 11 | `⼊` | U+2F0A | KANGXI RADICAL ENTER | Kangxi Radicals | So | '入' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_input_error | 15 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | server_input_error | 20 | `⼊` | U+2F0A | KANGXI RADICAL ENTER | Kangxi Radicals | So | '入' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | free_quota_exhausted | 6 | `⽤` | U+2F64 | KANGXI RADICAL USE | Kangxi Radicals | So | '用' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | free_quota_exhausted | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | free_quota_exhausted | 17 | `⽤` | U+2F64 | KANGXI RADICAL USE | Kangxi Radicals | So | '用' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | reached_membership_limit | 13 | `⽤` | U+2F64 | KANGXI RADICAL USE | Kangxi Radicals | So | '用' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | reached_membership_limit | 16 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | reached_membership_limit | 28 | `⽤` | U+2F64 | KANGXI RADICAL USE | Kangxi Radicals | So | '用' | 康熙部首字符 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | login_failed_token_expired | 5 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | tcl_ai_is_disable | 9 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | tcl_ai_is_disable | 25 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | tcl_ai_is_disable_android15 | 9 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | tcl_ai_is_disable_android15 | 25 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | network_exception_tip | 5 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | ai_net_req_opt_abort | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | ai_net_req_opt_not_allow | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | free_credit_exhausted | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | membership_credit_exhausted | 16 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | subtitles_fun_des | 30 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | subtitles_fun_des | 46 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | subtitles_fun_des | 57 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | server_input_error | 3 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | free_quota_exhausted | 18 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | tcl_ai_is_disable | 15 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | tcl_ai_is_disable_android15 | 15 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | network_exception_tip | 5 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | ai_net_req_opt_not_allow | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | free_credit_exhausted | 18 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | subtitles_fun_des | 30 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | subtitles_fun_des | 46 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | subtitles_fun_des | 57 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | server_input_error | 3 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | free_quota_exhausted | 18 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | tcl_ai_is_disable | 15 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | tcl_ai_is_disable_android15 | 15 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | network_exception_tip | 5 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | ai_net_req_opt_not_allow | 8 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | free_credit_exhausted | 18 | `，` | U+FF0C | FULLWIDTH COMMA | Halfwidth and Fullwidth Forms | Po | ',' | 全角字符归一化为 ',' |

## 按文件汇总

| 文件 | 异常字符串数 | 异常字符数 |
| --- | --- | --- |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rCN/strings.xml | 18 | 31 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rHK/strings.xml | 8 | 10 |
| /Users/wangzhen/android/git/openspec-project/openspec/android/res/values-zh-rTW/strings.xml | 8 | 10 |
