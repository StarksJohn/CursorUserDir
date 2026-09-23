---
name: ask-csx-mobile-upgrade
description: >-
  CS Mobile 私有恢复与专项路由入口。仅在用户显式使用
  /ask-csx-mobile-upgrade 或 @ask-csx-mobile-upgrade，或明确要求继续受保护待办、
  恢复跨会话状态、处理外部构建发布阻塞时使用。每个新 chat 先调用本入口；随后
  强制读取 Codex 对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-csx-mobile-upgrade

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/csx-mobile-upgrade/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\csx-mobile-upgrade\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只处理私有恢复快照、受保护待办、专项工作流路由和外部构建/发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。
- 普通一次性任务优先在新 chat 第一条消息中同时写 `/ask-csx-mobile-upgrade` 和任务正文；只有需要跨 chat、跨设备或长周期恢复时，才把任务放入本文件受保护区后仅输入入口词继续。

## 入口、路径与事实源

- Cursor 入口：Windows `%USERPROFILE%\.cursor\skills\ask-csx-mobile-upgrade\SKILL.md`；macOS `~/.cursor/skills/ask-csx-mobile-upgrade/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\csx-mobile-upgrade\SKILL.md`；macOS `~/.codex/skills/csx-mobile-upgrade/SKILL.md`。两端保持同一执行语义，不要求逐字同步。
- 项目根：Windows `D:\work\RN\csx-mobile-upgrade`；macOS `/Users/<用户名>/Desktop/work/RN/csx-mobile`。若实际路径不同，以当前机器为准。
- 业务行为、API 映射、组件交互和错误处理以当前源码、测试和真实运行证据为准。
- 稳定工程约束只维护在 Codex 对口目录的 `AGENTS.md`；技术栈、脚本、依赖、构建和发布方式以 `package.json`、项目配置和 `README.md` 为准。不创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- 当前阶段、无法从源码恢复的外部阻塞和最小下一步以本 Skill 的「项目状态恢复快照」为准。

发生冲突时，优先采用当前仓库文件、真实设备、Network、构建产物和外部平台的实时证据，不用旧快照覆盖事实。

## 与 Codex 入口对齐

- 两份入口分别维护，但事实源优先级、最小读取顺序、上下文门禁、授权边界、实施流程和输出约定保持一致。
- 在 Cursor 的 Codex 插件中输入 `/csx-mobile-upgrade`，应与 Cursor 输入框中执行 `/ask-csx-mobile-upgrade` 对同一明确任务达到相同推进效果。
- 两份「当前活跃需求」由用户维护；除非用户明确授权，不改写其文字、注释状态、层级或图片引用。用户本轮明确任务始终优先。
- 不把 CircleApp、Heals、Amber 或 New Town 的 Bundle ID、包名、TestFlight、蒲公英或 Play 应用当成本项目目标。

## 新会话最小读取顺序

在实现、排障、审查、改配置或给出专项结论前，依次执行：

1. 完整读取本文件，包括未注释的「当前活跃需求」。
2. 确认 Codex 对口目录 `AGENTS.md` 已读取，再按任务读取 `{workspace}/README.md`、`{workspace}/package.json` 和相关配置；只提取与任务相关的规则、命令与依赖，不复述其中的敏感信息。
3. 读取任务直接相关的 1～3 个源码、配置或测试文件；范围不足时再扩大，不默认扫描整棵 `src/`。
4. 若入口、项目文档或当前任务路由到其它 Skill，先完整读取对应 `SKILL.md` 及其明确要求的 `workflow.md`、`checklist.md` 或 `reference.md`。
5. 若引用 `![image](image)`，先按引用该 Markdown 文件的同目录精确路径读取所有直接相关图片；精确路径失败后才搜索。

任一必读文件读取失败时，明确报告精确路径和降级范围，再决定继续或请求用户补充。

## 项目约束与默认切入位置

- 当前基线是 React Native、TypeScript strict、React Navigation、Redux Toolkit、Metro、SVG 和多语言；精确版本与可用脚本以仓库为准。
- 非华为设备推送使用 FCM；华为 / 鸿蒙设备使用 HMS Push。修改共享推送逻辑前核对双端字段和平台限制。
- 第三方原生库字段、方法或参数在实现前核对当前类型定义或官方平台说明；平台专属 API 必须显式分支并提供另一端处理。
- 医疗健康文案避免确诊式、替代医嘱式表述。
- 不写入或输出账号、密码、token、证书、私钥、签名材料和环境密钥。

| 主题           | 默认切入位置                                                                         |
| -------------- | ------------------------------------------------------------------------------------ |
| 导航           | `src/csxRoutes/`、`src/csxRoutes/csxRouter.ts`                                       |
| API / DTO      | `src/api/`、`src/tools/`                                                             |
| i18n           | `src/i18n/`、`src/i18n/locale/`                                                      |
| 推送           | `src/tools/pushManager.ts`、`src/tools/hmsPush.ts`、`src/firebase/`                  |
| 健康数据       | `src/pages/HealthDataPage/`、`src/pages/EditHealthDataPage/` 及相关 hooks / services |
| 通用 UI / 主题 | `src/components/`、`src/components/theme/`、`src/styles/`                            |
| 原生构建与发布 | `android/`、`ios/`、`global.ts`、项目脚本和原生配置                                  |

## 实施工作流

1. 确认仓库身份、目标平台、环境和交付物，区分本应用与关联系统。
2. 按最小读取顺序恢复上下文，并把请求归类为需求、实现、运行时缺陷、审查、i18n、Figma、构建 / 发布或架构任务。
3. 优先读取真实截图、设备状态、Network、构建设置和直接相关代码，再作判断。
4. 可由真实页面触发 API 时，先读取实际请求与响应；权限或流程阻塞后才退回 Swagger、OpenAPI 或源码，并明确证据边界。
5. 收到 Figma URL、节点或设计还原任务时，先用 Figma MCP 读取节点；未成功读取前暂停依赖设计事实的实现或验收。
6. 代码任务依次完成项目内业务实现、项目内定向测试，再更新项目外 Skill 或恢复文档。若验证要求再次改代码，先回到业务实现阶段。
7. 开发阶段优先运行单文件、单用例、单平台或单设备验证；阶段收尾时再按风险扩大范围。
8. 完成项目相关任务后，按「状态与文档维护规则」覆盖更新恢复快照和最小下一步。

## 专项 Skill 路由

按当前机器实际存在的目录选择并读取专项 Skill；不要只凭名称执行。

| 任务                             | 默认路由                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------- |
| 创建或刷新项目规则               | `init-project`                                                                  |
| RN Hooks、跨端、列表、键盘与图片 | `react-native-patterns`                                                         |
| DTO、API 边界和严格类型          | `typescript-strict`                                                             |
| 代码审查                         | `code-review`；需要 BMAD 对抗审查时用 `bmad-code-review`                        |
| 翻译、术语与多语言               | `chinese-english-translation`，并同步所有必需 locale                            |
| Figma 到 RN                      | `ask-figma-to-rn-toolkit`、`figma-implement-design`；写入画布时再用 `figma-use` |
| 已澄清规格的快速实现             | `bmad-quick-dev`                                                                |
| 已有 story 文件的开发            | `bmad-dev-story`                                                                |
| 模块边界与架构演进               | `architecture-review` 或 `bmad-agent-architect`                                 |

默认顺序是澄清事实、读取最小代码切片、选择专项流程、实施和验证。需求模糊时不要直接进入 `bmad-quick-dev`。

### BMAD 执行门禁

任务、文档、恢复快照或上轮结论明确指向任一 `bmad-*` 且本轮要按其步骤产出时，先读取当前系统下 `~/.cursor/skills/<bmad-identifier>/SKILL.md`（Windows 为 `%USERPROFILE%\.cursor\skills\<bmad-identifier>\SKILL.md`），再读取它要求的同目录附属文件。读取失败时停止该专项步骤并报告精确路径，不依据历史经验代替。

## 用户已有日志保护硬门禁

- 当前源码中的 `console.log`、`console.info`、`console.warn`、`console.error`、自定义 logger、debugger、trace 和诊断 Hook 均视为用户已有代码。除非用户在本轮明确要求删除、注释、降级、脱敏、替换或重构某一条具体日志，否则必须逐条保留；“解决警告或报错”、真机检查、日志清洁、安全/隐私诊断、lint 或测试失败都不构成修改日志的授权。
- 日志记录到 warning/error 时优先修复实际根因，不得通过删除、屏蔽、改写或降低日志级别制造“无错误”结果。若根因属于外部服务、账号、云配置、依赖或环境，只报告边界和必要下一步，保留原日志。
- 发现日志可能包含敏感数据、输出过多、影响性能或与现有测试冲突时，只收集最小必要证据且不在回复复述敏感值；报告精确文件/行、风险和可选方案并等待用户授权。不得自行修改源码或测试来消除该日志。
- 用户明确授权日志改动后，只修改点名范围；收尾时单独复核 `console.*`、logger、debugger、trace 和诊断 Hook 的 diff，并逐项报告实际变化及原因。

## 运行、发布与外部系统门禁

- 环境由 `global.ts` 的 `global.env` 决定：`poc` 对应用户口头的 dev，`prod` 是生产接口。本仓库没有 Android productFlavor，也没有第二套 iOS Bundle ID。禁止套用 CircleApp 的 `com.circleapp.cdv`、`com.healshealthcare.circlemedical`、CDV TestFlight 或蒲公英短链。
- Android 真机：用当前 `package.json` 的 `android` 脚本，不要调用不存在的 `android:dev`。先 `adb devices -l` 锁定设备，成功标准是安装、进程和前台 Activity，不能只看 Gradle 成功。包名是 `com.csx.mobile.app`，入口是 `com.csx.mobile.app.MainActivity`。
- Android 发布：Release APK 用 `assembleRelease`，AAB 用 `bundleRelease`。`versionName` 以 `android/app/build.gradle` 的 `defaultConfig` 为准，当前为 `1.1.8`；`npm_package_version` 仍是 `1.0.0`，且 `YT_MOBILE_VERSION` 没有写回 `versionName`，不得把 `1.0.0` 当成对外版本。签名密码不得写入回复、Skill 或 README。蒲公英只使用 README 已记录的应用 `https://www.pgyer.com/manager/dashboard/app/8f9c603763ea7f12e3c53fffb83692d3`。未经该条授权不上传 Play。
- iOS：workspace `ios/YouTrackMobile.xcworkspace`，归档 scheme `YouTrackMobile[Release]`，configuration `Release`，Bundle ID `asia.cs.mobile`，显示名 `CS Mobile`，Team `HS8K5BGDV7`。当前仓库 New Architecture 与 Hermes 为开启（`android/gradle.properties` 的 `newArchEnabled=true`，`Info.plist` 的 `RCTNewArchEnabled` 为 true，`Podfile` 的 `:hermes_enabled => true`）。不得把 CircleApp 的 New Arch / Hermes 关闭门禁套到本项目，也不得改这三项，除非用户本轮明确要求。
- Git / 发布：检查远端和差异不等于授权 merge、删分支、push 或上架。出口合规、测试员邀请和 App Store 发布分别授权。

## 状态与文档维护规则

- 本 Skill 只保存无法从源码快速恢复的当前阶段、外部阻塞、最近关键证据和最小下一步；不复制业务规则、API 字段、测试数量、完整日志或发布流水。
- 每次项目相关任务结束时，直接替换「项目状态恢复快照」中的过期事实，删除已完成下一步；不要按日期追加 chat 历史。
- 只有阶段、外部阻塞、关键产物或下一步发生实质变化时才更新快照。普通解释、未验证推测或可从代码恢复的改动不写入。
- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
- 运行、构建、依赖和部署事实写入 `README.md`；临时状态不写入这些文件。
- 「当前活跃需求（不要修改这部分的子内容）」由用户维护。除非用户明确授权，否则保持其子内容逐字不变；未注释条目是新会话应优先继续的方向。
- 更新 Cursor 本 Skill 后，只在确有必要时同步 Codex 对照入口；不得为追求逐字一致复制平台专属说明或冗长参考。

## 项目状态恢复快照

### 当前阶段

- 分支 `1.1.8-stark-dev`，HEAD `948fa457`。`global.env` 已是 `poc`，本轮没有改它。New Architecture 与 Hermes 仍为开启，本轮没有改这三项。
- TECH-9093（iPhone 14 Pro Max / iOS 18.7.8 打不开通知）的代码改动留在工作树，尚未装到真机验收。个人中心推送开关现在跟随系统通知授权，不再被 FCM token 或服务端注册失败拉回关闭；未决定权限会走系统授权，已拒绝才去设置。
- 当前未完成范围仍以本文件未注释的「当前活跃需求」为准。图 1 Debug IPA 已在列设备处停止，没有归档、没有安装。

### 外部阻塞与证据缺口

- 2026-09-22 没有正在连接的有线真机。唯一配对设备是彭燕的 iPad（iPad Air 3rd，iOS 18.7.8，UDID `00008020-000208CC2E23002E`），`devicectl` 的 `tunnelState` 为 disconnected，上次连接 2026-09-20，`xctrace` 把它列在 Devices Offline。模拟器和这台离线 iPad 都不是安装目标。
- TestFlight build 当前是否仍为 processing / valid 未在本轮核验；只有任务依赖该状态时才访问 App Store Connect 实时确认。

### 最小下一步

1. 用数据线把一台 iPhone 或 iPad 接到这台 Mac，并在 `xcrun xctrace list devices` 的在线 Devices 里出现后，再从「当前活跃需求」第一条 IOS Debug IPA 的设备确认继续。没有有线真机就不要归档。
2. 真机启动后看个人中心「推送通知设置」：系统已允许通知时开关应为开；未决定时点开关应弹出系统授权；已拒绝时才进入系统设置。
3. 用户只调用入口或只说“继续”时，只做第一条 IOS 任务，做完即停。

## 输出与边界

- 使用简体中文说明；代码和代码注释使用英文。
- 只报告已验证、部分验证和外部阻塞，不把端口、环境变量、编译成功或上传成功冒充真实页面 / 真机验收。
- 不擅自扩大到无关重构、其它 Heals 仓库、生产发布或用户未授权的外部变更。
- 除非用户明确要求运行、构建、发布或真机验证，否则默认提供可执行步骤并由用户手动验证。
- 项目相关任务结束时说明恢复快照是已更新还是无需更新，并给出当前阻塞和最近可执行动作。
- 最终回复默认只报告产出、验证、风险和必要下一步；不输出文件加载清单，除非用户本轮明确要求。

## 当前活跃需求(不要修改这部分的子内容)
- MAC
  - 这些条目都是可执行发布任务。用户本轮点名哪一条就只做哪一条；只调用入口或只说“继续”时，只做第一条 IOS 任务，做完即停。
  - IOS:
    - 为当前 checkout 构建 `xxx` 环境的 Debug IPA，并安装、启动到已经用数据线接在当前 Mac 上的那一台真机。使用前把 `xxx` 换成 `poc` 或 `prod`；用户口头的 dev 对应 `poc`，本轮没写环境时用 `poc`。`version` 沿用 YouTrackMobile target 当前的 `MARKETING_VERSION`（仓库里现在是 `1.1.8`），只有用户本轮另外给出版本才改。本任务授权构建这个 Debug IPA、装到这台已连接真机并启动。不授权提交 Git、push、上传 TestFlight、邀请测试员、回答出口合规或发布到 App Store。禁止使用 CircleApp / CDV / Heals 的 Apple ID（`6781207370`、`6748490218`、`6740129703`、`6544800416`）或 Bundle ID `com.healshealthcare.circlemedical`。模拟器、仅无线连接的设备和没有插线的设备都不是目标。
      1. 构建前核对 New Architecture 与 Hermes 仍与仓库一致：`android/gradle.properties` 为 `newArchEnabled=true`，`ios/YouTrackMobile/Info.plist` 的 `RCTNewArchEnabled` 为 true，`ios/Podfile` 的 `:hermes_enabled => true`。本仓库当前是开启状态。不得套用 CircleApp 的关闭门禁，未经用户本轮明确要求不得改这三项。
      2. 确认项目根、分支、HEAD 和工作树。保留已有未提交改动，不执行 clean/reset。读取 `ios/YouTrackMobile.xcworkspace`、scheme `YouTrackMobile`、`ios/YouTrackMobile.xcodeproj` 里 YouTrackMobile target 的 Debug configuration、`Info.plist`、`Podfile`、`android/gradle.properties`、`global.ts` 和 `ios/AppDelegate.swift`。
      3. 把 `global.ts` 的 `global.env` 设成已经替换好的环境。本仓库只有 `poc` 和 `prod`，没有 Dev scheme，也没有第二套 Bundle ID。目标是 scheme `YouTrackMobile` + configuration `Debug`，产物 `YouTrackMobile.app`，Bundle ID `asia.cs.mobile`，显示名 `CS Mobile`，Team `HS8K5BGDV7`，Debug 的 `CODE_SIGN_IDENTITY` 为 `Apple Development`，`CODE_SIGN_STYLE=Automatic`。不得使用 scheme `YouTrackMobile[Release]`，不得使用 configuration `Release`，不得使用测试 target 的 `org.reactjs.native.example.*`。
      4. `YouTrackMobile.xcscheme` 和 `YouTrackMobile[Release].xcscheme` 的 ArchiveAction 都写着 `Release`。归档命令必须自己带上 `-configuration Debug`，不能靠 scheme 的默认归档配置。不要为了这次安装去改 scheme 文件，也不要改 `MARKETING_VERSION` 或 `CURRENT_PROJECT_VERSION`，更不要为了真机去查 App Store Connect 已经用过的 build。
      5. 用 `xcrun devicectl list devices` 列设备，必要时再用 `xcrun xctrace list devices` 对照。只接受状态可用、连接类型是 wired / USB 的 iPhone 或 iPad。一台有线真机都没有就停止。多于一台有线真机时停下列出 UDID、名称和系统版本，等用户指定，不得猜。模拟器、unavailable、nearby、network 设备都排除。记下这一台的 UDID。
      6. 用 `xcodebuild -workspace ios/YouTrackMobile.xcworkspace -scheme YouTrackMobile -configuration Debug -destination 'generic/platform=iOS' -showBuildSettings` 核对 `CONFIGURATION=Debug`、`PRODUCT_BUNDLE_IDENTIFIER=asia.cs.mobile`、`MARKETING_VERSION`、`DEVELOPMENT_TEAM=HS8K5BGDV7`，以及 `CODE_SIGN_IDENTITY` 含 Apple Development。有一项对不上就停止，不要连带改 Release 或测试 target。
      7. 执行 `xcode-select -p`、`xcodebuild -version`、`xcrun --sdk iphoneos --show-sdk-version`。默认 Xcode 优先 `/Applications/Xcode.app/Contents/Developer`。已经有别的 `xcodebuild` 占着同一 DerivedData 或 Archive 时只留一个任务，本次用单独的 DerivedData 和 Archive 路径。
      8. 在项目根归档。推荐骨架：`xcodebuild -workspace ios/YouTrackMobile.xcworkspace -scheme YouTrackMobile -configuration Debug -destination 'generic/platform=iOS' -derivedDataPath <unique-derived-data> -archivePath <unique-archive>.xcarchive CODE_SIGN_STYLE=Automatic DEVELOPMENT_TEAM=HS8K5BGDV7 CODE_SIGN_IDENTITY='Apple Development' -allowProvisioningUpdates archive`。不要用 `npm run ios`，那不是这条任务要的 Debug IPA。不要改成 `-destination 'id=<UDID>'` 直接 build 来躲开 IPA；只有导出 IPA 失败并写明原因后，才允许降级安装刚编出来的 `.app`，而且最终报告要写明没有 IPA。
      9. Archive 成功后先证明这次归档是 Debug：看构建日志里的 `CONFIGURATION=Debug`，再核 `.xcarchive` 里的 `YouTrackMobile.app`。核对 `CFBundleIdentifier=asia.cs.mobile`、`CFBundleDisplayName=CS Mobile`、`CFBundleShortVersionString`、`RCTNewArchEnabled=true`、Team，以及 `codesign --verify --deep --strict`。`AppDelegate.swift` 在 `DEBUG` 下通过 `RCTBundleURLProvider` 加载 `index`，不把包内的 `main.jsbundle` 当作这次启动的 JS。身份有一项不符，就不得导出，也不得安装。
      10. 写一份临时 exportOptions.plist：`method=development`、`signingStyle=automatic`、`teamID=HS8K5BGDV7`、`compileBitcode=false`、`stripSwiftSymbols=false`。不得使用 `method=app-store-connect`、`ad-hoc` 或 `enterprise`。如果 Xcode 拒绝用 `development` 导出这份 Debug archive，再改用 `method=debugging` 导一次，并在结果里写明实际 method。导出后核对 IPA 的 Bundle ID、version、`Apple Development` 签名和 SHA-256。不得拿旧 IPA 或 Release IPA 去装。
      11. 在项目根另开 Metro：`npm start`。已经有一个 cwd 和端口都对得上、监听 8081 的 Metro 就复用，不要再起第二个。Debug IPA 不内置 Release 用的 `main.jsbundle`，真机起来后要向 Mac 拉 `index`。数据线只负责安装，不会自动把 8081 转到手机。手机和 Mac 要在同一个局域网；不在同一网络时，把开发菜单里的 bundler 设为 `ipconfig getifaddr en0` 得到的地址再加端口 `8081`。空的 `ios/.metro-host.local` 不是已经配好的打包机地址。
      12. 安装并启动：`xcrun devicectl device install app --device <UDID> <ipa>`，然后 `xcrun devicectl device process launch --device <UDID> asia.cs.mobile`。安装失败时先看开发描述文件是否包含这台 UDID，不要改 Bundle ID，也不要换 Team。启动后用 `xcrun devicectl device process list --device <UDID>` 确认 `asia.cs.mobile` 在跑，并用 `xcrun devicectl device screenshot --device <UDID> <png路径>` 留下当前画面；本机的 devicectl 没有 screenshot 子命令时，改用 Xcode 的 Devices 窗口截图，并在结果里说明。红屏 “Could not connect to development server” 表示手机还连不上 Metro，先把打包机地址修通再停。只把 IPA 装上去，不能写成应用已经跑起来。
      13. 最终报告写出：设备名称、UDID、iOS 版本、有线连接、`global.env`、scheme `YouTrackMobile`、configuration `Debug`、Bundle ID、显示名、version、Xcode/SDK、New Arch / Hermes 仍为开启、Archive 与 IPA 的路径、大小、SHA-256、实际 export method、Metro 是否在 8081、安装和启动回执、截图路径。不提交、不 push、不上传 TestFlight。`global.env` 的改动留在工作树里，并在结果里写明。
    - 为当前 checkout 构建 `poc`（对应用户口头的 dev）环境的 `xxx` 版本 Release IPA。使用前把 `xxx` 换成 `1.1.8`，作为真实的 `version`，并真实上传到套装 ID 为 `asia.cs.mobile`、显示名为 `CS Mobile` 的 TestFlight。上传前必须在当前登录态打开 App Store Connect，按套装 ID 定位本应用。禁止使用 CircleApp / CDV / Heals 的 Apple ID（`6781207370`、`6748490218`、`6740129703`、`6544800416`）或 Bundle ID `com.healshealthcare.circlemedical`。本任务授权构建和上传，不授权提交 Git、push、邀请测试员、回答出口合规或发布到 App Store。
      1. 归档前核对 New Architecture 与 Hermes 仍与仓库一致：`android/gradle.properties` 为 `newArchEnabled=true`，`ios/YouTrackMobile/Info.plist` 的 `RCTNewArchEnabled` 为 true，`ios/Podfile` 的 `:hermes_enabled => true`。本仓库当前是开启状态。不得套用 CircleApp 的关闭门禁，未经用户本轮明确要求不得改这三项。
      2. 确认项目根、分支、HEAD 和工作树。保留已有未提交改动，不执行 clean/reset。读取 `ios/YouTrackMobile.xcworkspace`、scheme `YouTrackMobile[Release]`、`ios/YouTrackMobile.xcodeproj` 的 YouTrackMobile target、`Info.plist`、`Podfile`、`android/gradle.properties` 和 `package.json`。
      3. 归档前把 `global.ts` 的 `global.env` 设为 `poc`。本仓库没有 Dev scheme，也没有第二套 Bundle ID。目标是 scheme `YouTrackMobile[Release]` + configuration `Release`，产物 `YouTrackMobile.app`，Bundle ID `asia.cs.mobile`，显示名 `CS Mobile`，Team `HS8K5BGDV7`。不得归档 scheme `YouTrackMobile` 的 Debug，也不得使用测试 target 的 `org.reactjs.native.example.*`。
      4. `version` 优先用用户本轮指定值；否则用已替换的 `1.1.8`。只改 YouTrackMobile target 的 Release configuration 的 `MARKETING_VERSION`。`CURRENT_PROJECT_VERSION` 必须大于 App Store Connect 上该 App 已占用的 build，且为纯十进制正整数。页面读不到、套装 ID 不是 `asia.cs.mobile` 或应用名不是 `CS Mobile` 时，停止在上传前。
      5. 用 `xcodebuild -workspace ios/YouTrackMobile.xcworkspace -scheme 'YouTrackMobile[Release]' -configuration Release -showBuildSettings` 核对 version、build、Bundle ID、Team。不要连带改 Debug 或测试 target。
      6. 归档前执行 `xcode-select -p`、`xcodebuild -version`、`xcrun --sdk iphoneos --show-sdk-version`。默认 Xcode 优先 `/Applications/Xcode.app/Contents/Developer`。已有其它 `xcodebuild` 占用同一 Archive 时只保留一个任务，并为本次 version/build 使用独立 DerivedData 和 Archive 路径。
      7. 从项目根归档。推荐骨架：`xcodebuild -workspace ios/YouTrackMobile.xcworkspace -scheme 'YouTrackMobile[Release]' -configuration Release -destination 'generic/platform=iOS' -derivedDataPath <unique-derived-data> -archivePath <unique-archive>.xcarchive CODE_SIGN_STYLE=Automatic DEVELOPMENT_TEAM=HS8K5BGDV7 -allowProvisioningUpdates archive`。不要用 `npm run ios`。
      8. Archive 成功后核验 `CFBundleIdentifier=asia.cs.mobile`、`CFBundleShortVersionString`、`CFBundleVersion`、`RCTNewArchEnabled=true`、Team 和 `codesign --verify --deep --strict`。任一不符不得导出或上传。
      9. 用 `method=app-store-connect`、automatic signing、Team `HS8K5BGDV7`、`manageAppVersionAndBuildNumber=false` 导出 IPA。再核 Bundle ID、version/build、签名和 SHA-256。不得拿旧 IPA 上传。
      10. 仅在校验通过后上传到已核对的 `asia.cs.mobile` App。成功必须同时有上传工具的 `Upload succeeded`，以及 App Store Connect 构建列表出现本次 version/build。出口合规提示只报告，不代答。Apple 已接收时不得用同一 build 重传。
      11. 最终报告 App、version/build、Xcode/SDK、`global.env=poc`、New Arch / Hermes 仍为开启、Archive 与 IPA 路径、大小、SHA-256、上传回执和未覆盖范围。不提交、不 push。`global.env` 的改动留在工作树并在结果里写明。
    - 为当前 checkout 构建 `prod` 环境的 `xxx` 版本 Release IPA。使用前把 `xxx` 换成 `1.1.8`，作为真实的 `version`，并真实上传到同一个套装 ID `asia.cs.mobile`、显示名 `CS Mobile` 的 TestFlight。本仓库 prod 与 poc 共用 Bundle ID，差别只在 `global.env`。禁止上传到 CircleApp / CDV / Heals，也不要把 CircleApp 截图里的测试员 `cham2015@126.com` / 彭燕 加进本应用。本任务授权构建和上传，不授权提交 Git、push、邀请测试员、回答出口合规或发布到 App Store。
      1. 归档前的 New Architecture / Hermes 核对与 poc 任务相同，必须仍为开启。不得为了“对齐 CircleApp”改成 false。
      2. 确认项目根、分支、HEAD 和工作树，保留未提交改动。读取与 poc 任务相同的工程文件。
      3. 归档前把 `global.ts` 的 `global.env` 设为 `prod`。scheme、configuration、Bundle ID、显示名、Team 与 poc 任务相同。
      4. `version` 规则与 poc 相同，默认 `1.1.8`。build 必须未被该 App 占用。套装 ID 或应用名不匹配时停止在上传前。
      5. 只更新 Release configuration 的 `MARKETING_VERSION` 和 `CURRENT_PROJECT_VERSION`，再用 `-showBuildSettings` 复核。
      6. Xcode/SDK 与并发归档约束与 poc 任务相同。
      7. 使用与 poc 相同的 `xcodebuild archive` 骨架，但本次 `global.env` 必须已经是 `prod`。
      8. Archive 与 IPA 的 Bundle ID 必须是 `asia.cs.mobile`，不得是 Android 包名 `com.csx.mobile.app`，也不得是 CircleApp Bundle ID。`RCTNewArchEnabled` 必须仍为 true。
      9. 导出、签名和 SHA-256 校验与 poc 任务相同。校验失败不得上传。
      10. 上传成功标准与 poc 相同，目标仍是已核对的 `CS Mobile` / `asia.cs.mobile`。不邀请新测试员，不代答出口合规。
      11. 最终报告必须写明 `global.env=prod`、version/build、产物路径和上传回执。不提交、不 push。
  - android:
    - 执行 `npm run android`，把当前项目 `1.1.8` 版本、`global.env=poc` 的 debug APK 装到已授权真机上。本仓库没有 `npm run android:dev`。用 `adb devices -l` 锁定设备，时区是东八区。遇到 LogBox 红条报错直接修，黄条警告不作为停止条件。用 adb 截取当前画面，确认真机上的应用能打开且环境正确后再停；否则不要自动结束任务。
    - 为当前 checkout 构建 `poc` 环境的 `xxx` 版本 Release APK。使用前把 `xxx` 换成 `1.1.8`，作为真实的 `versionName`，或在本轮消息里明确写出 version。本任务授权构建，并把签过名的 Release APK 上传到蒲公英应用 `https://www.pgyer.com/manager/dashboard/app/8f9c603763ea7f12e3c53fffb83692d3`，使该应用显示本次包为最新。不授权自动安装到真机、提交 Git、push、上传 Google Play，或上传到 CircleApp 的 `cdvhealth` / `cdvhealthdev` 及其 agKey。
      1. 确认项目根、分支、HEAD 和工作树，保留未提交改动。读取 `package.json`、`android/app/build.gradle` 的 `applicationId` / `versionName` / `versionCode` / signingConfigs，以及 `global.ts`。
      2. 没有 productFlavor。目标是 `assembleRelease`，包名必须是 `com.csx.mobile.app`。构建前把 `global.env` 设为 `poc`。不得执行 `bundleRelease`，不得使用 `com.circleapp.cdv` 或 iOS Bundle ID。
      3. `versionName` 默认 `1.1.8`。不要用 `package.json` 的 `1.0.0`，也不要依赖 `YT_MOBILE_VERSION`，它目前没有写回 `versionName`。`versionCode` 改为大于文件中当前值、且小于 `2100000000` 的正整数；用户未指定时用当前值 + 1。不要照搬 CircleApp 的秒级时间戳，除非用户本轮要求。
      4. 只改本次需要的 `versionName` / `versionCode`。不要改 `applicationId`、签名或 iOS。不要把 `gradle.properties` 里的签名密码或蒲公英 key 写入回复、Skill 或 README。
      5. 确认 JDK、`ANDROID_HOME` 和 `android/gradlew` 可用。同一 `android/` 目录只保留一个 Gradle。
      6. 推荐命令：`cd android && ./gradlew assembleRelease`。不要 `gradlew clean`，除非本次构建因缓存损坏失败且已说明原因。不要用 `npm run android`（那是 debug 真机安装）。
      7. 产物预期在 `android/app/build/outputs/apk/release/app-arm64-v8a-release.apk`（ABI split 只含 `arm64-v8a`）。核验包名 `com.csx.mobile.app`、`versionName`、`versionCode`、`apksigner verify --verbose --print-certs`（至少含 v2）、绝对路径、字节数和 SHA-256。不符不得上传。
      8. 上传前在已登录页面确认该蒲公英应用的包名是 `com.csx.mobile.app`。Chrome 上传不能直接读 `android/app/build/` 时，把已校验 APK 复制到系统临时目录，再核一次包名和版本后上传，结束后删除副本。刷新后台，最新一条的应用名、包名、Version 必须对得上本次 APK。最新包不是本次 APK 才算失败。处理中时等待，不重复上传同一文件。
      9. 默认不安装到设备，最终回复写明“未安装到设备”。只有用户本轮另外要求安装时，才 `adb install -r` 并启动 `com.csx.mobile.app/.MainActivity`。
      10. 报告包名、改前/改后 versionName / versionCode、`global.env=poc`、APK 路径 / 大小 / SHA-256、签名和蒲公英核对结果。不提交、不 push。
    - 为当前 checkout 构建 `prod` 环境的 `xxx` 版本 Release APK。使用前把 `xxx` 换成 `1.1.8`，作为真实的 `versionName`。包名仍是 `com.csx.mobile.app`，没有 `.dev` 后缀。本任务授权构建并上传到同一个蒲公英应用 `https://www.pgyer.com/manager/dashboard/app/8f9c603763ea7f12e3c53fffb83692d3`。不授权安装、提交 Git、push、上传 Google Play 或 CircleApp 蒲公英。
      1. 步骤与 poc Release APK 相同，但构建前 `global.env` 必须是 `prod`。
      2. `versionName` 默认 `1.1.8`，`versionCode` 仍按当前值 + 1，除非用户指定。
      3. 只改 `versionName` / `versionCode` 和 `global.env`。不要改包名或签名。
      4. 命令仍是 `cd android && ./gradlew assembleRelease`。产物路径、包名校验、签名校验与 poc 任务相同。
      5. 上传目标仍是上述蒲公英应用。更新说明里写明本次是 `prod`。禁止传到 `cdvhealth` / `cdvhealthdev`。
      6. 默认不安装。最终报告写明 `global.env=prod`、version、产物和蒲公英最新包是否就是本次 APK。
    - 为当前 checkout 构建 `prod` 环境的 `xxx` 版本 Release AAB。使用前把 `xxx` 换成 `1.1.8`，作为真实的 `versionName`。本任务只授权构建签过名的 AAB。不要先复制 env 文件；直接执行 `bundleRelease`。不授权安装、提交 Git、push、上传蒲公英或 Google Play，也不把本包当成已提审。
      1. 确认项目根和工作树。读取 `android/app/build.gradle`、`android/gradle.properties` 的 `android.bundle.pageAlignment` 与 `newArchEnabled`，以及 `16_KB_memory_page_sizes/16KB_PAGE_SIZE_SOLUTION_GUIDE.md`。
      2. 目标是 `bundleRelease`，包名 `com.csx.mobile.app`。`global.env` 设为 `prod`。不得执行 `assembleRelease` 或任何带 flavor 的任务。
      3. `versionName` 默认 `1.1.8`。`versionCode` 大于当前值；用户未指定时 + 1。不为了取值去查 Play，除非用户本轮要求对照。
      4. 只改 `versionName` / `versionCode` 和 `global.env`。不要把签名密码写入回复。
      5. 确认 `android.bundle.pageAlignment=16384`，以及 `packagingOptions.jniLibs.useLegacyPackaging = false`。同一 `android/` 只保留一个 Gradle。
      6. 推荐命令：`cd android && ./gradlew bundleRelease`。不要 `gradlew clean`，除非缓存损坏且已说明原因。
      7. 产物预期在 `android/app/build/outputs/bundle/release/app-release.aab`。核验包名、`versionName`、`versionCode`、签名、路径、字节数和 SHA-256。优先用 `bundletool dump manifest`；没有 bundletool 时用等价命令，不得只看文件名。
      8. 按 `16_KB_memory_page_sizes/16KB_PAGE_SIZE_SOLUTION_GUIDE.md` 做本地 16KB 检查，至少覆盖 `lib/arm64-v8a/*.so`。未对齐则不得把该 AAB 当成可提审产物。本任务不上传 Play，也不上传蒲公英。
      9. 不安装 AAB。最终回复写明“未安装到设备”和“未上传”。
      10. 报告包名、version、`bundleRelease`、AAB 路径 / 大小 / SHA-256、签名、16KB 结果和 `global.env=prod`。不提交、不 push、不提审。

<!-- - figma-to-rn-toolkit 相关:
  - 请根据 `https://www.figma.com/design/Wa0Oa4oeMTy5H2Tk32ooqb/CSM?node-id=17126-28544&m=dev` 这个 Figma URL, 在 Windows `D:\work\RN\csx-mobile-upgrade\src\pages\Diagnosis\DiagnosisPage.tsx` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/src/pages/Diagnosis/DiagnosisPage.tsx` 页面 的 2018行 ,根据页面的代码风格和项目结构,设计实现 `React Native` 组件代码
    - 要求：
      - 匹配当前项目的代码风格（命名规范、目录组织、import 顺序等）
      - 复用项目中已有的公共组件和工具函数
      - 使用项目一致的样式方案（StyleSheet.create / styled-components 等） -->

<!-- - react-native-auto-positioned-popup 相关
  - Windows `D:\work\RN\csx-mobile-upgrade\global.ts` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/global.ts` 的 `global.$fake`已经设为了 true
  - Windows `D:\work\RN\csx-mobile-upgrade\src\pages\ImmuneRecordPage\ImmuneRecordPage.tsx` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/src/pages/ImmuneRecordPage/ImmuneRecordPage.tsx` 里绘制的![img_141828.png](img_141828.png)组件,显示在![img_142426.png](img_142426.png)的红框处,传入的 `useTextInput`是false, 实际调用的源码是 Windows `D:\work\RN\csx-mobile-upgrade\node_modules\react-native-auto-positioned-popup\src\AutoPositionedPopup.tsx` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/node_modules/react-native-auto-positioned-popup/src/AutoPositionedPopup.tsx`;
  - 目前点击 Windows `D:\work\RN\csx-mobile-upgrade\node_modules\react-native-auto-positioned-popup\src\AutoPositionedPopup.tsx` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/node_modules/react-native-auto-positioned-popup/src/AutoPositionedPopup.tsx` 里 1215行的`TouchableOpacity`后,执行了1219行的`onPress`回调;然后`state.isFocus`变成了true;然后`AutoPositionedPopupList`组件显示在了![img_144138.png](img_144138.png)红框处,也就是显示在了屏幕的中心;
  - 现在需要你在不改变原有代码逻辑的基础上修改这个逻辑,如果传入的 `internalSearch=true`,则点击后弹出的红框,也就是`AutoPositionedPopupList`组件,固定显示在如图![img_144313.png](img_144313.png)红框处(屏幕顶部导航栏)的下边;
  - 你只能新增代码,不要修改已有代码
  - 现在需要给 Windows `D:\work\RN\csx-mobile-upgrade\node_modules\react-native-auto-positioned-popup\src\AutoPositionedPopup.tsx` / Mac `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/node_modules/react-native-auto-positioned-popup/src/AutoPositionedPopup.tsx` 的887行的height的值加一个高度,这个高度用来显示如果原来useTextInput传入true时,显示的`memoizedTextInput`的高度;然后`AutoPositionedPopupList`的顶部需要显示`memoizedTextInput`,也就是把之前useTextInput传入true时显示的`memoizedTextInput`的操作逻辑,改到显示在`AutoPositionedPopupList`的顶部来操作 -->
