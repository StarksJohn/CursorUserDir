---
name: ask-heals-app-rn
description: >-
  Cursor：Heals React Native 医疗应用（heals-app-rn）的项目入口。用于恢复项目路径、
  事实源、工程约束和最小下一步，并路由 RN、TypeScript、API、i18n、导航、Figma、
  原生构建、代码审查或 BMAD 工作流。用户消息含 /ask-heals-app-rn、提及 Heals App，
  当前工作区为 Windows D:\work\RN\heals-app-rn 或 macOS
  $HOME/Desktop/work/RN/heals-app-rn，或需要继续该项目任务时使用。
---

# ask-heals-app-rn（Cursor）

## 路径与事实源

- 项目根：Windows `D:\work\RN\heals-app-rn`；macOS `/Users/<你的用户名>/Desktop/work/RN/heals-app-rn`，当前 Mac 为 `/Users/stark/Desktop/work/RN/heals-app-rn`。
- Cursor 入口：Windows `%USERPROFILE%\.cursor\skills\ask-heals-app-rn\SKILL.md`；macOS `/Users/<你的用户名>/.cursor/skills/ask-heals-app-rn/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%\.codex\skills\heals-app-rn\SKILL.md`；macOS `/Users/<你的用户名>/.codex/skills/heals-app-rn/SKILL.md`。
- 业务逻辑、API 映射、导航、i18n、UI 行为和错误处理：以当前 `src/`、`ios/`、`android/` 和测试为准。
- 稳定项目事实与工程约束：以 `.cursor/rules/project-context.mdc` 和实际存在的项目规则为准。
- 技术栈、脚本、依赖、环境、构建和发布方式：以 `package.json`、项目配置和 `README*` 为准。
- 当前任务、外部状态和最小下一步：以用户本轮消息、受保护的“当前活跃需求”和实时证据为准，不在入口正文复制状态流水。
- `README_stark.md` 可能含敏感信息；只按任务读取相关段落，不复述或新增账号、密码、token、Cookie、私钥、keystore 密码和生产密钥。

发生冲突时，当前源码、Git、ADB/Xcode/Gradle/Metro、真实页面和外部系统实时结果优先于历史摘要；产品范围、医疗合规和外部 contract 以负责人最新确认优先。

## 与 Codex 入口对齐

- 两份入口分别维护，但事实源优先级、最小读取顺序、上下文门禁、授权边界、实施流程和输出约定保持一致。
- 在 Cursor 的 Codex 插件中输入 `/heals-app-rn`，应与 Cursor 输入框中执行 `/ask-heals-app-rn` 对同一明确任务达到相同推进效果。
- 两份“当前活跃需求”由用户分别维护，不自动同步或改写；用户本轮明确任务始终优先。

## 启用与最小读取顺序

1. 完整读取本 `SKILL.md`；已在当前 chat 实际加载且未变化的文件不重复读取。
2. 读取仓库实际存在的项目规则：`AGENTS.md`、`.cursor/rules/project-context.mdc` 及与任务直接相关的 `.cursor/rules/*`。
3. 读取任务直接相关的源码、测试和原生配置；需要脚本、依赖或环境事实时，再读取 `package.json`、`README.md`、`README_stark.md`、`CLAUDE.md` 中实际存在者。
4. 普通实现、排障和审查不默认读取 Codex 对照入口；仅在用户调用 `/heals-app-rn`、两份入口需要对齐，或任务事实只存在于对照入口时读取。
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
- 新增用户可见文案时同步项目当前约定的全部 locale；不从历史 Skill 猜测语言清单。
- 跨平台逻辑优先使用公共字段；第三方 API 标记 `iOS ONLY`、`ANDROID ONLY`、deprecated 或 experimental 时，先核对类型定义或官方文档，并显式处理另一平台。
- 医疗健康文案避免确诊式、保证疗效式或替代医生建议式表达。
- 非必要不新增依赖；不写入或输出 token、Cookie、密码、私钥、证书、keystore 密码、生产密钥和测试账号明文。

## 运行、发布与外部系统门禁

- Android 真机任务：先从 `package.json` 核对脚本和 flavor/env，再用 `adb devices -l` 锁定设备；只处理属于本项目且阻塞本次运行的旧进程。成功至少需要构建/安装/启动结果、目标包进程和前台 Activity 证据，不能只看端口或 Gradle 成功。
- iOS/TestFlight 任务：先核对 scheme、configuration、Bundle ID、Team、version/build、Xcode/SDK 和签名；上传、测试群组、出口合规和 App Store 发布分别授权。外部页面上的 build、tester、group 和处理状态必须实时复核。
- Git/release 任务：先检查远端 refs、完整拓扑、工作树、提交差异和最终树；“方向看起来安全”或只询问是否应合并，不等于授权 merge、删分支、push 或发布。
- 浏览器和外部代码平台任务：使用当前已授权的真实会话并验证完整数据，不把可见列表或编辑器 viewport 当作完整源码；外部 Web 项目与本地 React Native checkout 分开判断。

## 文档维护规则

- `.cursor/rules/project-context.mdc` 只保存稳定项目事实与长期工程约束；`README.md` 保存通用工程说明；`README_stark.md` 只保存无秘密、可复用且不能从源码直接恢复的环境、构建、发布和验证方法。
- 不把字段清单、业务规则、默认值、单次分支/commit/PID、构建结果、测试数量、当前阻塞或聊天流水写入入口 Skill 或 README。
- 有新的可复用事实时，先完成项目代码和测试，再更新现有对应章节；直接修正过期内容并去重，不按日期追加。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，否则保持其子内容原文。
- 最终回复默认只报告产出、验证、风险和必要下一步；仅在用户要求、审查/排障、上下文缺失或慢任务复盘时列出关键加载文件。

## 输出与边界

- 对用户使用简体中文；代码与代码注释使用英文；引用真实文件时给出路径和必要行号。
- 诚实区分已验证、部分验证、外部阻塞和未执行；不把构建成功写成真机功能验收完成。
- 不把医学建议写成确诊或处方替代，不混入其它项目假设，不创建无关文档或脚本。

## 当前活跃需求(不要修改这部分的子内容)
- WIN:
  <!-- - 当前电脑已经在 Windows 项目根 目录`D:\work\RN\heals-app-rn`执行了 `npm run android:dev:win` 把当前项目的debug模式的app运行到了如图![img_114112.png](img_114112.png)![img_114124.png](img_114124.png)型号的真机上,真机所在的时区是 `东八区` -->
  <!-- - 在 `D:\work\RN\heals-app-rn\src\screens\login\login-screen\login-screen.tsx`页面,一开始显示![img_185014.png](img_185014.png),点击`renderMobileNumber`函数绘制的输入框后, 键盘弹起, 如图 ![img_185100.png](img_185100.png), 输入框的下半部分内容被遮挡了, 测试用屏幕更小的机型也发现了更明显的这个问题![img_185145.png](img_185145.png),并且提了BUG: `Problem Statement -->
