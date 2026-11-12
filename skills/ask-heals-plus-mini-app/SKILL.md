---
name: ask-heals-plus-mini-app
description: >-
  Heals 患者微信小程序私有恢复与专项路由入口。仅在用户显式使用
  /ask-heals-plus-mini-app 或 @ask-heals-plus-mini-app，或明确要求继续受保护待办、
  恢复跨会话状态时使用。每个新 chat 先调用本入口；随后强制读取 Codex 对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
  不用于 ask-heals-app-rn。
---

# ask-heals-plus-mini-app（Cursor）

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/heals-plus-mini-app/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\heals-plus-mini-app\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只处理私有恢复状态、受保护待办、专项路由和外部构建/发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。

## 路径与事实源

- 项目根：macOS `/Users/stark/Desktop/work/Heals Plus Mini App`。Windows 路径尚未登记，不得猜测。远程仓库 `healshealthcare/patient-wechat-mini-app`。
- Cursor 入口：Windows `%USERPROFILE%\.cursor\skills\ask-heals-plus-mini-app\SKILL.md`；macOS `/Users/<你的用户名>/.cursor/skills/ask-heals-plus-mini-app/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\heals-plus-mini-app\SKILL.md`；macOS `/Users/<你的用户名>/.codex/skills/heals-plus-mini-app/SKILL.md`。
- 页面、组件、接口、文案和条件编译：以当前 `pages/`、`packageB/`、`components/`、`apis/`、`locale/`、`utils/` 为准。
- 稳定工程约束只维护在 Codex 对口目录的 `AGENTS.md`；不创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- 技术栈、路由、平台和语言：以 `manifest.json`、`pages.json`、`main.js`、`utils/lang.js` 为准。`package.json` 只有依赖、没有 scripts，不得据此发明 npm 构建或测试命令。
- 当前任务、外部状态和最小下一步：以用户本轮消息、受保护的“当前活跃需求”和实时证据为准，不在入口正文复制状态流水。
- `README.md` 含微信密钥和测试账号。只按任务读取相关段落，不复述或新增 AppSecret、client secret、token、密码和测试账号明文。

发生冲突时，当前源码、Git、HBuilderX 编译结果和微信开发者工具真实预览优先于历史摘要；产品范围、医疗合规和外部 contract 以负责人最新确认优先。本仓库不是 `heals-app-rn`。

## 与 Codex 入口对齐

- 两份入口分别维护，但事实源优先级、最小读取顺序、上下文门禁、授权边界、实施流程和输出约定保持一致。
- 在 Cursor 的 Codex 插件中输入 `/heals-plus-mini-app`，应与 Cursor 输入框中执行 `/ask-heals-plus-mini-app` 对同一明确任务达到相同推进效果。
- 两份“当前活跃需求”由用户分别维护，不自动同步或改写；用户本轮明确任务始终优先。

## 启用与最小读取顺序

1. 完整读取本 `SKILL.md`；已在当前 chat 实际加载且未变化的文件不重复读取。
2. 确认 Codex 对口 Skill 同目录 `AGENTS.md` 已读取，再按任务读取相关 `.cursor/rules/*`；不要读取或创建 `project-context.mdc`。
3. 读取任务直接相关的页面、组件、接口和文案；需要平台、路由或语言事实时，再读取 `manifest.json`、`pages.json`、`main.js`、`utils/lang.js` 和 `README.md` 中实际存在者。
4. 普通实现、排障和审查不默认读取 Codex 对照入口；仅在用户调用 `/heals-plus-mini-app`、两份入口需要对齐，或任务事实只存在于对照入口时读取。
5. 用户只有入口口令而没有新任务时，执行本文件“当前活跃需求”中第一个未注释且可行动的事项；已有明确新任务时，不自动展开无关活跃项。
6. 路由到其它 Skill、ask、command 或 `bmad-*` 前，先完整读取对应 `SKILL.md` 及其明确要求的 `workflow.md`、`checklist.md`、`reference.md`。
7. 当前任务涉及 Markdown 图片引用时，先按引用文件同目录精确读取全部相关图片；读取失败后再搜索，不得用文字摘要代替图片事实。

不要默认通读仓库、全部 README 或另一客户端入口，也不要把历史摘要当成已加载的当前事实。

## 实施工作流

1. 确认实际工作区、Git 分支、工作树和任务授权边界；保留用户已有改动，不扩大到无关重构、提交、push、上传微信平台或外部系统写操作。
2. 按实现、排障、API、i18n、页面路由、分包、微信开发者工具预览、审查或设计还原分类，只读取能决定下一步的高价值文件。
3. 代码任务依次完成真实业务实现、同项目内可做的验证；确认无需继续改代码后，再更新项目文档或项目外入口资料。
4. API contract 可由真实请求观察到时，先读取实际请求与响应；受登录、权限或域名白名单阻塞后，再查 `apis/` 源码。
5. Figma URL、节点或设计还原任务必须先通过 Figma MCP 读取节点事实；截图只能作为补充验证，并映射到现有 Vue 组件和样式。
6. 开发阶段优先单页面、单流程验证。未运行的 HBuilderX 编译、微信开发者工具预览或上传必须明确说明。
7. 不因普通代码改动更新本 Skill；只有入口、事实源、跨客户端对齐、长期门禁或受保护活跃需求由用户授权变更时才更新。

## 项目工程约束

- uni-app、Vue 3、`mp-weixin`、路由和语言的精确值以当前仓库和共享 `AGENTS.md` 为准。
- 请求复用 `apis/base.js` 与 `apis/index.js`。新页面先登记到 `pages.json`：主包在 `pages/`，分包根是 `packageB`。
- `main.js` 全局注册 `h-custom-nav`、`h-tabbar`、`h-empty`。能复用 `components/` 或 `uni_modules/` 时不新增依赖。
- 新增用户可见文案必须写入 `locale/en.json`、`locale/zh-Hans.json`、`locale/zh-Hant.json`。`utils/lang.js` 加载这三份，存储键为 `Accept_Language`，默认 `zh-Hans`。`manifest.json` 的 `locale` 与 `fallbackLocale` 均为 `zh-Hans`。不要套用 `heals-app-rn` 的语言清单或英文兜底规则。
- 微信专用逻辑使用现有条件编译。`manifest.json` 里其它小程序块不是当前产品目标。
- 医疗健康文案避免确诊式、保证疗效式或替代医生建议式表达。
- 非必要不新增依赖；不写入或输出 AppSecret、client secret、token、密码、私钥和生产密钥。

## 用户已有日志保护硬门禁

- 当前源码中的 `console.log`、`console.info`、`console.warn`、`console.error`、自定义 logger、debugger、trace 和诊断 Hook 均视为用户已有代码。除非用户在本轮明确要求删除、注释、降级、脱敏、替换或重构某一条具体日志，否则必须逐条保留；“解决警告或报错”、预览检查、日志清洁、安全/隐私诊断、lint 或测试失败都不构成修改日志的授权。
- 日志记录到 warning/error 时优先修复实际根因，不得通过删除、屏蔽、改写或降低日志级别制造“无错误”结果。若根因属于外部服务、账号、微信配置、依赖或环境，只报告边界和必要下一步，保留原日志。
- 发现日志可能包含敏感数据、输出过多、影响性能或与现有测试冲突时，只收集最小必要证据且不在回复复述敏感值；报告精确文件/行、风险和可选方案并等待用户授权。不得自行修改源码或测试来消除该日志，也不得以历史改动、记忆、测试断言、lint、code review 或前一代理行为推定授权。
- 用户明确授权日志改动后，只修改点名范围；收尾时单独复核 `console.*`、logger、debugger、trace 和诊断 Hook 的 diff，并逐项报告实际变化及原因。

## 运行、发布与外部系统门禁

- 微信小程序任务先确认目标是 `mp-weixin`。本地阅读源码、HBuilderX 编译、微信开发者工具预览、上传和正式发布是分开的证据，不能互相替代。
- 上传微信平台、修改 AppID、服务器域名或隐私权限必须单独授权。未授权时不上传、不改平台配置。
- Git/release 任务：先检查远端 refs、完整拓扑、工作树、提交差异和最终树；“方向看起来安全”或只询问是否应合并，不等于授权 merge、删分支、push 或发布。
- 不把 `heals-app-rn` 的 Metro、Gradle、Xcode、TestFlight 或 Android 真机流程用到本仓库。

## 文档维护规则

- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
- `README.md` 可能含密钥。不把密钥、测试账号、字段清单、单次分支/commit、构建结果或聊天流水写入入口 Skill 或 README。
- 本仓库目前没有 `README_stark.md`。不要为单次任务新建它。
- 有新的可复用事实时，先完成项目代码和验证，再更新现有对应章节；直接修正过期内容并去重，不按日期追加。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，否则保持其子内容原文。
- 最终回复默认只报告产出、验证、风险和必要下一步；仅在用户要求、审查/排障、上下文缺失或慢任务复盘时列出关键加载文件。

## 输出与边界

- 对用户使用简体中文；代码与代码注释使用英文；引用真实文件时给出路径和必要行号。
- 诚实区分已验证、部分验证、外部阻塞和未执行；不把源码阅读写成微信开发者工具预览通过，也不把预览写成已发布。
- 不把医学建议写成确诊或处方替代，不混入其它项目假设，不创建无关文档或脚本。

## 当前活跃需求(不要修改这部分的子内容)

- 把当前项目的 dev 环境 debug 包运行到当前 adb 已连接的 Android 真机上，直到手机微信前台打开的是这个小程序，并且之后只改页面、组件、文案或接口代码时，真机能通过自动预览更新。验收通过前不要自动停止。同一阻塞连续 3 次没有进展就停止并报告。真机时区按东八区核对。本任务只走 HBuilderX 的微信小程序 dev 编译和微信开发者工具自动预览。禁止执行 `npm run android:dev`、Gradle、Metro、`adb reverse tcp:8081`，禁止使用 `heals-app-rn` 的包名，禁止 `cli upload` 和发行上传。
  1. 锁定设备：`adb devices -l` 只接受状态为 `device` 的一台手机。没有手机就停止。多于一台时列出序列号和 model 后停止，不要猜。后续 adb 命令都带 `-s <serial>`。用 `adb shell getprop persist.sys.timezone` 核对是否为 `Asia/Shanghai`。不一致只写入报告，不因此重装微信。
  2. 定位工具：当场查找 HBuilderX 和微信开发者工具。macOS 命令行是 `<安装路径>/Contents/MacOS/cli`，Windows 是 `<安装路径>/cli.bat`。先执行 `cli -h`，没有 `auto-preview` 就停止。本仓库 `package.json` 没有小程序脚本，禁止新建 npm 脚本代替 HBuilderX。找不到这两个应用就停止并报告查找范围，不要擅自安装。
  3. 切到 dev 接口：读取 `apis/index.js`。生效值如果是注释里标成 prod 的域名，把 `origin`、`hpOrigin`、`passportOrigin` 改成同一文件注释里标成 dev 的地址，并把请求头里的 `x-client-secret` 改成注释里标成 dev 的值。prod 值留在注释里。已经是 dev 注释值就不要再改。secret、测试账号和 AppSecret 不得写入 Skill、提交说明或回复。只改这些赋值，保留工作区里已有的其它改动。不要提交，不要 push。
  4. 编译 debug 产物：用 HBuilderX「运行到小程序模拟器 -> 微信开发者工具」编译。产物目录必须是项目根下的 `unpackage/dist/dev/mp-weixin`。禁止改用 `unpackage/dist/build/mp-weixin`。微信开发者工具打开这个 dev 目录；该目录的 `project.config.json` 必须含有 appid 和 projectname。AppID 以当前 `manifest.json` 的 `mp-weixin.appid` 为准。HBuilderX 已经打开该目录时，不要再开第二个项目。
  5. 选择快路径或重新打开：开发者工具已经打开上述 dev 目录、HBuilderX 运行会话还在，并且这次只改了 `pages/`、`packageB/`、`components/`、`locale/`、`utils/`、`apis/`、`styles/` 时，走快路径。快路径不关闭微信、不重装微信、不重新导入项目。等 dev 产物新于上次预览后，直接做第 7 步。`manifest.json`、`pages.json`、新增静态资源，或开发者工具没有打开 dev 目录时，重新编译并执行 `cli open --project "<dev 产物绝对路径>"`。项目路径含空格，必须加引号。
  6. 准备手机微信：`adb shell monkey -p com.tencent.mm -c android.intent.category.LAUNCHER 1` 把微信拉到前台。自动预览要求手机微信与开发者工具是同一个登录账号，并且手机在线。adb 只负责锁定设备、拉起微信和截图，不负责传输小程序代码。`cli islogin` 未登录时执行 `cli login`，把二维码交给用户扫。扫码完成前不要反复重试。
  7. 推到真机：开发者工具「设置 -> 安全设置」必须已开启服务端口。未开启时停止并说明这个设置，不要猜端口做 `adb reverse`。使用自动预览：`cli auto-preview --project "<dev 产物绝对路径>" --auto-preview-type mobile`。退出码 0 才算推送成功。同一错误连续 3 次没有进展就停止并保留命令原文。
  8. 代码更新后的刷新：保存源码后，HBuilderX 会更新 `unpackage/dist/dev/mp-weixin`。产物变新就再执行一次第 7 步。这是本项目最接近 RN debug 包保存后自动更新的官方路径。微信文档中的代码热重载只更新开发者工具模拟器，不能把它当成手机已经热重载。真机调试会另外上传一份调试包并提供断点，保存代码不会自动更新那次会话。用户本轮没有另行要求断点时，不要启动真机调试。
  9. 验收：`adb exec-out screencap -p` 必须显示微信前台已经打开本小程序，而不是只停在微信聊天列表。`cli auto-preview` 退出码为 0。HBuilderX 和控制台没有阻塞运行的红色报错。最终报告写明序列号、时区核对结果、走的是快路径还是重新打开、dev 产物路径、`apis/index.js` 哪些常量处于 dev、自动预览结果，以及没有上传、没有提交。域名白名单或登录账号不一致时停止并说明，不要改微信公众平台配置。

<!-- - 改动后刷新真机UI: 页面、组件、文案或接口代码已经改动并保存后，把最新 dev 产物再自动预览到当前 adb 已连接的 Android 真机，让手机微信前台打开的小程序显示最新 UI。验收通过前不要自动停止。同一阻塞连续 3 次没有进展就停止并报告。本条不重装 HBuilderX 或微信开发者工具，不切换 `apis/index.js` 的环境，不重新导入项目，不启动真机调试，不提交，不 push。禁止执行 `npm run android:dev`、Gradle、Metro、`adb reverse tcp:8081`，禁止使用 `heals-app-rn` 的包名，禁止 `cli upload` 和发行上传，禁止改用 `unpackage/dist/build/mp-weixin`。
  1. 锁定设备：`adb devices -l` 只接受状态为 `device` 的一台手机。没有手机就停止。多于一台时列出序列号和 model 后停止，不要猜。后续 adb 命令都带 `-s <serial>`。用 `adb shell getprop persist.sys.timezone` 核对是否为 `Asia/Shanghai`。不一致只写入报告，不因此重装微信。
  2. 确认产物：dev 产物目录必须是项目根下的 `unpackage/dist/dev/mp-weixin`，且其中 `project.config.json` 含有 appid 和 projectname。AppID 以当前 `manifest.json` 的 `mp-weixin.appid` 为准。HBuilderX 运行会话还在、微信开发者工具已经打开该 dev 目录，并且这次只改了 `pages/`、`packageB/`、`components/`、`locale/`、`utils/`、`apis/`、`styles/` 时，走快路径。快路径不关闭微信、不重装微信、不重新导入项目。等该目录新于上次自动预览后再推送。运行会话不在、开发者工具没有打开该 dev 目录，或改动涉及 `manifest.json`、`pages.json`、新增静态资源时，用 HBuilderX「运行到小程序模拟器 -> 微信开发者工具」重新编译，并执行 `cli open --project "<dev 产物绝对路径>"`。项目路径含空格，必须加引号。该 dev 目录已经打开时，不要再开第二个项目。
  3. 准备手机微信：`adb shell monkey -p com.tencent.mm -c android.intent.category.LAUNCHER 1` 把微信拉到前台。自动预览要求手机微信与开发者工具是同一个登录账号，并且手机在线。`cli islogin` 未登录时执行 `cli login`，把二维码交给用户扫。扫码完成前不要反复重试。开发者工具「设置 -> 安全设置」的服务端口未开启时停止并说明这个设置，不要猜端口做 `adb reverse`。
  4. 推到真机：执行 `cli auto-preview --project "<dev 产物绝对路径>" --auto-preview-type mobile`。退出码 0 才算推送成功。同一错误连续 3 次没有进展就停止并保留命令原文。微信开发者工具的代码热重载只更新模拟器。真机要看到最新 UI，必须等这次自动预览成功。用户本轮没有另行要求断点时，不要启动真机调试。
  5. 验收：`adb exec-out screencap -p` 必须显示微信前台已经打开本小程序的最新界面，而不是只停在微信聊天列表或仍停留在改动前的旧界面。`cli auto-preview` 退出码为 0。HBuilderX 和控制台没有阻塞运行的红色报错。最终报告写明序列号、时区核对结果、走的是快路径还是重新打开、dev 产物路径、自动预览结果，以及没有上传、没有提交。域名白名单或登录账号不一致时停止并说明，不要改微信公众平台配置。 -->

