---
name: ask-csx-web-react
description: >-
  Cursor：csx-web-react 独立 Next.js / React 前端项目入口；name 为
  ask-csx-web-react，口令 /ask-csx-web-react。用于恢复当前项目上下文、收敛
  TECH-8370 / TECH-8458 显示屏配置与公开大屏任务、核对 API / static export /
  Bitbucket 部署规则，并路由 React、TypeScript、Figma、代码审查、BMAD 等专项
  skills。Use when the user works on csx-web-react, invokes
  /ask-csx-web-react, or the workspace is macOS
  /Users/<你的用户名>/Desktop/work/csx-web-react.
---

# ask-csx-web-react（Cursor）

## 与 Codex 入口（对照）

| 客户端           | `SKILL.md`                                                                                                                                      | `name`              | 口令                 |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| Cursor（本文件） | **macOS** `/Users/<你的用户名>/.cursor/skills/ask-csx-web-react/SKILL.md`（当前 Mac：`/Users/stark/.cursor/skills/ask-csx-web-react/SKILL.md`） | `ask-csx-web-react` | `/ask-csx-web-react` |
| Codex（对照）    | **macOS** `/Users/<你的用户名>/.codex/skills/csx-web-react/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/csx-web-react/SKILL.md`）           | `csx-web-react`     | `/csx-web-react`     |

两侧不要求逐句同步，但工作区、项目事实、TECH 文档门禁、API / 部署规则、当前状态快照和输出约定应保持一致。若 Codex 侧 skill 更新了长期项目事实，应同步检查本 Cursor 入口是否需要收敛。

## 目的

本 skill 是 **`csx-web-react`** 的 Cursor 侧项目入口，用于在新会话或跨工具切换时，把任务拉回到项目事实与最小必要上下文上。

- **恢复项目事实**：先读项目规则、依赖、Next 配置和直接相关源码，避免只凭历史记忆行动。
- **收敛任务范围**：区分「显示屏配置后台 / TECH-8458 公开大屏 / API / 鉴权 / 部署 / Figma / 审查 / 排障」。
- **路由专项能力**：将 React、TypeScript、Figma、代码审查、架构、BMAD、Cursor / MCP 等任务指向对应 skills。
- **维护状态快照**：项目相关任务结束前更新本文件的「项目状态恢复快照」和「下一步任务列表」。
- **保护事实源边界**：README 只维护工程规则；TECH 私有技术文档只在门禁满足时维护需求、API、部署和验收事实。

**非目标**：不在本文件保存 token、Cookie、私钥、证书、部署凭证、逐 chat 流水、完整截图记录或可由 README / 私有技术文档恢复的大段内容。

## 何时使用

- 用户显式 `@ask-csx-web-react`、`/ask-csx-web-react` 或自然语言提及本 skill 名。
- 用户提到 `csx-web-react`、display screen config、显示屏配置、公开大屏、TECH-8370、TECH-8458、`/display-screen-config/`、old `csx` artifact、`csx-k8` deploy 等本仓相关任务。
- 当前工作区根目录为 `/Users/<你的用户名>/Desktop/work/csx-web-react`（当前 Mac：`/Users/stark/Desktop/work/csx-web-react`），且需要项目级引导。
- 用户未指定文件，但明显在本仓库内请求实现、排障、审查、部署或 Figma 对齐。

## 工作区与路径

| 用途                               | macOS 路径                                                                                              |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 工作区根（默认）                   | `/Users/<你的用户名>/Desktop/work/csx-web-react`（当前 Mac：`/Users/stark/Desktop/work/csx-web-react`） |
| 旧 Vue 项目                        | `/Users/<你的用户名>/Desktop/work/csx-web`（当前 Mac：`/Users/stark/Desktop/work/csx-web`）             |
| 本 Cursor skill                    | `/Users/<你的用户名>/.cursor/skills/ask-csx-web-react/SKILL.md`                                         |
| Codex 对照 skill                   | `/Users/<你的用户名>/.codex/skills/csx-web-react/SKILL.md`                                              |
| TECH-8370 / TECH-8458 私有技术文档 | `/Users/<你的用户名>/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md`                              |
| CTO 旧 `csx-web` 全量迁移评估      | `/Users/<你的用户名>/.codex/skills/csx-web-react/csx-web全量迁移到csx-web-react工作量评估.md`           |

若用户明确给出 fork、分支 worktree 或临时路径，以用户指定路径为准；不要把用户目录下的 skill 路径误当成业务仓库根。后续 `{workspace}` 均指当前实际工作区根。

## 新会话必读顺序

新 chat 或首次进入本仓库任务时，按以下顺序读取；已有上下文中已实际加载的文件可不重复读，但不能只凭文件名或历史摘要假设已加载。

1. **本 skill 文件**：确认入口目标、路径、状态快照、下一步任务和门禁。
2. **检查 TECH-8370 / TECH-8458 文档门禁**：仅当本文件「最新待继续问题」中存在未注释的 TECH-8370 / TECH-8458 需求问题或子任务时，读取私有技术文档；否则不要读取、摘要或更新该文档。用户明确要求读取 / 更新该文档时，以用户本轮要求为准。
3. **项目规则与锚点文件**：
   - `{workspace}/.cursor/rules/project-context.mdc`
   - `{workspace}/package.json`
   - `{workspace}/next.config.ts`
   - `{workspace}/README.md`
4. **API 相关任务**：按「API 文档与 Swagger 查询门禁」先核对 OpenAPI，再读或改 API 代码。
5. **任务直接相关文件**：只读取当前任务涉及的 `src/`、`e2e/`、配置、脚本或测试文件。
6. **部署 / CI/CD 任务**：再读取 `{workspace}/bitbucket-pipelines.yml` 和相关脚本。
7. **旧 Vue 入口或旧系统对照**：先读取 Cursor 侧 `ask-csx-web` 或 Codex 侧 `csx-web` skill，再读取 `/Users/stark/Desktop/work/csx-web` 中的直接相关源码。

若仓库文件、README、项目规则、本 skill 和 Codex skill 冲突，优先级为：当前源码 / 配置 > README 工程规则 > 私有技术文档中已确认事实 > 本 skill 快照 > 旧对话或历史摘要。

## TECH 文档加载与更新门禁

- 默认**不读取** `CSX顯示屏配置技术文档.md`。
- 当本文件「最新待继续问题」中存在任何未注释的 TECH-8370 / TECH-8458 需求问题或子任务时，视为 **TECH-8370 / TECH-8458 活跃轮次**，必须读取私有技术文档。
- 活跃轮次中，如果未完成任务明确要求读取 ClickUp 页面，先用可用的浏览器 / MCP 工具读取点名的 TECH-8370 / TECH-8458 页面，再按私有技术文档规则读取 PRD。
- 活跃轮次每轮结束前，必须更新本 skill 的项目状态恢复快照和下一步任务列表；私有技术文档只在需求事实、架构/API/部署结论、外部问题草稿或验收清单发生变化时更新对应权威章节。
- 更新私有技术文档时至少检查第 0 节职责分工、第 8 节外部问题和本轮涉及的权威章节；不得只在末尾追加流水，必须去重、删除过期结论，并保持 README / 私有技术文档 / 本 skill 三者分工一致。
- 去重检查必须覆盖精确重复、语义重复和过期冲突；同一事实只保留一个权威章节，其它章节改为引用或删除。
- 私有技术文档章节职责固定：第 0 节保存恢复入口、文档分工和冲突优先级；需求事实和产品边界进第 2 节，稳定架构决策进第 3 节，重要开发事实和验证证据进第 5 节，估时进第 6 节，问题统一结论进第 7 节，未解决外部依赖和对外问题草稿进第 8 节，部署验收清单进第 9 节，第 10 节只保存“当前状态 / 下一步已迁移到 skill”的说明。
- 不在技术文档中维护逐 chat 执行流水、完整当前状态、完整下一步或重复的“给产品当前状态说明”；需要对外回复时，临时从第 8 节、README 部署流程和本 skill 当前状态生成。
- 条件不满足时，不读取或更新私有技术文档；README 仍只维护仓库工程规则，不写入需求、当前状态、UI 验收、API 字段映射、对外问题草稿或临时结论。
- 用户输入框单独提及 TECH-8370 / TECH-8458，但「最新待继续问题」中没有未注释的相关需求问题或子任务时，不自动触发该文档加载和更新；用户本轮明确要求读取 / 更新该文档除外。

## 外部问题清单维护与重新提问提醒门禁

TECH-8370 / TECH-8458 活跃轮次中，私有技术文档第 8 节是尚未解决的外部问题唯一维护位置。每轮出现以下任一情况时，必须检查并更新对应负责人问题清单：

- 用户提供产品、旧 `csx-web` 前端、后端 API 开发或运维的新回复。
- 源码、网页、API、Pipeline、Figma、PRD、测试或联调结果证明原问题已回答、前提错误、负责人错误或需要追问。
- 本轮新增需求、方案、风险、阻塞、环境或部署结论，需要外部负责人确认后才能继续。
- 原问题已经可以由当前上下文直接回答，不应继续向外部人员询问。

负责人路由固定为：后端 API 开发只确认 API contract、公开访问安全、数据规则、接口错误与降级；旧 `csx` POC / Prod release owner 确认历史合包、Jenkins wrapper、前端产物如何注入最终 package；运维确认实际部署矩阵、静态托管、线上路径映射和部署覆盖；旧前端确认旧源码无法确认的实际运行、入口集成和兼容事实；产品确认需求范围、优先级、交互、显示规则和验收口径。

更新规则：

1. 先把新回复或证据沉淀到第 2、3、5、7、9 节中对应权威章节，再更新第 8 节；第 8 节不得重复保存已确认结论。
2. 已回答、已由源码验证、前提失效或不再阻塞的问题必须删除；部分回答的问题改写为只追问剩余未知项。
3. 新问题必须问对负责人、可直接发送、包含必要上下文，并明确需要对方确认的具体事实；不得把 API 问题发给运维、把线上承载 / rewrite 问题发给后端 API 开发，或要求前端决定产品范围。
4. 若问题清单变化会改变执行顺序、阻塞或交付路径，同步更新本 skill 的下一步任务列表；只调整措辞且不改变行动时，不新增下一步。
5. 仅当本轮对第 8 节问题清单发生实质变化时，最终回复增加 `需要重新提问`，按负责人列出新增、改写或仍需追问的问题；仅格式调整、排序、去重或没有新增证据时写 `需要重新提问：无`。

## API 文档与 Swagger 查询门禁

当前项目有传统 `csx POC` 与 `csx-k8 dev` 两套 Swagger 文档入口。API 任务必须按目标系统选择对应文档；若需要比较 `csx` 与 `csx-k8`，必须同时查询两套 OpenAPI 定义并列出差异。

| 系统         | UI                                                      | OpenAPI JSON                                                 |
| ------------ | ------------------------------------------------------- | ------------------------------------------------------------ |
| 旧 `csx`     | `https://poc.demo.clinicsolution.hk/swagger/index.html` | `https://poc.demo.clinicsolution.hk/swagger/v1/swagger.json` |
| `csx-k8 dev` | `https://api-poc.clinicsolution.hk/swagger/index.html`  | `https://api-poc.clinicsolution.hk/swagger/v1/swagger.json`  |

执行当前项目 API 相关任务时，必须先主动查询目标系统的 Swagger / OpenAPI 定义，再读代码或写实现；不得只凭截图、历史记忆、旧 Vue 源码或已写代码推断接口 contract。若 Swagger UI 页面不可用，优先直接读取同域 `swagger/v1/swagger.json`；JSON 也失败时再说明实际失败并降级到旧源码、浏览器网络请求或后端截图证据。

API 查询最小动作：

1. 用 Swagger / OpenAPI 定位目标 path，记录 `method`、`summary`、`tags`、query parameters、requestBody、response schema 和必要 `$ref`。
2. 当 `NEXT_PUBLIC_CSX_SYSTEM=csx-k8`、使用 `pnpm dev:k8` / `dev:k8:direct` / `build:poc:k8` / `build:prd:k8`，或任务明确提到 K8 dev / K8 Prod 时，以 `csx-k8` Swagger 为当前实现依据；传统 `csx` 环境则以旧 `csx` Swagger 为当前实现依据。
3. Swagger 定义、旧 Vue 源码、运行时网络请求或后端回复冲突时，明确列出冲突来源；只把已验证的一方作为当前实现依据，剩余 contract 放入私有技术文档第 8.1 节向后端追问。
4. 修改 `src/lib/display-api.ts`、`src/lib/api-client.ts`、环境配置、API 测试或 mock 数据前，先把本轮实际查到的接口定义用于校验字段名、参数大小写、请求方法、header、requestBody、response schema 和公开访问策略。

大屏队列相关接口优先核对：

- `GET /api/AppointmentQueueData/GetQueuePatientListAsync`
- `POST /api/AppointmentQueueData/AddOrUpdateCallNumber`
- `GET /api/AppointmentQueueData/GetNextAppointmentId`
- `GET /api/AppointmentQueueData/GetClincInfoAsync`
- `GET /api/AppointmentQueueData/GetDoctorProfilePictureAsync`
- `GET /api/AppointmentQueueData/GetQueueNewPatientListAsync`
- `POST /api/AppointmentQueueData/Test`

## 稳定项目事实

- `csx-web-react` 是独立 Next.js / React static export 项目；默认部署路径为 `/display-screen-config/`，构建产物为 `out/`。
- 技术栈以 `{workspace}/package.json` 和源码为准：Node `>=20.9`、pnpm `>=8.15`、Next.js `16.1.1`、React `19.2.3`、TypeScript、Tailwind CSS 4、ESLint 9、Playwright。
- `next.config.ts` 使用 `output: 'export'`、默认 `basePath` / `assetPrefix` 为 `/display-screen-config`、`trailingSlash: true`、`reactStrictMode: true`、`images.unoptimized: true`。
- App Router 路由入口在 `src/app/`；业务 feature 主要在 `src/features/`；共享 API、鉴权、映射和工具在 `src/lib/`。
- CSX 登录态由 same-origin browser storage 提供；管理后台配置页请求应经 `src/lib/api-client.ts` 加 CSX auth / locale headers。
- 公开大屏页面预期可免 CSX 登录访问；最终安全边界由后端 API 保证。
- 本项目与旧 Vue `csx-web` 分仓处理；除非用户明确要求，不修改旧 Vue 的依赖、webpack、构建命令或 pipeline。
- README 只维护通用工程规则、环境脚本、static export、pipeline、部署流程和验证方式；不要写入需求事实、截图流水、当前状态或敏感信息。
- TECH-8458 公开大屏外层必须填满当前浏览器可显示区域，不能固定为 `768px` 居中画布；`768 × 1366` 仅作为竖版设计基准。页面背景使用浅蓝灰 `#edf3fc`，主区域高度、核心 UI 字号、图标和图片尺寸不得因为浏览器宽度或横竖屏方向变化而改变。
- 公开大屏里所有文字、医生头像、二维码和关键图片的高度都不得因为浏览器变宽而变大或变小；同高不同宽 viewport 下只能改变横向排布和可用宽度，不能改变核心纵向尺寸。
- 诊所品牌中英文名称按 Figma `Bold/小标题` 使用 `Outfit 700 / 16px / line-height 100%`；医生列表卡片头像不得使用卡片宽度百分比放大。
- 媒体区视频按产品确认默认静音播放；以后等 API 返回声音配置字段后，再按字段决定有声或无声。
- 本地 `pnpm dev:k8` 使用 `next dev --webpack` 启动 Next.js dev server，并启动本地 API 代理 `http://127.0.0.1:3100`；不要把手动删除 `.next` 当作日常开发流程。
- 当前职责边界：前端负责 React 实现、构建产物、Bitbucket 前端 pipeline 和可验证配置；后端 API contract、Jenkins 合包 wrapper、最终 release package 注入和运维部署不是前端开发职责。

## 状态与文档维护规则

- 新 chat 默认从本 skill 的「最新待继续问题」、用户输入框、项目配置和源码恢复最小必要上下文。
- 每次执行 `csx-web-react` 当前项目相关任务后，最终回复前必须更新本 `SKILL.md` 的「项目状态恢复快照」和「下一步任务列表」，用于新 chat 恢复上下文。
- 本 skill 快照只保存恢复所需的最新事实、当前阻塞和最小下一步；不得写逐 chat 流水、长推理、敏感凭证、可从 README 恢复的工程规则全文，或可从私有技术文档恢复的 TECH 细节全文。
- 如果本轮是 TECH-8370 / TECH-8458 活跃轮次，先按变化范围更新私有技术文档权威章节，再把本 skill 快照同步为当前状态和最小下一步；完整下一步以本 skill 为准。
- 如果本轮改变工程规则，先同步 `{workspace}/README.md`，再在本 skill 快照中记录 README 已同步；不要把工程规则全文复制到 skill。
- 更新本 skill 快照时必须删除过期状态和已完成下一步，保持单一最新列表，不得只追加历史记录；新事实应合并进既有主题条目，不使用日期前缀记录对话流水。
- 条件不满足时，不读取或更新私有技术文档；README 仍只维护仓库工程规则，不写入需求、状态、UI、验收、接口字段或临时结论。

## 验证速度规则

- 开发迭代期间优先运行与当前改动直接相关的定向测试、单个 Playwright 用例、单一 viewport 或浏览器局部检查；不得在每个小改动后重复运行完整 Playwright 测试矩阵。
- 完整 `pnpm test:e2e` 仅在用户明确要求、阶段性任务准备最终交付 / 提交，或修改共享 API、路由、全局布局、轮播状态机等高风险公共行为时运行一次。
- 同一轮已经通过完整测试后，后续小范围 CSS、文案或文档调整默认只做定向回归；除非发现失败或新增高风险改动，否则不再次运行完整测试。
- `lint`、`typecheck`、`build` 也按风险选择执行时机；开发中先快速验证，最终收尾再集中运行必要质量门。

## 阶段门禁

- 是否允许继续推进，优先根据用户输入框、「最新待继续问题」、项目配置、源码和当前任务直接相关文件判断。
- 外部 API、产品规则或部署条件未满足时，可以实现不依赖它们的模型、mock、页面骨架、空状态和测试骨架，但不能把它们标记为真实联调完成。
- 若实现中发现 static export 无法满足需求，回退到架构与部署评估，不能直接引入 Node Server / SSR。
- 真实 API、部署和测试数据未准备好时，不把项目标记为可上线。

## 环境与命令锚点

| 环境               | 本地启动            | 构建脚本            | API 规则                                |
| ------------------ | ------------------- | ------------------- | --------------------------------------- |
| 旧 `csx` POC       | `pnpm dev:csx`      | `pnpm build:poc`    | 同源相对 `/api`                         |
| 旧 `csx` Prod      | `pnpm dev:csx:prod` | `pnpm build:prd`    | 同源相对 `/api`                         |
| `csx-k8` dev / POC | `pnpm dev:k8`       | `pnpm build:poc:k8` | `https://api-poc.clinicsolution.hk/api` |
| `csx-k8` Prod      | `pnpm dev:k8:prod`  | `pnpm build:prd:k8` | `https://api.clinicsolution.hk/api`     |

开发迭代期间优先运行与当前改动直接相关的定向验证；阶段收尾或高风险公共逻辑改动后再运行 `pnpm lint`、`pnpm typecheck`、目标 build 或 Playwright。

## 任务路由（关联 skills）

按任务类型选用专项能力（macOS 默认在 `/Users/<你的用户名>/.cursor/skills/<name>/SKILL.md`）。路由后必须先读取对应 `SKILL.md` 及其 `workflow.md` / `checklist.md` / `reference.md` 等依赖。

| 场景                               | Skill / 行动                                                      |
| ---------------------------------- | ----------------------------------------------------------------- |
| 规则缺失或刷新项目规则             | `init-project`                                                    |
| React / Next.js 实现               | 项目规则 + 直接相关源码；涉及类型边界时加 `typescript-strict`     |
| Figma UI 对齐                      | Cursor Figma skills / MCP；若工具不可用，明确失败并给最小配置步骤 |
| 代码审查                           | `code-review` 或 `bmad-code-review`                               |
| 架构讨论                           | `architecture-review` 或 `bmad-agent-architect`                   |
| 规格清晰的快速实现                 | `bmad-quick-dev`                                                  |
| 已有 story 文件                    | `bmad-dev-story`                                                  |
| Cursor / MCP / Rules / Skills 问题 | `ask-cursor` 或 `create-skill`                                    |
| 旧 Vue `csx-web` 对照              | `ask-csx-web` 或 Codex 侧 `csx-web`                               |

## 图片与 Figma 门禁

- 用户、skill、项目文档或待继续问题中出现 `![img_xxx.png](img_xxx.png)` 时，必须按引用源 `.md` 同目录拼接文件名精确读取图片；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。
- 从 Codex skill 迁移来的截图任务，图片默认在 Codex skill 所在目录；除非已把图片文件复制到 Cursor skill 同目录，不要把相对图片引用改写为 Cursor skill 同目录引用。
- 涉及 Figma 样式、尺寸、节点结构或变量时，必须用可用的 Figma MCP / 插件读取节点事实；不得只凭浏览器截图或肉眼观察替代。

## 执行工作流

1. 确认任务针对 `csx-web-react` 或用户指定的 worktree。
2. 按「新会话必读顺序」恢复最小上下文，并检查 TECH 文档门禁。
3. 合并用户输入与本文件「最新待继续问题」，形成当前验收范围；用户明确裁剪时以用户裁剪为准。
4. 分类任务：需求 / 实现 / 排障 / API / Figma / 部署 / 审查 / 文档。
5. API、Figma、图片、BMAD 或其它 skill 触发时，先完成对应门禁。
6. 修改前说明计划修改文件和验收标准。
7. 实现后按风险运行定向验证；未运行应用、构建、测试、浏览器或外部页面读取时明确说明。
8. 活跃 TECH 轮次结束前，按变化范围更新私有技术文档；每次当前项目相关任务结束前，更新本文件的状态快照和下一步任务列表。
9. 最终回复说明完成内容、验证结果、剩余风险、下一步、需要重新提问的负责人及问题文本，以及文件加载清单。

## 输出约定

完成阶段性任务时，按实际已加载上下文提供：

```markdown
本轮产出：<完成的代码 / 文档 / 决策>
当前阻塞：<阻塞项 / 无>
当前建议下一步：<最小可执行动作>
需要重新提问：<无 / 按产品、旧前端、后端 API、运维分组列出可直接发送的问题>
私有技术文档：<未加载 / 已按严格条件加载>
README 工程规则：<无需更新 / 已同步 / 本轮结论不适合写入 README>
项目状态恢复快照：<已更新 / 未更新及原因>
当前 chat 上下文已加载的关键文件：<列表>
执行当前任务过程中新增读取/加载的文件：<列表 / 无新增>
```

回复使用简体中文；代码与代码注释使用英文。不得把 token、密码、Cookie、私钥、证书、部署凭证或其它敏感值写入代码、文档、skill 或最终回复。

## 项目状态恢复快照（每轮结束更新）

用于新 chat 快速恢复当前项目上下文。每次当前项目相关任务结束前维护本节；不要把逐 chat 流水、敏感信息、长推理或私有技术文档详述写入这里。

### 最新状态

- `csx-web-react` 是独立 Next.js / React static export 项目；默认 `basePath` / `assetPrefix` 为 `/display-screen-config`，构建产物为 `out/`。README 已收敛为仓库级工程手册，只维护技术栈、目录结构、四条主链路环境脚本、页面入口、Static Export、Bitbucket Pipelines、通用本地构建产物验证流程、Figma 工作流前置条件、质量门和工程边界；私有技术文档只维护 TECH-8370 / TECH-8458 需求事实、API 口径、UI 规则、部署结论、验收清单和必要外部问题。
- CTO 要求的旧 `csx-web` 全量迁移评估已更新到 `/Users/stark/.codex/skills/csx-web-react/csx-web全量迁移到csx-web-react工作量评估.md`。当前口径为纯前端迁移评估：旧系统剔除技术 / 承载路由和已确认无需迁移的大屏相关入口后，需要迁移的独立业务页面为 121 个，独立业务页面组件为 120 个，压缩纯前端估算合计为 70.26 个工作日；最终仍需 CTO / 产品先冻结必须迁移范围、废弃页面、优先业务域和是否接受分阶段迁移。
- TECH-8458 第一阶段公开大屏前端骨架和主要 UI 修复已完成；已实现免登录公开大屏、真实 API 顺序展示完整医生名单、固定最新叫号区、医生列表分页 / 轮播、5 秒诊所 / 队列增量轮询、诊所信息完整签名比较、诊所品牌增量更新、队列变化局部刷新、队列内嵌 `doctorProfile.iconUrl` / `teleconsultationAvailable` 驱动头像和视频诊症图标更新、头像 URL 版本参数绕过缓存、`videoURL` 变化才重启视频、二维码 15 分钟独立刷新、多视频循环、默认静音播放和异常状态。
- 公开大屏数据更新口径已收敛：顶部最新叫号区只使用 `GetQueueNewPatientListAsync.latestCallNumberDoctorProfile`；该对象为 `null` 或缺失时顶部显示 `暫無叫號 No call numbers available`，不从 `item[]` 借用医生姓名。医生轮播卡和 `Total Queued` 继续来自 `GetQueueNewPatientListAsync.item[]` / `item[].doctorProfile`；5 秒轮询时仅 `latestCallNumberDoctorProfile` 深度签名变化只更新顶部最新叫号区，`item[]` 深度签名或数量变化才重置医生轮播和进度，二者都未变则页面显示不变。
- 大屏专属样式已从 `src/app/globals.css` 拆到 `src/features/display-screen/display-screen.css`；两个大屏路由入口显式引入 feature CSS，避免 `body { overflow: hidden; }`、`.doctor-card`、`.queue-stats` 等样式污染未来页面。最新响应式 UI 结论：顶部科室固定在医生中文名上一行且不换行，空间不足时 chip 内文字省略；中文医生名固定第二行，英文医生名保持单行省略；白色医生卡片多科室最多显示两行；顶部 `最新叫號 Last Call`、白卡 `最新叫號 Last Call` 与白卡 `等候 Queued` 三处标签字号均为 `18px`。
- 当前工作树有未提交的 `src/features/display-screen/display-screen.css` 调整：顶部最新叫号区英文医生名、白色医生卡片中文名和英文名均加粗到 `font-weight: 700`，并抽出 `--call-label-font-size: 18px` 统一叫号 / 等候标签字号。Cursor 侧 Chrome DevTools MCP 已可用。本地公开大屏 `http://localhost:3000/display-screen-config/tvScreenNew/?clinicCode=0-Doctor%20Lee&deviceId=38a6be9e-3a19-454b-a0e1-c7d5689101eb` 已实页验证：页面 HTTP 200，无控制台报错；浏览器请求经 `http://127.0.0.1:3100` 代理，`GetClincInfoAsync`、`GetQueueNewPatientListAsync`、`GetCallNumberScreenPageSettingAsync`、`DownloadFileInBase64` 均返回 HTTP 200 / `code:0`，响应头 `csx-currversion: 1.9.14.260807.7978c8a87`。该 `deviceId` 配置为竖版、主题色 `#FFB600`，诊所宣传视频关闭、總排隊人數关闭、自助排队二维码开启；顶部因 `latestCallNumberDoctorProfile=null` 显示 `暫無叫號`，医生列表 `item.length=4` 按两卡分页显示 `1 / 2`。
- 已完成的主要验证包括 `pnpm typecheck`、`pnpm lint`、`pnpm run build:poc:k8`、浏览器 DOM 验证、本地旧 `csx` POC 页面 HTTP 200 健康检查、Chrome 真实页面验证、本地 `csx-k8 dev / POC` 页面 HTTP 200 和 API 代理 200 验证。执行新任务前仍需按当前工作树和改动风险重新选择验证范围。
- 大屏自助排队二维码当前按 `${checkinHost}/new/{healsCoreId}?d={timestampPayload}` 生成，15 分钟独立刷新且不跟随 5 秒诊所 / 队列轮询重置；若 `healsCoreId` 为空则隐藏二维码浮层。当前 React 只负责二维码 URL 生成；checkin-dev 已确认支持 `/new/{healsCoreId}`。
- 本地开发脚本已收敛为四条主链路：`pnpm dev:csx`、`pnpm dev:csx:prod`、`pnpm dev:k8`、`pnpm dev:k8:prod`。`pnpm dev:k8` 会启动 Next `http://localhost:3000` 和本地 API 代理 `http://127.0.0.1:3100`，代理真实转发到 `https://api-poc.clinicsolution.hk`；旧 `csx` POC / dev / Prod 已收敛为默认同源 `/api`，`csx-k8 Prod` 使用 `https://api.clinicsolution.hk`。
- `csx-k8 dev` 正式页面入口保持 `https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode={clinicCode}`；Bitbucket `#96` 已验证是远端 `main` 更新后的成功 branch pipeline。`https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TES` 当前无法访问的问题已由用户确认是运维问题，不再作为前端配置问题追问。
- `csx-k8 prod` 前端侧配置已补齐：`custom: deploy-to-prod` 使用 `pnpm run build:prd:k8`，deployment environment 为 `production`，目标页面 `https://csx.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode={clinicCode}`，API base `https://api.clinicsolution.hk`。Bitbucket `production` deployment environment 只需要 `DISPLAY_SCREEN_S3_BUCKET`、`DISPLAY_SCREEN_CLOUDFRONT_DISTRIBUTION_ID` 两个 deploy step 变量；pipeline 已有 deploy 前预检，真实值仍需 DevOps 替换并重跑 `custom: deploy-to-prod`。
- 旧 `csx` POC / Prod 不在 29 / Windows Jenkins 上 build React，也不把 React 源码移入旧 `csx-web`。既定方案由 Bitbucket 先生成 `react-artifact.zip`，zip 第一层为 `display-screen-config/**`，再由后端 / release owner 的 Jenkins wrapper 下载、校验并注入最终 CSX release package。
- 旧 `csx` POC 的 React artifact、解压目录、后端应用层静态文件映射和公网 release / deploy 链路已验证通过；`https://poc.demo.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TESTCLINIC` 已返回 HTTP 200，静态资源和 API 请求路径正确。后续仅在前端代码更新时重新生成 POC artifact，并由后端 / release owner 按既有流程重新合包和发布。
- 旧 `csx` Prod 已配置 `custom: build-old-csx-prod-artifact`，目标 fixed latest 为 `csx-web-react-old-csx-prod-main-latest.zip`；旧 Prod React 示例 `https://sfsc3051.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=SFSC` 已验证返回 HTTP 200、静态资源来自同 host `/display-screen-config/**`、API 请求同源 `/api/...`。旧 Prod 多租户不需要按租户生成不同 artifact；若线上页面仍请求 `GetDoctorProfilePictureAsync`，先让后端 / release owner 排查 Jenkins 下载、合包工作区和最终 CSX release package 是否实际使用最新 old Prod artifact。
- Figma 工作流已在 Codex 配置中启用 `mcp_servers.figma.enabled=true`，Codex 会话可通过 Figma MCP 读取节点；后续涉及 Figma 节点事实时继续优先使用 Figma MCP，不用浏览器截图或肉眼观察替代。
- 不得把 token、密码、Cookie、私钥、证书或部署凭证写入 README、skill、技术文档、脚本或最终回复。已泄露过的 Atlassian token 后续仍建议轮换，但不阻塞当前 old POC 合包验证。当前职责边界：前端负责 React 实现、构建产物、Bitbucket 前端 pipeline 和可验证配置；后端 API contract、Jenkins 合包 wrapper、最终 release package 注入和运维部署不是前端开发职责。

### 下一步任务列表

1. CTO 旧 `csx-web` 全量迁移评估：把 `/Users/stark/.codex/skills/csx-web-react/csx-web全量迁移到csx-web-react工作量评估.md` 的结论和 Markdown 表格发给 CTO / 产品，让他们先确认必须迁移范围、废弃页面、优先业务域和是否接受分阶段迁移；不要在范围未冻结前承诺全量重写排期。
2. TECH-8458 公开大屏：主要逻辑、UI、样式隔离和医生姓名加粗已完成；本地已用 Chrome DevTools 验证带 `deviceId` 的 `0-Doctor Lee` 大屏能按设备配置渲染。下一步如无新增 UI / API 问题，提交当前 `src/features/display-screen/display-screen.css` 改动，并按目标环境重新构建 old POC / K8 dev / K8 prod artifact 或部署。
3. 旧 `csx` POC：本地 latest zip 结构、后端解压目录、29 内网访问和公网 POC `TESTCLINIC` URL 均已验证通过；仅在前端代码更新时重新生成 POC artifact，并请后端 / release owner 按现有 POC release / deploy 流程重新合包和发布，无需运维改 IIS / rewrite / virtual directory。
4. 旧 `csx` Prod：`sfsc3051` 旧 Vue 入口和 React 新页面均已公网验证可访问，Prod host / 同源 API / 多租户 artifact 口径已收口。若线上页面仍请求 `GetDoctorProfilePictureAsync`，下一步先让后端 / release owner 对比 Jenkins 下载的 fixed latest zip、合包工作区和最终 CSX release package 中的 JS chunk。
5. 旧 `csx` frontend / non-k8 部署流程：DevOps 询问 `process of deployment to csx frontend (non-n8)` 时，回复应聚焦旧 `csx` POC / Prod 的 Bitbucket artifact、后端 / release owner Jenkins wrapper 下载校验、注入最终 CSX release package、运维继续按现有最终 package 部署；不要覆盖或替代 `csx-k8 prod` 的 DevOps 问题。
6. `csx-k8 prod`：前端 build / deploy pipeline 已配置完成，当前阻塞类型是 production deployment 的 `DISPLAY_SCREEN_S3_BUCKET` 或 `DISPLAY_SCREEN_CLOUDFRONT_DISTRIBUTION_ID` 真实值 / 权限未确认；下一步让 DevOps 替换两个 `DISPLAY_SCREEN_*` 变量的真实生产值，并确认 `/display-screen-config/**` 静态托管和 deep link 支持。变量值填好后运行 `custom: deploy-to-prod` 并验证页面请求 `https://api.clinicsolution.hk/api/...`。

## 最新待继续问题（不要修改这部分的子内容）
<!-- - 借鉴`/Users/stark/.codex/skills/csx-web-react/SKILL.md`和当前项目状态,更新当前skill -->
<!-- - 新 chat 执行 `/csx-web-react` 后，先执行用户输入框里的具体任务；没有具体任务时，根据项目配置和源码恢复最小必要上下文 -->
<!-- - 为什么 skill里还有类似如图这种带日期的聊天流水内容? 把 skill 和技术文档以及`/Users/stark/Desktop/work/csx-web-react/README.md`里 的 和 `2026` 相关的带日期的聊天流水内容沉淀成 既定事实,以后不要再新增 对话流水内容 -->
<!-- - 我负责 当前项目的前端开发,不负责 后端API 和 部署运维的开发; -->
<!-- - 接下来的工作流是需要你用`Chrome DevTools`或codex的`Chrome`插件读取figma的节点信息,然后帮我布局页面的UI,目前你能否执行这个工作流?
  - 已经重启,帮我验证下如图![img_100224.png](img_100224.png)这个任务是否完成 -->
<!-- - 帮我总结下 git commit message -->
<!-- - 如果你在当前chat的上下文里没有用 `chrome_devtools` 读取过 `https://app.clickup.com/t/8553538/TECH-8370`页面的需求描述,先查看这个需求的需求描述和当前第一阶段只需要做的子需求`https://app.clickup.com/t/8553538/TECH-8458`的需求描述,不用看Activity里的内容,再解决以下未注释的问题; -->
<!-- - 你本地启动当前项目在`旧csx`系统的dev(http://192.168.99.29:8083)环境 -->
<!-- - 你本地启动当前项目在`旧csx`系统的poc环境,请求`https://poc.demo.clinicsolution.hk/api/` -->
<!-- -你本地启动当前项目在`旧csx`系统的prod环境 ,访问 sfsc3051 这个租户的页面 ,请求`https://sfsc3051.clinicsolution.hk/api`-->
<!-- - 你重新本地启动当前项目在`csx-K8`系统的dev(也是poc)环境 ,请求 `https://api-poc.clinicsolution.hk/api` -->
<!-- - 精简优化技术文档和`README.md`,技术文档只保留项目里已经做过的所有需求的已经沉淀的事实,而`README.md`只保留和具体需求无关的通用的项目配置和事实规则 -->
- 大屏需求相关:
    <!-- - 我访问了`http://192.168.99.29:8083/display-screen-config/tvScreenNew/?clinicCode=ClinicB` -->
    <!-- - 我访问了 `http://localhost:3000/display-screen-config/tvScreenNew/?clinicCode=TESTCLINIC` -->
    <!-- - 我访问了 mock页面 `http://localhost:3000/display-screen-config/tvScreenNew/?mock=1&doctors=2` -->
    <!-- - 我访问了 `http://localhost:3000/display-screen-config/tvScreenNew/?clinicCode=TES`页面 -->
    <!-- - 我访问了`https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TES` -->
    <!-- - 再帮我验证下目前页面加载逻辑是否是:
        - 页面加载后先请求一次`https://poc.demo.clinicsolution.hk/api/AppointmentQueueData/GetClincInfoAsync`和`https://poc.demo.clinicsolution.hk/api/AppointmentQueueData/GetQueueNewPatientListAsync?clinicCode=TESTCLINIC&pageIndex=1&pageSize=1000`API;
        - 第一轮请求完这2个API之后,每5秒再请求一轮`GetClincInfoAsync`和`GetQueueNewPatientListAsync`这2个API
        - 针对`GetClincInfoAsync`api,判断最新返回的数据是否和上次返回的数据的所有字段的值一致(不仅要比较每条数据对象的第一层的字段的值,还有比较子对象里的数据,也就是深度比较);如果不一致,就根据最新的某个字段的值是否变化更新页面的![img_164400.png](img_164400.png)区域或重新轮播![img_164415.png](img_164415.png)视频区域;
        - 针对`GetQueueNewPatientListAsync`API,判断最新请求的API返回的item数组的每条数据的顺序是否和上次这个API返回的item数组的每条数据的循序一致,并且每条数据的每个字段的值(不仅要比较每条数据对象的第一层的字段的值,还要比较子对象里的数据,也就是深度比较)是否和上次这个API返回的item数组的每条数据的每个字段的值一致,并且医生数量是否一致;如果都一致,就继续轮询显示;如果不一致,就根据最新这个API返回的数据刷新如图![img_105124.png](img_105124.png)红框处的医生轮播区域,重新轮询显示医生(![img_154503.png](img_154503.png)进度条记得重置;重新轮播的原因是`如果有10条数据,当前轮播到了第3条,改了第9条数据的某个字段,比如医生头像或简介,此时如果不重新轮播,本轮轮播到第9条数据时,就不会显示最新修改后的简介或其它字段;不能每页请求2条数据,因为轮播页面不能固定显示2个医生,可能4个,可能3个`),重新计算總排隊人數的值;轮询显示完所有医生后, 不再需要重新请求这2个API,只需要重新根据现有数据重新轮播;视频区域二维码的更新逻辑不变;
        - 如图![img_105204.png](img_105204.png)红框是叫号区,此处显示数据的更新逻辑只依赖`GetQueueNewPatientListAsync`返回的`latestCallNumberDoctorProfile`对象和上一次返回的`latestCallNumberDoctorProfile`对象进行深度对比之后是否变化;`latestCallNumberDoctorProfile`对象为null或者没有此字段时,整个叫号区不显示内容,只占位显示 -->
    <!-- - ![img_231652.png](img_231652.png),![img_231700.png](img_231700.png),![img_231709.png](img_231709.png),![img_231724.png](img_231724.png),![img_231736.png](img_231736.png),这几个区域的高度目前是根据当前浏览器显示区域的高度的百分比算的
          诊所栏：6.47%
          等待队列栏：5.06%
          医生区：60.47%
          媒体区：28%
          是否正确? -->
- 顯示屏配置需求 相关:
    <!-- - 点击 旧csx系统的`https://poc.demo.clinicsolution.hk/ui/index.html#/ManagementSettings/ProgramSettings` 页面里的 ![img_151956.png](img_151956.png)红框后,  浏览器会打开一个新标签, 打开类似![img_152016.png](img_152016.png)这种页面; 新标签的页面需要创建的一个新的react的项目(技术栈可借鉴 `/Users/stark/Desktop/work/MyStartupProject1`项目) ,新项目可以当做当前项目的react版本,API环境和当前项目一致,可以把 `/Users/<你的用户名>/Desktop/work/csx-display-screen-config` 项目 的名称就成 `csx-web-react`,然后作为这个新项目,然后把技术栈更新到和`/Users/stark/Desktop/work/MyStartupProject1`项目一致,新项目的PRD 是 `https://hmolwpux55nnq.ok.kimi.link/#/displays`,你用 chrome_devtools 读取,然后 新项目里的左侧菜单栏里只显示 `程序设定-显示屏配置`页面;也就是点击 当前项目的`https://poc.demo.clinicsolution.hk/ui/index.html#/ManagementSettings/ProgramSettings` 页面里的 ![img_151956.png](img_151956.png)红框后,浏览器打开新标签,跳转到新项目的`程序设定-显示屏配置`页面  -->
- 运维部署相关:
  - 旧csx系统:
      <!-- - 当前项目的大屏页面在旧csx系统的prod环境的域名比如是`https://sfsc3051.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=SFSC`
        - 为什么页面里还请求了`GetDoctorProfilePictureAsync`API, 页面明显不是最新的代码构建的包;不现在不知道运维是否部署了如图![img_110407.png](img_110407.png)后端给他的合包,因为运维不回复;最新的前后端合包里的前端的构建zip下载解压到了`/Users/stark/Downloads/display-screen-config`,你确认下前端构建的包是否有问题 -->
      <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 `686` 行开始的 问题发给后端开发人员后, 他回复:  -->
      <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 723 行开始的 问题发给运维开发人员后, 他回复:  -->
      <!-- - 你不要完全按他们的回复方案做,需要判断他们的回复是否符合事实;如果不对的地方,需要在新问题里给他解释 -->
      <!-- - 根据当前项目的状态和`csx-web`项目的源码,以及当前chat的上下文里你已经知道的内容,从当前项目的前端开发人员的视角,总结并执行当前项目前端能做的所有任务,再用中文更新技术文档里旧`csx`系统poc环境部署相关的问题(先包含当前项目已经做了哪些),再包括给`csx-web`项目的前端开发人员Nina的问题,给后端开发人员的问题,以及给运维的问题;然后告诉我当前阶段需要发给哪些人,从第几行开始复制给他们; -->
        <!-- - 你的改动不要影响已经在csx-k8系统的dev环境部署好了的'https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode={clinicCode}' 域名
        - 你的改动和给后端人员和运维的建议,尽量不要给运维添加工作量,他很忙
        - 在你给的方案里尽量表现出不需要运维做任何改动的文案
        - 你的最新问题里需要包含前端需要的操作流程和后端需要的操作流程 -->
      <!-- - 根据项目最新状态和技术文档,以及后端的打包文档(/Users/stark/Desktop/work/csx-web-react/doc/csx打包 2.docx),帮我在`/Users/stark/Desktop/work/csx-web-react/README.md`里总结出,把当前项目部署到旧`csx`系统的poc环境的过程中,前端配置了什么(包括项目里的配置和`https://bitbucket.org/healshealthcare/csx-web-react/`里的配置以及其他地方的配置),后端配置了什么,运维配置了什么;这样如果以后部署到旧csx系统的prod环境时,可以借鉴 -->
  - csx-k8系统:
      <!-- - 目前当前项目已经部署到了旧csx系统的poc和prod环境,页面域名分别是`https://poc.demo.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TESTCLINIC`和`https://sfsc3051.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=SFSC`(sfsc3051是商户号) -->
      <!-- - 之前也部署到了csx-k8系统的dev环境,页面是`https://csx-poc.clinicsolution.hk/display-screen-config/tvScreenNew/?clinicCode=TES`,之前能访问, 现在无法访问,你检查下是当前项目的配置问题还是运维的问题;csx-k8系统的dev环境的最新的前端构建在`https://bitbucket.org/healshealthcare/csx-web-react/pipelines/results/94/steps/%7Bcf55c738-d609-4d46-aec8-81c81d991779%7D` -->
      <!-- - 现在需要进行csx-k8系统的prod环境的部署 -->
      <!-- - 根据当前项目的状态,`csx-web`项目的源码,`https://bitbucket.org/healshealthcare/csx-web-react/pipelines`的已有配置,以及当前chat的上下文里你已经知道的内容,从当前项目的前端开发人员的视角,先执行当前项目前端能做的所有关于csx-k8系统的prod环境的部署的任务,再用中文更新技术文档里问运维的关于`csx-8`系统prod环境部署相关的问题,问题里先包含当前项目前端已经做了哪些,再包括给运维的问题;然后告诉我从第几行开始复制给他们; -->
        <!-- - 你的改动不要影响旧csx系统已经部署好的poc和prod环境的配置 -->
    <!-- - 我把 `/Users/stark/.codex/skills/csx-web-react/CSX顯示屏配置技术文档.md` 的 792 行开始的问题发给运维后, 他回复 ``; -->
      <!-- - 根据项目最新状态和技术文档,帮我在`/Users/stark/Desktop/work/csx-web-react/README.md`里总结出,把当前项目部署到`csx-k8`系统的dev环境的过程中,前端配置了什么(包括项目里的配置和`https://bitbucket.org/healshealthcare/csx-web-react/`里的配置以及其他地方的配置),运维配置了什么;这样如果以后部署到csx-k8系统的prod环境时,可以借鉴 -->
- figma 相关:
   <!-- - 把当前项目的页面的布局改成响应式布局的样式,适配不同大小和分辨率的浏览器,避免出现某个元素显示不下或者被截断的情况,外层如图![img_161601.png](img_161601.png)![img_161613.png](img_161613.png)![img_161622.png](img_161622.png)![img_161629.png](img_161629.png) 这4 个大区高度继续等比例匹配 Figma；区内所有容易溢出的字体、头像、卡片、二维码等用响应式 CSS 变量和 clamp() 随浏览器尺寸适配。也就是说不是压缩某个大区，而是在对应大区内部自适应。 -->
  <!-- - 使用当前Mac系统的cursor里的codex插件的`figma`mcp拿到 `https://www.figma.com/design/R2iu3VINGNezIvRMdUjucV/CSX?node-id=17462-134442&m=dev` 这个 Figma 节点数据 -->
  <!-- -  在 `/Users/<你的用户名>/Desktop/work/RN/csx-mobile/src/pages/Diagnosis/DiagnosisPage.tsx` 页面 的 `2018` 行 ,设计实现 和当前项目代码风格一致的 组件 -->
  <!-- - 要求：
    - 匹配当前项目的代码风格（命名规范、目录组织、import 顺序等）,项目结构和技术栈
    - 复用当前项目中已有的公共组件和工具函数
    - 使用当前项目里一致的样式方案（Tailwind CSS / 现有本地组件等） -->
