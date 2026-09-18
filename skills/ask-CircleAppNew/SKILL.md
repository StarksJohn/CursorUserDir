---
name: ask-CircleAppNew
description: >-
  CircleApp 私有恢复与专项路由入口。仅在用户显式使用独立入口词
  /ask-CircleAppNew 或 @ask-CircleAppNew，或明确要求继续受保护待办、恢复跨会话状态、
  处理外部构建发布阻塞时使用。每个新 chat 先调用本入口；随后强制读取 Codex
  对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-CircleAppNew（Cursor）

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/CircleAppNew/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\CircleAppNew\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只处理私有恢复状态、受保护待办、专项路由和外部构建/发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。
- 普通一次性任务优先在新 chat 第一条消息中同时写 `/ask-CircleAppNew` 和任务正文；只有需要跨 chat、跨设备或长周期恢复时，才把任务放入本文件受保护区后仅输入入口词继续。

## 路径与事实源

- 项目根：Windows `D:\work\RN\CircleAppNew`；macOS `/Users/<你的用户名>/Desktop/work/RN/circleapp`，当前 Mac 为 `/Users/stark/Desktop/work/RN/circleapp`。用户给出 fork、worktree 或其它路径时以用户路径为准。
- Cursor 入口：Windows `%USERPROFILE%\.cursor\skills\ask-CircleAppNew\SKILL.md`；macOS `/Users/<你的用户名>/.cursor/skills/ask-CircleAppNew/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\CircleAppNew\SKILL.md`；macOS `/Users/<你的用户名>/.codex/skills/CircleAppNew/SKILL.md`。
- 业务逻辑、API 映射、导航、i18n、UI 行为和错误处理：以当前 `src/`、`ios/`、`android/` 和测试为准。
- 稳定工程约束只维护在 Codex 对口目录的 `AGENTS.md`；不创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- 技术栈、脚本、依赖、环境、构建和发布方式：以 `package.json`、项目配置和 `README*` 为准。
- Play 16KB / 原生库对齐：仅在该任务出现时读取仓库根 `16KB_PAGE_SIZE_SOLUTION_GUIDE.md`；具体 `.so` 以 Play 报错或本地分析结果为准。
- 当前任务、外部状态和最小下一步：以用户本轮消息、受保护的“当前活跃需求”和实时证据为准，不在入口正文复制状态流水。
- `CLAUDE.md` 可能含过期版本或敏感操作说明；只按任务读取相关段落，并以当前源码为准，不复述或新增账号、密码、token、Cookie、私钥、keystore 密码和生产密钥。

发生冲突时，当前源码、Git、ADB/Xcode/Gradle/Metro、真实页面和外部系统实时结果优先于历史摘要；产品范围、医疗合规和外部 contract 以负责人最新确认优先。

## 与 Codex 入口对齐

- 两份入口分别维护，但事实源优先级、最小读取顺序、上下文门禁、授权边界、实施流程和输出约定保持一致。
- 在 Cursor 的 Codex 插件中输入 `/CircleAppNew`，应与 Cursor 输入框中执行 `/ask-CircleAppNew` 对同一明确任务达到相同推进效果。
- 两份“当前活跃需求”由用户维护；除非用户明确授权，不改写其文字、注释状态、层级或图片引用。Codex 受保护区块若要求读取本入口的「当前活跃需求」，只读取、不改写。用户本轮明确任务始终优先。

## 启用与最小读取顺序

1. 完整读取本 `SKILL.md`；已在当前 chat 实际加载且未变化的文件不重复读取。
2. 确认 Codex 对口 Skill 同目录 `AGENTS.md` 已读取，再按任务读取相关 `.cursor/rules/*` 或仓库 `.cursorrules`；不要读取或创建 `project-context.mdc`。
3. 读取任务直接相关的源码、测试和原生配置；需要脚本、依赖或环境事实时，再读取 `package.json`、`README.md`、`CLAUDE.md`、`16KB_PAGE_SIZE_SOLUTION_GUIDE.md` 中实际存在且与任务相关者。
4. 普通实现、排障和审查不默认读取 Codex 对照入口；仅在用户调用 `$CircleAppNew` / `/CircleAppNew`、两份入口需要对齐，或任务事实只存在于对照入口时读取。
5. 用户只有入口口令而没有新任务时，执行本文件“当前活跃需求”中第一个未注释且可行动的事项；已有明确新任务时，不自动展开无关活跃项。
6. 路由到其它 Skill、ask、command 或 `bmad-*` 前，先完整读取对应 `SKILL.md` 及其明确要求的 `workflow.md`、`checklist.md`、`reference.md`。
7. 当前任务涉及 Markdown 图片引用时，先按引用文件同目录精确读取全部相关图片；读取失败后再搜索，不得用文字摘要代替图片事实。

不要默认通读仓库、全部 README 或另一客户端入口，也不要把历史摘要当成已加载的当前事实。

## 实施工作流

1. 确认实际工作区、Git 分支、工作树和任务授权边界；保留用户已有改动，不扩大到无关重构、提交、push、部署或外部系统写操作。
2. 按实现、排障、API、i18n、导航、原生构建、真机、审查或设计还原分类，只读取能决定下一步的高价值文件。
3. 代码任务依次完成真实业务实现、同项目内测试/验证；确认无需继续改代码后，再更新项目文档或项目外入口资料。
4. API contract 可由真实页面触发时，先读取实际请求与响应；受登录、权限或页面状态阻塞后，再查源码、Swagger 或 OpenAPI。
5. Figma URL、节点或设计还原任务必须先通过 Figma MCP 读取节点事实；截图和浏览器 DOM 只能补充验证。
6. 开发阶段优先单文件、单用例、单平台或单设备验证；阶段收尾再按风险扩大矩阵。未运行的测试、应用或真机流程必须明确说明。
7. 不因普通代码改动更新本 Skill；只有入口、事实源、跨客户端对齐、长期门禁或受保护活跃需求由用户授权变更时才更新。

## 项目工程约束

- React Native、React、TypeScript、React Navigation、依赖版本、scripts 和 locale 清单的精确值以当前仓库为准。
- API 复用 `src/api` 既有 client、endpoint 和 DTO/type；导航改动同步 screen 注册、参数类型、深链和回退行为。
- 新增用户可见文案时同步项目当前约定的全部 locale；语言清单以 `src/i18n` 为准，不从历史 Skill 猜测。
- 跨平台逻辑优先使用公共字段；第三方 SDK 或原生桥接标记 `iOS ONLY`、`ANDROID ONLY`、deprecated 或 experimental 时，先核对类型定义或官方文档，并显式处理另一平台。
- 遵循项目现有函数组件、Hooks、Context、EStyleSheet / 主题、路径别名和原生 flavor 约定；不为统一形式改变运行语义。
- 环境与构建使用仓库现有脚本和 Gradle / Xcode 配置；不要凭旧笔记复制 `.env`、切换 flavor 或改变签名流程。
- 医疗健康文案避免确诊式、保证疗效式或替代医生建议式表达。
- 非必要不新增依赖；不写入或输出 token、Cookie、密码、私钥、证书、keystore 密码、生产密钥和测试账号明文。
- 未经用户授权不做无关重构，也不假设 Heals、Amber、CS Mobile 或 New Town 与本项目结构相同。

## 用户已有日志保护硬门禁

- 当前源码中的 `console.log`、`console.info`、`console.warn`、`console.error`、自定义 logger、debugger、trace 和诊断 Hook 均视为用户已有代码。除非用户在本轮明确要求删除、注释、降级、脱敏、替换或重构某一条具体日志，否则必须逐条保留；“解决警告或报错”、真机检查、日志清洁、安全/隐私诊断、lint 或测试失败都不构成修改日志的授权。
- 日志记录到 warning/error 时优先修复实际根因，不得通过删除、屏蔽、改写或降低日志级别制造“无错误”结果。若根因属于外部服务、账号、云配置、依赖或环境，只报告边界和必要下一步，保留原日志。
- 发现日志可能包含敏感数据、输出过多、影响性能或与现有测试冲突时，只收集最小必要证据且不在回复复述敏感值；报告精确文件/行、风险和可选方案并等待用户授权。不得自行修改源码或测试来消除该日志，也不得以历史改动、记忆、测试断言、lint、code review 或前一代理行为推定授权。
- 用户明确授权日志改动后，只修改点名范围；收尾时单独复核 `console.*`、logger、debugger、trace 和诊断 Hook 的 diff，并逐项报告实际变化及原因。

## 运行、发布与外部系统门禁

- Android 真机任务：先从 `package.json` 核对脚本和 flavor/env，再用 `adb devices -l` 锁定设备；只处理属于本项目且阻塞本次运行的旧进程。成功至少需要构建/安装/启动结果、目标包进程和前台 Activity 证据，不能只看端口或 Gradle 成功。Windows 与 macOS 的脚本名可能不同，以当前 `package.json` 为准。
- Android 发布 / Play / 16KB 任务：先核对 flavor、`applicationId` / suffix、`versionName` / `versionCode` 和产物路径；AAB/APK 校验、商店页面状态和 16KB 对齐结果分开报告。16KB 结论写入或更新 `16KB_PAGE_SIZE_SOLUTION_GUIDE.md`，不把 `.so` 清单复制进本 Skill。未经授权不上传商店、不提交 Git。
- iOS 任务：先核对 scheme、configuration、Bundle ID、Team、version/build、Xcode/SDK 和签名；上传、测试群组、出口合规和 App Store 发布分别授权。外部页面上的 build、tester、group 和处理状态必须实时复核。
- Git/release 任务：先检查远端 refs、完整拓扑、工作树、提交差异和最终树；“方向看起来安全”或只询问是否应合并，不等于授权 merge、删分支、push 或发布。
- 浏览器和外部代码平台任务：使用当前已授权的真实会话并验证完整数据，不把可见列表或编辑器 viewport 当作完整源码；外部 Web 项目与本地 React Native checkout 分开判断。

## 文档维护规则

- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
- `README.md` 保存通用工程说明；`CLAUDE.md` 不作为版本或密钥事实源。`16KB_PAGE_SIZE_SOLUTION_GUIDE.md` 只保存 16KB 对齐流程与结论。
- 不把字段清单、业务规则、默认值、单次分支/commit/PID、构建结果、测试数量、当前阻塞或聊天流水写入入口 Skill 或 README。
- 有新的可复用事实时，先完成项目代码和测试，再更新现有对应章节；直接修正过期内容并去重，不按日期追加。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，否则保持其子内容原文。
- 最终回复默认只报告产出、验证、风险和必要下一步；不输出文件加载清单，除非用户本轮明确要求。

## 输出与边界

- 对用户使用简体中文；代码与代码注释使用英文；引用真实文件时给出路径和必要行号。
- 诚实区分已验证、部分验证、外部阻塞和未执行；不把构建成功写成真机功能验收完成。
- 不把医学建议写成确诊或处方替代，不混入其它项目假设，不创建无关文档或脚本。

## 当前活跃需求(不要修改这部分的子内容)

<!-- - **Android / Google Play — 16KB 内存页大小**  
  - 场景：在 `android` 下构建 **prodRelease** AAB 并上传 Play Console 后出现 **Does not support 16 KB** / 原生库未对齐 16KB 页面等提示。  
    - 之前的具体报错是 Libraries that do not support 16 KB:
      base/lib/arm64-v8a/libHealthyMonitor.so
      base/lib/arm64-v8a/libabsl.cr.so
      base/lib/arm64-v8a/libbloodsuger.so
      base/lib/arm64-v8a/libbodytemp.so
      base/lib/arm64-v8a/libc++_chrome.cr.so
      base/lib/arm64-v8a/libc++_shared.so
      base/lib/arm64-v8a/libchrome_zlib.cr.so
      base/lib/arm64-v8a/libfbjni.so
      base/lib/arm64-v8a/libhermes.so
      base/lib/arm64-v8a/libhermestooling.so
      base/lib/arm64-v8a/libicuuc.cr.so
      base/lib/arm64-v8a/libimagepipeline.so
      base/lib/arm64-v8a/libjsi.so
      base/lib/arm64-v8a/liblibox.so
      base/lib/arm64-v8a/libnative-filters.so
      base/lib/arm64-v8a/libnative-imagetranscoder.so
      base/lib/arm64-v8a/liboxygen.so
      base/lib/arm64-v8a/libpartition_alloc.cr.so
      base/lib/arm64-v8a/libpdfium.cr.so
      base/lib/arm64-v8a/libpdfiumandroid.so
      base/lib/arm64-v8a/libreactnative.so
      base/lib/arm64-v8a/libreanimated.so
      base/lib/arm64-v8a/librnscreens.so
      base/lib/arm64-v8a/libworklets.so
      base/lib/x86_64/libHealthyMonitor.so
      base/lib/x86_64/libNskAlgo.so
      base/lib/x86_64/libabsl.cr.so
      base/lib/x86_64/libbloodsuger.so
      base/lib/x86_64/libbodytemp.so
      base/lib/x86_64/libc++_chrome.cr.so
      base/lib/x86_64/libc++_shared.so
      base/lib/x86_64/libchrome_zlib.cr.so
      base/lib/x86_64/libconceal.so
      base/lib/x86_64/libfbjni.so
      base/lib/x86_64/libhermes.so
      base/lib/x86_64/libhermestooling.so
      base/lib/x86_64/libicuuc.cr.so
      base/lib/x86_64/libimagepipeline.so
      base/lib/x86_64/libjsi.so
      base/lib/x86_64/liblibox.so
      base/lib/x86_64/libnative-filters.so
      base/lib/x86_64/libnative-imagetranscoder.so
      base/lib/x86_64/libneuroskybpi.so
      base/lib/x86_64/liboxygen.so
      base/lib/x86_64/libpartition_alloc.cr.so
      base/lib/x86_64/libpdfium.cr.so
      base/lib/x86_64/libpdfiumandroid.so
      base/lib/x86_64/libreactnative.so
      base/lib/x86_64/libreanimated.so
      base/lib/x86_64/librnscreens.so
      base/lib/x86_64/libworklets.so
      Libraries that do not support 16 KB:
      base/lib/arm64-v8a/libHealthyMonitor.so
      base/lib/arm64-v8a/libbloodsuger.so
      base/lib/arm64-v8a/libbodytemp.so
      base/lib/arm64-v8a/libc++_shared.so
      base/lib/arm64-v8a/libfbjni.so
      base/lib/arm64-v8a/libhermes.so
      base/lib/arm64-v8a/libhermestooling.so
      base/lib/arm64-v8a/libimagepipeline.so
      base/lib/arm64-v8a/libjsi.so
      base/lib/arm64-v8a/liblibox.so
      base/lib/arm64-v8a/libnative-filters.so
      base/lib/arm64-v8a/libnative-imagetranscoder.so
      base/lib/arm64-v8a/liboxygen.so
      base/lib/arm64-v8a/libpdfiumandroid.so
      base/lib/arm64-v8a/libreactnative.so
      base/lib/arm64-v8a/libreanimated.so
      base/lib/arm64-v8a/librnscreens.so
      base/lib/arm64-v8a/libworklets.so
      base/lib/x86_64/libHealthyMonitor.so
      base/lib/x86_64/libNskAlgo.so
      base/lib/x86_64/libbloodsuger.so
      base/lib/x86_64/libbodytemp.so
      base/lib/x86_64/libc++_shared.so
      base/lib/x86_64/libconceal.so
      base/lib/x86_64/libfbjni.so
      base/lib/x86_64/libhermes.so
      base/lib/x86_64/libhermestooling.so
      base/lib/x86_64/libimagepipeline.so
      base/lib/x86_64/libjsi.so
      base/lib/x86_64/liblibox.so
      base/lib/x86_64/libnative-filters.so
      base/lib/x86_64/libnative-imagetranscoder.so
      base/lib/x86_64/libneuroskybpi.so
      base/lib/x86_64/liboxygen.so
      base/lib/x86_64/libpdfiumandroid.so
      base/lib/x86_64/libreactnative.so
      base/lib/x86_64/libreanimated.so
      base/lib/x86_64/librnscreens.so
      base/lib/x86_64/libworklets.so
      ,经过我之前修改之后,目前只剩下如图![img_174548.png](img_174548.png)里的 `Linktop SDK` 相关的问题,
  - **本仓库事实源**：优先阅读并维护 `{workspace}/16KB_PAGE_SIZE_SOLUTION_GUIDE.md`（若已存在则以其为流程与结论主文档）。  
  - **可参考先例**：`D:\work\RN\amber-medical-app-rn\16KB_PAGE_SIZE_SOLUTION_GUIDE.md` 中的解决思路（迁移到本仓库时需按当前 Gradle、NDK、依赖版本调整）。  
  - 具体涉及的 `.so` 列表以 **Play 报错或本地分析结果** 为准，不必在 skill 内重复冗长清单。
  - 把你每轮的回答都用最精简的内容更新到 `{workspace}/16KB_PAGE_SIZE_SOLUTION_GUIDE.md`（业务仓库根：**Windows** `D:\work\RN\CircleAppNew`；**macOS** `/Users/<你的用户名>/Desktop/work/RN/circleapp`，当前 Mac：`/Users/stark/Desktop/work/RN/circleapp`）,保证每次开启新的chat后,都可以借助 这个文档 恢复这个项目的最小必要上下文;不要修改 **Windows** `%USERPROFILE%\.cursor\skills\ask-CircleAppNew\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-CircleAppNew/SKILL.md` 的 `当前活跃需求` 里的内容 -->

# win
<!-- - 在业务仓库根目录执行（**Windows** `D:\work\RN\CircleAppNew`；**macOS** `/Users/<你的用户名>/Desktop/work/RN/circleapp`，当前 Mac：`/Users/stark/Desktop/work/RN/circleapp`）
  - `cd android; .\gradlew assembleRelease`
    -  `npm run android:dev_win` 把当前项目的debug模式 -->
  <!-- - 的app运行到了如图![img_114112.png](img_114112.png)![img_114124.png](img_114124.png)型号的真机上,真机所在的时区是 `东八区` -->
<!-- - 我现在想 构建 这个项目的 prod 环境的 `.aab` 文件 ; 是否需要先 copy `.env.production` to `.env`,再 执行 `./gradlew bundleProdRelease `; 还是直接执行  `./gradlew bundleProdRelease `? -->

# MAC
- IOS:
  <!-- - 为当前 checkout 构建 `dev` 环境的 `xxx`版本的 Release 模式 的 IPA,使用前把 `xxx` 换成 `1.0.3`, 作为真实的 `version`，并真实上传到 CircleApp / CDV Health (Dev) 的 TestFlight：`https://appstoreconnect.apple.com/teams/1f49f429-f33a-4c15-b357-7025b5e32451/apps/6781207370/testflight/ios`（Apple ID `6781207370`，套装 ID `com.healshealthcare.circlemedical.dev`）。上传前仍须在当前登录态打开该页，确认 App 名称是 `CDV Health (Dev)` 且套装 ID 仍匹配；禁止沿用 Heals Dev `6740129703`、Heals Prod `6544800416`，也禁止把 `android/google-services.json` 残留 `app_store_id` `6544800416` 当作本项目 App Store ID。本任务明确授权构建和上传，但不授权自动提交 Git、push、分配测试群组、回答出口合规问题或发布到 App Store。
    1. 先确认项目根、当前分支、HEAD 和工作树；保留已有未提交改动，不执行 clean/reset，不覆盖无关文件。读取 `ios/Circle.xcworkspace`、scheme `Dev Release`、`ios/Circle.xcodeproj` 的 Circle target build settings、`Circle/Info.plist`、`Podfile` 和相关发布说明，以源码和真实构建结果为准。
    2. 目标营销版本优先使用用户本轮明确指定的 version；用户未指定时，读取 Circle target 的 `Dev Release` configuration 当前 `MARKETING_VERSION` 并保持不变，不擅自升级版本。目标必须是 scheme `Dev Release` + configuration `Dev Release`，产物 `Circle.app`，Bundle ID 必须为 `com.healshealthcare.circlemedical.dev`，显示名 `CDV Health (Dev)`，Team ID 必须为 `HS8K5BGDV7`；不得误改或误上传 scheme `Circle`（Prod `Release`）或 `Dev Debug`，也不得使用 CircleTests 残留的 `com.healshealthcare.healspass` / `com.healshealthcare.healspass.dev`。
    3. 构建前通过当前登录态打开 Dev App `6781207370` 的 iOS TestFlight 页，核对名称 `CDV Health (Dev)` 与套装 ID `com.healshealthcare.circlemedical.dev` 后读取 iOS TestFlight 构建列表和详情；核对目标 version 下以及历史列表中已使用的 build number，选择未使用、严格递增且符合 Apple 当前 `CFBundleVersion` 格式的 build number。优先使用比已确认最大值大 1 的纯十进制正整数；不得只根据本地工程、截图日期或历史摘要猜测，也不得使用未经验证的 Heals App ID。若登录、权限、App 名称/套装 ID 不匹配、或页面读取失败，停止在上传前并明确报告阻塞。
    4. 只更新 Circle target 的 `Dev Release` configuration 对应的 `MARKETING_VERSION` 和 `CURRENT_PROJECT_VERSION`，然后通过 `xcodebuild -workspace ios/Circle.xcworkspace -scheme 'Dev Release' -configuration 'Dev Release' -showBuildSettings` 再次核对 version、build、Bundle ID、configuration 和 Team；不要连带修改 `Release` / `Debug` / `Dev Debug` 或 CircleTests。
    5. 归档前执行 `xcode-select -p`、`xcodebuild -version`、`xcrun --sdk iphoneos --show-sdk-version`，确认默认 Xcode/SDK 满足 Apple 当前上传门禁。本机应优先使用 `/Applications/Xcode.app/Contents/Developer`；若默认仍指向旧 Xcode，在获得系统管理员授权后切换并复核。不得继续上传由不满足当前门禁的旧 SDK 生成的 Archive/IPA。
    6. 检查是否已有其它 `xcodebuild` 正在使用相同 DerivedData、Archive 或 `build.db`；只保留一个归档任务，并为本次 version/build 使用唯一、可追溯的 DerivedData 和 Archive 路径，避免并发构建互相锁库或污染产物。
    7. 从项目根使用 `.env.development`、workspace `ios/Circle.xcworkspace`、scheme `Dev Release`、configuration `Dev Release`、generic iOS destination、automatic signing 和正确 Team 归档；禁用 Sentry 自动上传，保留符号上传警告供结果判断。该 scheme 的 `ArchiveAction` 才是 `Dev Release`，`ProfileAction` 仍指向 `Release`，本任务只走 `archive`。推荐命令骨架：`ENVFILE=.env.development SENTRY_DISABLE_AUTO_UPLOAD=true xcodebuild -workspace ios/Circle.xcworkspace -scheme 'Dev Release' -configuration 'Dev Release' -destination 'generic/platform=iOS' -derivedDataPath <unique-derived-data> -archivePath <unique-archive>.xcarchive CODE_SIGN_STYLE=Automatic DEVELOPMENT_TEAM=HS8K5BGDV7 -allowProvisioningUpdates archive`。
    8. Archive 成功后先独立核验归档内 App 的 `CFBundleIdentifier`、`CFBundleShortVersionString`、`CFBundleVersion`、`DTSDKName`、`DTXcode`、TeamIdentifier 和 `codesign --verify --deep --strict`；任一值不符时不得导出或上传。`CFBundleIdentifier` 必须是 `com.healshealthcare.circlemedical.dev`。
    9. 使用 `method=app-store-connect`、automatic signing、正确 Team、`manageAppVersionAndBuildNumber=false` 的 ExportOptions 导出本地 IPA。再次解包核对 Bundle ID、version/build、SDK、Apple Distribution 证书、Store provisioning profile、`get-task-allow=false`、`beta-reports-active=true` 和深度签名，并记录 IPA 绝对路径、字节数和 SHA-256；不得用未经验证的旧 IPA 代替本次产物。
    10. 仅在 IPA 校验通过后，通过 Xcode/App Store Connect 正式上传到 Dev App `6781207370`。成功标准必须同时满足：上传工具明确返回 `Upload succeeded`，并且该 App 的 App Store Connect “构建版本上传”或目标 version 列表真实出现本次 version/build。等待 Apple 处理到可辨识的最终状态；若显示“缺少出口合规证明”，只报告并交回用户决定，不代替用户作合规声明。Agora/Hermes 等 dSYM 缺失警告与上传失败分开报告，不得把有警告的成功上传写成失败，也不得隐瞒其对原生崩溃符号化的影响。
    11. 上传或网络异常时，先判断 Apple 是否已收到该 version/build，再决定是否重试；Apple 已接收或正在处理时不得重复上传相同构建。网络超时按当前 Mac 的 VPN/代理规则排查；Apple 明确拒绝时保留错误原文和 request/response ID，修复根因后重新归档并使用未占用的 build number。
    12. 最终报告目标 App（含实时读到的 App Store Connect App ID）、version/build、Xcode/SDK、Archive 和 IPA 路径、IPA 大小/SHA-256、签名与 provisioning 校验、上传回执、App Store Connect 实际状态、dSYM/合规风险和未覆盖范围。除非用户明确要求，不提交或 push；完成项目产物和验证后，仅把新增或变化的通用工程/环境/发布事实更新到项目 `README_stark.md`（仓库根当前无此文件时不要新建，也不要写入 `README.md` 的账号段落），不写单次状态流水或秘密。 -->
  <!-- - 为当前 checkout 构建 `prod` 环境的 `xxx` 版本的 Release 模式 IPA,使用前把 `xxx` 换成 `1.0.3`, 作为真实的 `version`，并真实上传到 CircleApp / CDV Health 的 TestFlight：`https://appstoreconnect.apple.com/teams/1f49f429-f33a-4c15-b357-7025b5e32451/apps/6748490218/testflight/ios`（Apple ID `6748490218`，套装 ID `com.healshealthcare.circlemedical`）。上传前仍须在当前登录态打开该页，确认 App 名称是 `CDV Health` 且套装 ID 仍匹配；禁止沿用 Heals Prod `6544800416`、Heals Dev `6740129703`，也禁止把 `android/google-services.json` 残留 `app_store_id` `6544800416` 当作本项目 App Store ID。上传后必须保证该页测试用户列表包含如图 ![img_143933.png](img_143933.png) 的内部测试员及其设备：`cham2015@126.com` / 彭燕 / 内部 / iPad Air（第三代）/ iOS 18.7.8。本任务明确授权构建、上传，以及为保证该内部测试员/设备出现在测试用户列表而进行的核对、补齐内部测试员、把该测试员加入已有内部测试群组；但不授权自动提交 Git、push、邀请截图以外的新测试员、创建新 Apple ID、回答出口合规问题或发布到 App Store。
    1. 先确认项目根、当前分支、HEAD 和工作树；保留已有未提交改动，不执行 clean/reset，不覆盖无关文件。读取 `ios/Circle.xcworkspace`、scheme `Circle`、`ios/Circle.xcodeproj` 的 Circle target build settings、`Circle/Info.plist`、`Podfile` 和相关发布说明，以源码和真实构建结果为准。
    2. 目标营销版本优先使用用户本轮明确指定的 version；否则使用本条标题里已替换的 `xxx`；若标题仍是占位符 `xxx` 且本轮未指定，读取 Circle target 的 `Release` configuration 当前 `MARKETING_VERSION` 并保持不变，不擅自升级版本。目标必须是 scheme `Circle` + configuration `Release`（该 scheme 的 `ArchiveAction` 为 `Release`，`LaunchAction` 为 `Debug`），产物 `Circle.app`，Bundle ID 必须为 `com.healshealthcare.circlemedical`，显示名 `CDV Health`，Team ID 必须为 `HS8K5BGDV7`；不得误改或误上传 `Dev Release` / `Dev Debug`，也不得使用 CircleTests 残留的 `com.healshealthcare.healspass`。当前工程里 Circle `Debug` 的 `CURRENT_PROJECT_VERSION` 与 `Release` 并不相同，不得为了“对齐”去改 `Debug`。
    3. 构建前通过当前登录态打开 Prod App `6748490218` 的 iOS TestFlight 页，核对名称 `CDV Health` 与套装 ID `com.healshealthcare.circlemedical` 后读取 iOS TestFlight 构建列表和详情；核对目标 version 下以及历史列表中已使用的 build number，选择未使用、严格递增且符合 Apple 当前 `CFBundleVersion` 格式的 build number。优先使用比已确认最大值大 1 的纯十进制正整数；不得只根据本地工程、截图日期或历史摘要猜测，也不得使用未经验证的 Heals App ID。若登录、权限、App 名称/套装 ID 不匹配、或页面读取失败，停止在上传前并明确报告阻塞。
    4. 只更新 Circle target 的 `Release` configuration 对应的 `MARKETING_VERSION` 和 `CURRENT_PROJECT_VERSION`；不要连带修改 `Dev Release` / `Dev Debug` / `Debug` 或 CircleTests。然后通过 `xcodebuild -workspace ios/Circle.xcworkspace -scheme Circle -configuration Release -showBuildSettings` 再次核对 version、build、Bundle ID、configuration 和 Team。
    5. 归档前执行 `xcode-select -p`、`xcodebuild -version`、`xcrun --sdk iphoneos --show-sdk-version`，确认默认 Xcode/SDK 满足 Apple 当前上传门禁。本机应优先使用 `/Applications/Xcode.app/Contents/Developer`；若默认仍指向旧 Xcode，在获得系统管理员授权后切换并复核。不得继续上传由不满足当前门禁的旧 SDK 生成的 Archive/IPA。
    6. 检查是否已有其它 `xcodebuild` 正在使用相同 DerivedData、Archive 或 `build.db`；只保留一个归档任务，并为本次 version/build 使用唯一、可追溯的 DerivedData 和 Archive 路径，避免并发构建互相锁库或污染产物。
    7. 从项目根使用 `.env.production`、workspace `ios/Circle.xcworkspace`、scheme `Circle`、configuration `Release`、generic iOS destination、automatic signing 和正确 Team 归档；禁用 Sentry 自动上传，保留符号上传警告供结果判断。推荐命令骨架：`ENVFILE=.env.production SENTRY_DISABLE_AUTO_UPLOAD=true xcodebuild -workspace ios/Circle.xcworkspace -scheme Circle -configuration Release -destination 'generic/platform=iOS' -derivedDataPath <unique-derived-data> -archivePath <unique-archive>.xcarchive CODE_SIGN_STYLE=Automatic DEVELOPMENT_TEAM=HS8K5BGDV7 -allowProvisioningUpdates archive`。
    8. Archive 成功后先独立核验归档内 App 的 `CFBundleIdentifier`、`CFBundleShortVersionString`、`CFBundleVersion`、`DTSDKName`、`DTXcode`、TeamIdentifier 和 `codesign --verify --deep --strict`；任一值不符时不得导出或上传。`CFBundleIdentifier` 必须是 `com.healshealthcare.circlemedical`，不得是 `.dev`，也不得是 Android 包名 `com.circleapp.cdv`。
    9. 使用 `method=app-store-connect`、automatic signing、正确 Team、`manageAppVersionAndBuildNumber=false` 的 ExportOptions 导出本地 IPA。再次解包核对 Bundle ID、version/build、SDK、Apple Distribution 证书、Store provisioning profile、`get-task-allow=false`、`beta-reports-active=true` 和深度签名，并记录 IPA 绝对路径、字节数和 SHA-256；不得用未经验证的旧 IPA 代替本次产物。
    10. 仅在 IPA 校验通过后，通过 Xcode/App Store Connect 正式上传到 Prod App `6748490218`。成功标准必须同时满足：上传工具明确返回 `Upload succeeded`，并且该 App 的 App Store Connect “构建版本上传”或目标 version 列表真实出现本次 version/build。等待 Apple 处理到可辨识的最终状态；若显示“缺少出口合规证明”，只报告并交回用户决定，不代替用户作合规声明。Agora/Hermes 等 dSYM 缺失警告与上传失败分开报告，不得把有警告的成功上传写成失败，也不得隐瞒其对原生崩溃符号化的影响。
    11. 上传或网络异常时，先判断 Apple 是否已收到该 version/build，再决定是否重试；Apple 已接收或正在处理时不得重复上传相同构建。网络超时按当前 Mac 的 VPN/代理规则排查；Apple 明确拒绝时保留错误原文和 request/response ID，修复根因后重新归档并使用未占用的 build number。
    12. 上传后通过当前登录态打开 `https://appstoreconnect.apple.com/teams/1f49f429-f33a-4c15-b357-7025b5e32451/apps/6748490218/testflight/ios` 的测试用户列表（禁止打开 Heals `6544800416`），实时核对是否包含如图![img_142626.png](img_142626.png)的内部测试员：邮箱 `cham2015@126.com`、名称彭燕、类型内部，且设备列含 iPad Air（第三代）。若测试员不在列表中，仅补齐该已有内部测试员并加入已有内部测试群组，使其能访问本次构建；不得邀请截图以外的新测试员，不得创建新 Apple ID。TestFlight 设备列在对方安装后才会刷新；不要求远程把新 IPA 装进该 iPad，也不要把其“已安装”仍显示旧 version/build 当成测试员缺失。若登录、权限或页面读取失败，明确报告阻塞和已完成项。
    13. 最终报告目标 App（含实时读到的 App Store Connect App ID）、version/build、Xcode/SDK、Archive 和 IPA 路径、IPA 大小/SHA-256、签名与 provisioning 校验、上传回执、App Store Connect 实际状态、测试用户核对结果（是否含彭燕 / `cham2015@126.com` / iPad Air（第三代））、dSYM/合规风险和未覆盖范围。除非用户明确要求，不提交或 push；完成项目产物和验证后，仅把新增或变化的通用工程/环境/发布事实更新到项目 `README_stark.md`（仓库根当前无此文件时不要新建，也不要写入 `README.md` 的账号段落），不写单次状态流水或秘密。 -->
- android:
  -  你执行`npm run android:dev`,把当前项目的`1.0.3`版本的 `dev `环境的debug模式的apk运行到如图 ![img_114112.png](img_114112.png)![img_114124.png](img_114124.png) 型号的真机上,直到你用 adb 截取真机当前画面(比如遇到LogBox黄条警告或者红条报错,直接解决),检查完毕真机上运行的 APP 没问题为止,否则不要自动停止任务; 真机所在的时区是 `东八区`
  <!-- - 为当前 checkout 构建 `dev` 环境的 `xxx` 版本 Release 模式 APK。使用前把 `xxx` 换成 `1.0.3`, 作为真实的 `versionName`，或在本轮消息里明确写出 version。本任务明确授权构建，但不授权自动安装到真机、提交 Git、push、上传 Google Play / 任何商店或发布。
    1. 先确认项目根、当前分支、HEAD 和工作树；保留已有未提交改动，不执行 clean/reset，不覆盖无关文件。读取 `package.json` 脚本、`android/app/build.gradle` 的 flavor / `applicationId` / `applicationIdSuffix` / `versionName` / `versionCode` / signingConfigs、以及 `.env.development` 是否存在，以源码和真实构建结果为准。
    2. 目标 `versionName` 优先使用用户本轮明确指定的 version；否则使用本条标题里已替换的 `xxx`；若标题仍是占位符 `xxx` 且本轮未指定，读取当前 `defaultConfig.versionName` 并保持不变，不擅自升级。目标必须是 `dev` flavor + `release` buildType（`assembleDevRelease`），最终包名必须为 `com.circleapp.cdv.dev`（`applicationId` `com.circleapp.cdv` + `applicationIdSuffix` `.dev`）；不得误改或误构建 `prod` / `debug`，也不得使用历史临时包名 `com.circleapp.cdvs`、iOS Bundle ID 或 Heals 包名。
    3. 目标 `versionCode`：用户本轮明确指定时用指定值；否则若 `versionName` 相对当前 gradle 有变化，则使用当前 `versionCode + 1` 的正整数；若 `versionName` 也不变，则保持当前 `versionCode`。不得只根据已安装 APK、截图日期或历史摘要猜测。
    4. 只更新本次 Dev Release 需要的 `versionName` / `versionCode`。这两项目前写在共用 `defaultConfig`，只改这两处，并在结果中说明 `prod` flavor 会读到同一组值，但本任务不得执行 `assembleProdRelease`，也不得改 prod flavor、iOS、`applicationId`、`applicationIdSuffix` 或 signing。不要把 keystore 路径以外的签名秘密（密码、alias、密钥内容）写入回复、Skill 或 README。
    5. 构建前确认本机 JDK、Android SDK / `ANDROID_HOME`、Gradle wrapper 可用；macOS 使用 `./gradlew`，Windows 使用 `gradlew.bat`。检查是否已有其它 Gradle 正在使用同一 `android/` 目录或 `build` 输出；只保留一个本次构建。
    6. 从项目根使用 `.env.development`、`dev` flavor、`release` buildType，并禁用 Sentry 自动上传。推荐命令骨架：`cd android && ENVFILE=.env.development SENTRY_DISABLE_AUTO_UPLOAD=true ./gradlew assembleDevRelease`。不要用 `npm run android:dev`（那是 `devDebug` 真机安装）。不要 `gradlew clean`，除非本次构建因缓存损坏失败且已说明原因。
    7. 构建成功后独立核验产物 `android/app/build/outputs/apk/dev/release/app-dev-release.apk`：包名必须为 `com.circleapp.cdv.dev`、`versionName`、`versionCode`、签名（`apksigner verify` 或等价命令）、文件绝对路径、字节数和 SHA-256。任一值不符时不得把旧 APK 当作本次产物。
    8. 最终报告目标包名、versionName / versionCode、Gradle 任务、APK 路径 / 大小 / SHA-256、签名校验、是否改了共用 `defaultConfig`、以及未覆盖范围（默认未安装、未上传）。除非用户明确要求，不安装、不提交、不 push；完成产物和验证后，仅把新增或变化的通用工程 / 环境 / 发布事实更新到项目 `README_stark.md`（仓库根当前无此文件时不要新建，也不要写入 `README.md` 的账号段落），不写单次状态流水或秘密。 -->
  <!-- - 为当前 checkout 构建 `prod` 环境的 `xxx` 版本 Release 模式 APK。使用前把 `xxx` 换成 `1.2.1.5`, 作为真实的 `versionName`，或在本轮消息里明确写出 version。本任务明确授权构建，但不授权自动安装到真机、提交 Git、push、上传 Google Play / 任何商店或发布。
    1. 先确认项目根、当前分支、HEAD 和工作树；保留已有未提交改动，不执行 clean/reset，不覆盖无关文件。读取 `package.json` 脚本、`android/app/build.gradle` 的 flavor / `applicationId` / `applicationIdSuffix` / `versionName` / `versionCode` / signingConfigs、以及 `.env.production` 是否存在，以源码和真实构建结果为准。
    2. 目标 `versionName` 优先使用用户本轮明确指定的 version；否则使用本条标题里已替换的 `xxx`；若标题仍是占位符 `xxx` 且本轮未指定，读取当前 `defaultConfig.versionName` 并保持不变，不擅自升级。目标必须是 `prod` flavor + `release` buildType（`assembleProdRelease`），最终包名必须为 `com.circleapp.cdv`（无 `.dev` suffix）；不得误改或误构建 `dev` / `debug`，也不得使用历史临时包名 `com.circleapp.cdvs`、iOS Bundle ID 或 Heals 包名。
    3. 目标 `versionCode`：用户本轮明确指定时用指定值；否则若 `versionName` 相对当前 gradle 有变化，则使用当前 `versionCode + 1` 的正整数；若 `versionName` 也不变，则保持当前 `versionCode`。不得只根据已安装 APK、截图日期或历史摘要猜测。若用户本轮要求对照 Play 商店，再通过当前登录态读取该 Prod App（包名 `com.circleapp.cdv`）已用 `versionCode`，选择未占用且严格递增的正整数；登录、权限或页面读取失败时停止在改 `versionCode` 前并报告阻塞。默认不打开 Play Console。
    4. 只更新本次 Prod Release 需要的 `versionName` / `versionCode`。这两项目前写在共用 `defaultConfig`，只改这两处，并在结果中说明 `dev` flavor 会读到同一组值，但本任务不得执行 `assembleDevRelease`，也不得改 dev flavor、iOS、`applicationId`、`applicationIdSuffix` 或 signing。不要把 keystore 路径以外的签名秘密（密码、alias、密钥内容）写入回复、Skill 或 README。
    5. 构建前确认本机 JDK、Android SDK / `ANDROID_HOME`、Gradle wrapper 可用；macOS 使用 `./gradlew`，Windows 使用 `gradlew.bat`。检查是否已有其它 Gradle 正在使用同一 `android/` 目录或 `build` 输出；只保留一个本次构建。
    6. 从项目根使用 `.env.production`、`prod` flavor、`release` buildType，并禁用 Sentry 自动上传。推荐命令骨架：`cd android && ENVFILE=.env.production SENTRY_DISABLE_AUTO_UPLOAD=true ./gradlew assembleProdRelease`。不要用 `npm run android:prod`（那是 `prodRelease` 真机安装）。不要 `gradlew clean`，除非本次构建因缓存损坏失败且已说明原因。
    7. 构建成功后独立核验产物 `android/app/build/outputs/apk/prod/release/app-prod-release.apk`：包名必须为 `com.circleapp.cdv`（不得带 `.dev`）、`versionName`、`versionCode`、签名（`apksigner verify` 或等价命令）、文件绝对路径、字节数和 SHA-256。任一值不符时不得把旧 APK 当作本次产物。
    8. 最终报告目标包名、versionName / versionCode、Gradle 任务、APK 路径 / 大小 / SHA-256、签名校验、是否改了共用 `defaultConfig`、以及未覆盖范围（默认未安装、未上传）。除非用户明确要求，不安装、不提交、不 push；完成产物和验证后，仅把新增或变化的通用工程 / 环境 / 发布事实更新到项目 `README_stark.md`（仓库根当前无此文件时不要新建，也不要写入 `README.md` 的账号段落），不写单次状态流水或秘密。 --> 
