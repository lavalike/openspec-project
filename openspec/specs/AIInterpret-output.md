# 【假设】AI 同声传译概要设计 V0.1
- **作者**：【假设】
- **日期**：2026-04-07
- **适用范围**：Android V 及以上版本的 TCL 手机/平板海外项目，含蒙娜丽莎高端商务机型同声传译二期能力。

## 1 引言
### 1.1 背景
全球化旅行与商务交流催生实时跨语种沟通需求；蒙娜丽莎机型需结合 TCL 耳机，提供沉浸式 AI 同声传译，形成整机+配件卖点。目标是在文本、对话、同声传译、拍照翻译等场景提供稳定、低延迟的语言服务。

### 1.2 术语和缩略语
| 缩略语 | 全称 | 说明 |
| --- | --- | --- |
| ASR | Automatic Speech Recognition | 语音转文本服务 |
| TTS | Text-to-Speech | 文本转语音输出 |
| MT | Machine Translation | 文本翻译服务 |
| SDK | Software Development Kit | 对接微软语音、Google 翻译等 |
| SiEngine | Simultaneous Interpretation Engine | 会话核心控制，引擎负责 ASR/MT/TTS 等流程 |

### 1.3 参考资料
- AI 翻译需求文档
- Ergo：TCL AI Ergo & GD（P90-104）
- 微软 ASR/TTS 文档与 SDK 示例
- Simultaneous Interpretation_V1.0.0 需求矩阵。

## 2 需求分析
### 2.1 需求概述
#### 2.1.1 需求背景
- 场景：随行翻译、商务会议记录、旅行交流、耳机卖点。
- 渠道：桌面、侧边栏、Settings、TCL AI 等入口直接启动。

#### 2.1.2 需求列表
- 文本/对话/同声传译主流程
- 沉浸模式
- 历史记录编辑与分享
- 画中画小窗、悬浮球模式
- 网络/服务器/敏感词/系统异常处理
- 无障碍适配、暗黑模式
- 功能埋点与数据监控。

#### 2.1.3 需求范围及限制
- Android V+，MTK/QCOM/展锐芯片
- 海外项目（依赖 Google 翻译 SDK）
- 需前台服务 + SYSTEM_ALERT_WINDOW 权限以支持悬浮窗常驻。

#### 2.1.4 需求整体目标
- 多语言对（Google MT + 微软 ASR/TTS），含离线包管理
- 低延迟实时翻译与离线兜底
- 更强场景覆盖：拍照翻译、耳机广播、沉浸模式
- 组件化架构、支持持续优化体验。

### 2.2 需求分析
#### 2.2.1 竞品分析
- 小米双屏同步翻译、AI录音机：端云协同 + 大模型摘要；对标需补齐实时显示、记录结构化能力。

#### 2.2.2 功能性需求分析
| 编号 | 描述 | 优先级 | 说明 |
| --- | --- | --- | --- |
| F1 | 沉浸式同声传译界面（含耳机广播） | P0 | 提供沉浸视图与字幕 |
| F2 | 历史记录编辑/分享 | P0 | 支持敏感词过滤与本地存储 |
| F3 | 画中画 / 悬浮球 | P0 | ForegroundService 持续运行 |
| F4 | 异常处理（网络/服务器/敏感词/系统） | P0 | 提示/降级策略 |
| F5 | 无障碍、暗黑模式 | P0 | 兼容 TalkBack、系统主题 |
| F6 | 功能埋点 | P0 | 接入公司 BI |

#### 2.2.3 非功能性需求分析
- 性能/功耗/安全/DFX 均需与一期持平；关注录音、ASR、蓝牙链接等高功耗路径。
- 可维护、可测试（日志、dumpsys）、可服务（埋点、BI）。
- 可靠性：异常掉电/重启恢复；整句校对逻辑；断网自动暂停并提示。

#### 2.2.4 设计约束分析
- 悬浮窗权限 + 前台服务常驻
- Activity/悬浮窗状态同步但去耦
- 网络/电话/蓝牙/语言监听迁移至进程单例（SiEngine + Service）。

#### 2.2.5 依赖分析
- 外部：ConnectivityManager、TelephonyManager、BluetoothManager、AIAbility（ASR/TTS/翻译、语言包下载）
- 内部：NavBackStack（单 Activity）、全局语言配置 dialogueSource/Target、AI Core Service、Google Lens、BI。

#### 2.2.6 影响分析
- 加入悬浮窗/全局入口需校验系统弹框策略，避免误触
- 依赖耳机蓝牙状态，需与其他音频业务协调
- 新增前台通知，需评估对体验影响
- 语言包下载影响存储与网络，需提示用户
- 对现有文本/对话翻译界面需要保持语言同步配置。

## 3 总体架构设计
### 3.1 零层设计
Interpret 作为系统级 AI 应用的一部分，不支持卸载；与桌面、侧边栏、Settings、TCL AI等入口集成；依赖 AI Core Service 与云端模型管理。

### 3.2 一层设计
#### 3.2.1 系统总体结构框图
- **UI 层**：主界面/对话翻译/文本翻译/同声传译/语言管理、画中画、悬浮球
- **服务层**：SimultaneousService（ForegroundService 控生命周期）
- **数据层**：SiEngine + SiController，管理 ASR/MT/TTS、会话状态、监听
- **资源层**：语言包、配置 DataStore、日志、BI 埋点
- **基础层**：网络、数据库、工具、共享 View。

#### 3.2.2 场景时序图/整体关键流程
1. **主路径**：全屏启动同声传译 → 请求权限/模型 → ASR streaming → MT → TTS → 耳机广播/屏幕显示 → 历史记录落盘。
2. **进入悬浮窗**：Activity 触发 enterOverlayWindowMode → Service 创建 Window → SiOverlayViewModel 同步状态 → 可拖拽/返回全屏。
3. **异常**：
   - 网络断开：ConnectivityManager 回调 → SiEngine pause → UI 提示 → 网络恢复自动继续；
   - 服务器异常：触发 retry()，失败则提示并允许历史浏览；
   - 敏感词：翻译结果标记并提示用户；
   - 语言不一致：语言列表区分语音/文本，提示不可用语言。
4. **耳机断开**：BluetoothManager 回调 → 暂停广播 → 提示切换设备。
5. **电话/系统中断**：TelephonyManager 回调 → 自动暂停 → 恢复后继续。
6. **全屏↔悬浮球**：Overlay 位置/大小持久化，支持最小化 + 气泡提示。

#### 3.2.3 模块分解
| 模块 | 职责 | 功能覆盖 |
| --- | --- | --- |
| UI 主界面 | Compose + NavHost，负责主/沉浸/历史页面 | F1/F2 |
| Overlay/小窗 | WindowManager 渲染，支持悬浮球 | F3 |
| SiHomeViewModel | 全屏状态管理、指令发送 | F1/F4 |
| SiOverlayViewModel | 小窗状态管理 | F3/F4 |
| SimultaneousService | 前台服务、进程单例、窗口控制 | 全局 |
| SiEngine | ASR/MT/TTS 调度、监听、历史写入 | F1~F4 |
| LanguageManager | 语言包下载/删除、当前配置 | F1/F3 |
| HistoryRepository | 本地数据库/文件 | F2 |
| BI Logger | 埋点、日志 | F6 |

### 3.3 开发和运行环境
- 开发：Windows + Android Studio，Kotlin + Compose
- 运行：Android V+，实机测试（手机/平板），耳机蓝牙链路。

### 3.4 模块开发方式说明
- 新开发：SimultaneousService、SiEngine、Overlay UI
- 改进：文本/对话翻译模块、语言管理模块
- 复用：AI Core Service、BI 系统、Google Lens Intent
- 依赖第三方：微软 ASR/TTS、Google 翻译/拍照。

### 3.5 技术方案风险点
1. AI 模型容量影响 APK 体积 → 统一由 AI Core 管理共享模型。
2. 语音识别/文本翻译语言列表不一致 → UI 提示、区分列表。
3. 整句校对与逐字输出不一致 → 使用 Recognizing/Recognized 双通道并加标点断句。
4. 悬浮窗权限/前台通知体验风险 → 提供引导页与通知管理入口。
5. 画中画兼容性 → Android 8+ TYPE_APPLICATION_OVERLAY + 前台服务。

## 4 二层设计（模块内部设计）
### 4.1 语音识别模块
- 结构：录音器 → ASR SDK → Recognizing/Recognized 回调 → 文本缓冲 → UI。
- 流程：启动会话 → 请求麦克风 + 网络 → streaming 识别 → Recognizing 更新 UI → Recognized 写入历史 → 断句/敏感词检测。
- 时序：Service 驱动 SiEngine.start → ASR Callback → ViewModel stateFlow → Compose Render。
- 并发：ASR 运行于独立线程，主线程仅订阅状态；异常时自动重连或提示。

### 4.2 翻译模块
- 结构：文本输入（ASR/手动/拍照）→ Google MT API → 文本结果。
- 拍照翻译：通过 Intent 调起 Lens Activity（`ACTION_VIEW` + ClassName `com.google.android.apps.search.lens.LensActivity`），结果回写到历史列表。
- 流程：输入→语言校验→在线/离线判定→调用 MT→错误重试→敏感词过滤→UI 展示。
- 并发：翻译任务放入线程池，支持重试/取消；网络异常退回 offline 提示。

### 4.3 语音播放模块
- 结构：文本→微软 TTS→音频流→耳机/扬声器。
- 流程：判断耳机连接→生成 TTS 请求→播放控制（turnOn/OffBroadcast）→音量与焦点管理。
- 并发：播放线程与 ASR 线程分离，支持暂停/继续。

### 4.4 语言管理模块
- 结构：Google SDK（翻译包）+ TCL 云（ASR/TTS 模型）+ DataStore 缓存列表。
- 流程：获取支持列表→展示下载状态→触发下载/删除→进度通知→更新当前语言。
- 时序：UI 请求 → LanguageManager → Google/TCL 接口 → 回调更新 UI。
- 并发：下载任务启用 WorkManager，支持断点续传。

### 4.5 历史记录模块
- 本地数据库（Room）存储会话文本/时间/语言/分享状态。
- 编辑：提供合并、删除敏感信息。
- 分享：生成文本/图片，调用系统分享面板。

## 5 接口设计
### 5.1 提供接口
#### 5.1.1 外部接口
| 接口 | 描述 | 方式 |
| --- | --- | --- |
| ASR | 语音转文本 | AI Core Service / ASR Service |
| MT | 文本翻译 | AI Core Service / MT Service |
| TTS | 文本转语音 | AI Core Service / TTS Service |
| 拍照翻译 | 调用 Google Lens | Intent |
| 隐私/意见反馈 | 调用系统 SDK | SDK |
| 版本号 | 调用系统 AOTA | AIDL |
| 监控日志 | BI 埋点 | SDK |

#### 5.1.2 内部接口
`SiHomeViewModel`, `SiOverlayViewModel`, `SimultaneousService`, `SiEngine`, `SiOverlayWindowRepository` 提供的 enter/pause/continue/stop/turnOnBroadcast/updateWindow 等方法。

### 5.2 依赖接口
- 系统：ConnectivityManager、TelephonyManager、BluetoothManager、NotificationManager
- AIAbility：ASR/TTS/翻译、语言包下载
- TCL Cloud：语音模型下载
- Google Lens 服务

## 6 非功能设计
### 6.1 性能
- 启动时间与同声传译一期持平；ASR 延迟 < 500ms、MT < 1s、TTS < 1s。
- 避免新增进程/线程；若需额外线程需在方案评审通过。
- 监控 CPU/GPU/RAM，评估导入/导出流程。

### 6.2 功耗
- 录音/ASR/蓝牙为高功耗；提供暂停策略、耳机断连自动停播。
- 待机时关闭麦克风/网络请求，避免后台耗电。

### 6.3 内存
- 常驻内存增量控制 < 20MB；动态内存主要来自音频 buffer 与 TTS 播放。
- 模型不随 APK 打包，调用 AI Core 共享。

### 6.4 可靠性（DFR）
- 出错表：网络断开→暂停+重试，服务器异常→提示+可重试，敏感词→提示+屏蔽，系统异常→保存草稿+恢复。
- 异常掉电/重启：使用 DataStore/数据库持久化当前会话与悬浮窗状态。
- Logs：ASR/TTS/MT 关键阶段打印。

### 6.5 安全性（DFSe）
- 敏感权限最小化，麦克风/蓝牙/Overlay/ForegroundService 均需用户授权。
- 数据加密存储历史记录，符合 GDPR；通信走 HTTPS + SDK 内部加密。
- 开源合规：微软/Google SDK License 已评估，内部实现避免 GPL。

### 6.6 可维护性
- MVI 架构 + 组件化。
- Service/Engine 分层，便于扩展。
- 配置中心统一管理 Feature。

### 6.7 可测试性（DFT）
- 提供 dumpsys/shell 命令查看会话状态。
- 埋点与日志可在线排查。
- 测试 APK 支持模拟网络/服务器异常。

### 6.8 可服务型性（DFS）
- BI 埋点：入口、会话时长、耳机状态、异常类型。
- FCM/云端配置可远程控制特性/灰度。

### 6.9 可配置性（DFCu）
- Feature Flag 控制沉浸模式、悬浮窗、小窗广播。
- 内外销差异：海外打开 Google SDK，内销保持关闭。
- 平台差异：按芯片项目配置语言包列表。

### 6.10 兼容性（DFC）
- Android V+ (Android 12+)；MTK/QCOM/展锐全档位。
- 耳机协议：蓝牙 LE/Classic，需向下兼容。
- 支持多品牌 ROM，若缺少 Google 服务则关闭相关入口。

### 6.11 解耦
- 通过组件化 + 接口隔离 AI 服务。
- Overlay 与 Activity 状态解耦；语言管理/BI 解耦为单独模块。

### 6.12 全球化
- 支持 59 种离线文本语言 (Google)，15 种语音语言 (微软)；列表区分并提示。
- 支持系统语言/区域自动推荐；多语言 UI 字符串维护。

## 7 数据结构设计
- **LanguageConfig**：源/目标语言、下载状态；并发访问通过 Mutex 保护。
- **HistoryEntry**：id、timestamp、speaker、sourceText、targetText、shareStatus、sensitiveFlag。
- **OverlayState**：windowSize、location、mode、locked；存储在 DataStore。
- **SessionState**：ASR status、MT status、TTS status、errorType；stateFlow 广播。

## 8 数据库设计（可选）
- Room 数据库：`history_table`，索引 timestamp，支持搜索/分享；可选云端同步。

## 9 验收标准与测试建议
- 功能：同声传译主流程、悬浮窗切换、历史分享、异常场景。
- 性能：ASR/MT/TTS 延迟、CPU/RAM、功耗。
- 可靠性：网络闪断、电话打断、耳机插拔、系统重启恢复。
- 安全与合规：权限提示、隐私政策。
- 可测试性：日志/命令覆盖。
- 埋点：与 BI 报表核对。

## 10 风险与应对
| 风险 | 描述 | 等级 | 缓解 |
| --- | --- | --- | --- |
| 模型体积大 | 多语言模型影响存储 | 中 | AI Core 统一管理、按需下载 |
| 语音/文本语言不一致 | 微软/谷歌支持范围不同 | 中 | 分列表展示、灰掉不支持 |
| 整句校对滞后 | Recognized 与实时结果差异 | 中 | 双通道输出 + 标点断句 |
| 悬浮窗权限受限 | Android 8+ 权限限制 | 中 | 权限引导 + ForegroundService |
| 蓝牙/耳机依赖 | 耳机断连影响沉浸体验 | 中 | 监听回调→暂停→提示 |
| 功耗 | 长时间录音/TTS | 中 | 自动暂停、耳机广播可控 |

## 11 待确认问题
1. 蒙娜丽莎项目是否需要定制 UI 主题或品牌元素？
2. 历史记录是否需要云端同步/多端共享？
3. Google 服务缺失地区的替代方案？
4. 是否引入大模型摘要能力？
5. 耳机广播是否支持多设备同时推送？
