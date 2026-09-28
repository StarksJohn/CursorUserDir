---
name: ask-MyStartupProject1
description: >-
  MyStartupProject1 私有恢复、BMAD 总控与市场推广持续执行入口。仅在用户显式使用
  /ask-MyStartupProject1 或 @ask-MyStartupProject1，或明确要求恢复项目阶段、继续
  BMAD/市场推广检查点时使用。每个新 chat 先调用本入口；随后强制读取 Codex 对口
  Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-MyStartupProject1

## 客户端适配

- 本入口是 Cursor 侧。显式触发词为 `/ask-MyStartupProject1` 或 `@ask-MyStartupProject1`。项目名、工作区、仓库名和路径片段不触发。
- 配对 Codex 入口：macOS `$HOME/.codex/skills/MyStartupProject1/SKILL.md`；Windows `%USERPROFILE%\.codex\skills\MyStartupProject1\SKILL.md`。正式触发词为 `$MyStartupProject1`，`/MyStartupProject1` 仅作独立兼容词。
- 两侧功能相同：事实优先级、读取门禁、BMAD 路由、生命周期、市场推广状态机、授权边界、恢复快照和下一步判断都一致。只保留触发词、初始化命令和本文件路径这些客户端写法。
- 发现重大结构冲突时，执行 Cursor 初始化入口：macOS `$HOME/.cursor/skills/init-project/SKILL.md`；Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`。不要求用户再次输入 `/init-project`。

## 调用策略与边界

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取唯一项目规则 `$HOME/.codex/skills/MyStartupProject1/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\MyStartupProject1\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得用摘要或项目根副本替代。
- 每个新 chat 先显式调用本入口，再从该 `AGENTS.md`、当前源码与聚焦测试开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行该 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时按「客户端适配」执行初始化，刷新后重新读取 `AGENTS.md` 并继续原任务。
- 本 Skill 只补充无法安全放进仓库的阶段状态、BMAD/市场推广门禁、外部阻塞和受保护待办。
- 用户给出具体任务时，该任务优先于受保护待办；只有仅调用入口或明确要求“继续”时，才解析未注释待办并从第一个未完成门禁续跑。
- 普通一次性任务优先在新 chat 第一条消息中同时写入口词和任务正文；只有需要跨 chat、跨设备或长周期恢复时，才把任务放入本文件受保护区后仅输入入口词继续。
- 医疗内容保持教育、陪伴、记录和安全提醒定位；不得表述为诊断、确定治疗方案或医生替代。生产写操作、账户清理、付款、数据迁移和破坏性操作必须有明确用户授权，并先用只读检查解析精确目标。
- 当前项目解释应照顾用户后端经验有限的背景，清楚区分前端、服务端、数据库和部署证据。不因历史付费、AI 或白名单方案仍存在代码资产，就默认把它们重新纳入当前 release。

## 路径与事实优先级

- 项目根：macOS `/Users/stark/Desktop/work/MyStartupProject1`；Windows `D:/work/MyStartupProject1`。
- Cursor 入口：macOS `$HOME/.cursor/skills/ask-MyStartupProject1/SKILL.md`；Windows `%USERPROFILE%\.cursor\skills\ask-MyStartupProject1\SKILL.md`。
- Codex 入口：macOS `$HOME/.codex/skills/MyStartupProject1/SKILL.md`；Windows `%USERPROFILE%\.codex\skills\MyStartupProject1\SKILL.md`。
- 已完成需求与稳定产品边界：`<项目根>/项目主档案.md`。
- Story / Epic 状态：`<项目根>/stories/sprint-status.yaml`。
- 工程、命令、环境、构建、数据库和部署：当前源码、`package.json`、配置与相关 `README.md` 章节。
- 市场推广假设、渠道、漏斗、阈值和停止条件：`<项目根>/market-overseas-user-acquisition-and-conversion-research-2026-08-11.md` 的完成版。
- 私有阶段、外部阻塞和最小下一步：仅在继续待办、阶段判断或市场推广检查点时读取 `$HOME/.codex/skills/MyStartupProject1/references/recovery-state.md`。
- 方向筛选、完整生命周期、文档命名和低频模板：仅在需要时读取本 Skill 同目录 `reference.md`。

冲突按以下优先级处理：

1. 当前源码、聚焦测试、真实 DOM / Network / API / Production 响应和当前 Git 状态。
2. 唯一 `AGENTS.md`、`package.json` 与相关 `README.md` 章节。
3. 用户本轮明确授权或需求来源。
4. 按需读取的主档案、Sprint 状态、市场研究文档与恢复快照。
5. 本文件受保护区块中的历史兼容待办。

快照用于恢复，不替代实时核验。开发状态以 `sprint-status.yaml` 为准；最新执行入口以恢复快照的最小下一步为准。

## 启用与最小读取顺序

仅在用户显式使用本客户端入口词，或明确要求恢复项目阶段、继续 BMAD / 市场推广检查点时启用。

1. 完整读取本 `SKILL.md`。
2. 读取唯一 `AGENTS.md` 和当前任务直接相关文件；不要通读 README、主档案、市场研究全文、恢复快照或历史附件。
3. 仅在任务依赖已完成需求、产品边界或 Story 状态时读取 `项目主档案.md` 或 `sprint-status.yaml`。
4. 仅在继续待办、判断当前阶段、处理外部阻塞或续跑市场推广时读取 `references/recovery-state.md`。阶段为 `market-promotion` 且正在续跑时，再读市场研究文档 frontmatter、`Research Synthesis` 与实验阈值；不要重复已完成的研究步骤。
5. 需要工程命令、环境或部署信息时，再读取 `package.json`、相关配置和 `README.md`。
6. 只有重新讨论方向、目标市场、首发终端、BMAD 生命周期或需要模板时，才读取 `reference.md`。
7. 路由到任意 BMAD 或其它 Skill 时，先完整读取对应 `SKILL.md` 及其明确要求的附属文件。

若用户或相关文档引用图片，先按引用源文件所在目录解析并读取图片；读取失败后才搜索。不要以摘要、旧 chat、磁盘存在或上一轮已读代替当前会话实际读取。

## 执行工作流

1. 先判断本轮是具体任务还是“继续项目”类恢复请求；具体任务不得被无关待办覆盖。同时确认任务属于回答、诊断、改动、发布还是项目规划，以及是否需要修改文件或外部状态。
2. UI、网页和生产问题先读真实页面、DOM、Network 与直接相关代码；能从真实页面取得 API 请求和响应时，不先用 Swagger 推断。
3. 代码任务依次完成仓库实现、聚焦测试，再进入文档维护判断；未完成前两段时不改 Skill、快照或主档案。
4. 开发阶段优先运行单用例、单 viewport 或相关文件检查；阶段收尾再按风险扩大到 typecheck、lint、build 或完整回归。
5. 生产发布必须区分前端、API、数据库和部署证据；即使数据库结论是“无 schema 变化”“already in sync”或受外部访问阻塞，也要单独说明。不把恢复快照当成实时 Production 证据。
6. 最终明确区分静态校验、本地运行、Production 核验和外部平台确认，不扩大成功范围。不输出 token、Cookie、密码、私钥、数据库 URL 或部署凭证。
7. 任务收尾先判断是否需要更新恢复状态、下一步列表和项目事实；只有判断为需要时才写入。详见「文档维护」。

## BMAD 路由

| 需求类型                               | 优先入口                                        |
| -------------------------------------- | ----------------------------------------------- |
| 方向、用户、痛点、价值主张、go / no-go | `bmad-agent-analyst`                            |
| 市场规模、竞品、定价和商业信号         | `bmad-market-research`                          |
| 医疗、康复、患者旅程和领域术语         | `bmad-domain-research`                          |
| Product Brief、产品定义和 MVP 边界     | `bmad-product-brief`                            |
| 路线图、优先级、里程碑和发布范围       | `bmad-agent-pm`                                 |
| 架构、技术方案和模块边界               | `bmad-agent-architect`                          |
| 单 Story 规格                          | `bmad-create-story`                             |
| 功能实现、修复和部署                   | `bmad-dev-story` 或 `bmad-agent-dev`            |
| 测试策略和验收                         | `bmad-agent-qa` 或 `bmad-qa-generate-e2e-tests` |
| 增量或发布前审查                       | `bmad-code-review` 或 `code-review`             |
| 实施准备                               | `bmad-check-implementation-readiness`           |
| Epic / Story 拆解                      | `bmad-create-epics-and-stories`                 |

### BMAD 执行门禁

- 只有真正按某个 `bmad-*` 工作流产出时才加载它；泛泛讨论阶段或角色时不批量读取子 Skill。
- 执行前读取已安装的 `~/.cursor/skills/<bmad-identifier>/SKILL.md` 或 `%USERPROFILE%/.cursor/skills/<bmad-identifier>/SKILL.md`，再读取其中要求的 `workflow.md`、`checklist.md`、`reference.md`、模板或输入发现文件。
- 磁盘上存在、历史摘要提到或上一轮读过，不等于当前 chat 已加载。
- 开始单 Story 循环前，同时读取主档案、Sprint 状态、`epics.md`、目标 Story、上一条相关 Story 和真实代码锚点；不得只根据历史摘要生成规格或实现。
- 若子 Skill 使用 `review`，而本项目状态机使用 `code-review`，以 `sprint-status.yaml` 为准并说明差异。
- Epic 1-7 和 Story 1.1-7.4 已完成；除非用户批准新范围，不要因为总控路由自动创建新 Story。
- 重新进入开发时，默认串行执行 `create-story -> dev-story -> code-review -> done`；一条 Story 未闭环前不批量生成后续 Story，除非用户明确要求或确有并行开发需要。详细循环、阶段门禁和自动回退见 `reference.md`。

## 生命周期与回退

默认生命周期为：

`方向筛选 -> 需求验证 -> 市场与竞品 -> 价值主张 -> go/no-go -> Product Brief -> MVP -> 技术方案 -> 实施准备 -> Story 拆解 -> 开发 -> 测试验收 -> 发布 -> 上线跟踪 -> 迭代决策`

- 关键上游前提未满足时，不强行推进下游。
- 用户、新证据、测试或生产结果推翻当前前提时，回退到最近一个能重新回答问题的阶段；后续产物受影响时明确标记为暂时失效。
- 当前项目已完成既有开发 Story 和 Production 全链路验收，处于市场推广执行；普通测量、推广修复和增长验收不要回到方向筛选，除非真实用户证据推翻核心需求或定位。
- 需要完整阶段定义、输出模板和回退映射时读取 `reference.md`；不要把低频模板重新复制进本入口。

## 市场推广持续执行

- 持续推进市场推广、真实用户反馈与转化观察，直到满足完成条件形成闭环，或达到已经核验且需要用户/平台外部状态变化才能恢复的明确阻塞。不得把单个渠道动作、暂无数据或时间门禁写成任务完成。
- 渠道边界：不在 X 推广；Reddit 不是唯一渠道；当前非 Reddit 公开路径为 LinkedIn；owned SEO 与搜索发现继续作为已上线入口。新增账号、社区、付费渠道、权限连接，或超出 Story 8.3 的开发范围，先取得对应授权。

当 `project_phase` 为 `market-promotion`，且用户要求“继续”“开始推广”“直到完成”或只调用本入口而没有更具体任务时，直接从 `references/recovery-state.md` 中第一个未完成门禁继续执行，不要只复述计划或等待逐步输入 `C`。

按以下状态机串行推进；发现实现或 Production 问题时回退到最近的代码、测试或发布阶段：

1. `research-complete`：市场研究已确认，定位、渠道、漏斗、阈值和停止条件已落盘。
2. `measurement-ready`：完成健康声明与隐私审计；实现最小化、可观察且经过测试的真实漏斗与结构化反馈。
3. `production-verified`：完成 build、Git/Vercel 发布、前端/API/数据库结论，并用真实 Production 验证事件链；测试账号和内部流量不得计入市场指标。
4. `campaign-live`：至少一个高意图内容入口和一个经规则核对的合规获客动作已真实上线；记录受控 source/campaign，不批量灌水、不伪造身份或社会证明。
5. `observation-active`：持续读取真实外部用户的 Day 1/3/7/14、错误与结构化反馈；样本或时间未到时保持 active，不把“暂无数据”写成完成。
6. `decision-complete`：达到研究文档规定的预注册样本与观察窗，或触发明确停止条件；形成有证据的 go/hold/stop 决策、遗留风险和下一迭代入口。

只有同时满足以下条件，才把市场推广任务标记为完成：

- Production 中的声明、隐私漏斗、关键页面/API 和数据库结论已验证。
- 已执行真实合规获客，且至少获得一个可审计的渠道结果；不得把 mock、开发者访问、测试账号、自动化流量或免费注册写成真实用户、自然搜索或付费意愿。
- 已按预注册阈值完成观察，或因安全、隐私、渠道政策、无效获客等停止条件形成可解释的终止决策。
- 已记录最终指标、用户反馈、go/hold/stop 结论和下一阶段；不存在尚未处理的 P0/P1 产品、隐私或发布问题。

用户已明确授权市场推广时，可在研究文档允许的渠道范围内执行普通公开发布；需要新账号、付费、身份或医疗资质声明、接受平台条款、向具体个人发送消息、扩大敏感数据处理或新建超出 Story 8.3 的开发范围时，先取得对应授权。禁止诊断、疗效保证、14 天痊愈、虚假临床背书、虚假评价和基于健康状态的再营销。

每次跨 turn 或跨 chat 前，先判断 `references/recovery-state.md` 是否需要更新。只有阶段、已上线渠道、观察窗、聚合指标、阻塞或最小下一步相对当前文件发生实质变化时，才覆盖写入这些字段。只保存聚合数据，不写用户邮箱、标识符、诊断或自由文本健康信息；没有实质变化时不重写文件。

### 时间门禁、轮询节流与立即推进

- 当第一个未完成门禁只依赖未来时间、样本自然增长或平台异步处理时，在检查点写入精确 UTC `next_eligible_check_at`；它只控制固定复查时点，不改变原实验阈值。
- `next_eligible_check_at` 只节流同一个定时指标检查，不暂停整个市场推广任务。用户要求“现在继续”“不能等”或“直到完成”时，立即转向当前授权范围内第一个不依赖未来时间的真实动作，不要只核对时间后结束。
- 立即动作按顺序选择：修复 Production/隐私/测量回归；完成研究已批准但尚未上线的 owned SEO 或技术发现入口；对已验证 live URL 执行尚未完成的一次性搜索发现提交；准备或执行已获授权且平台规则允许的渠道动作；最后才是新增测量能力。需要代码或新增范围时先做影响分析，并按 `create-story -> dev-story -> code-review -> release` 建立有边界的 Story。
- 当前 UTC 早于 `next_eligible_check_at` 时，不重复查询相同 summary、Search Console、DNS、Production API 或 Vercel 日志，不重写只有时间戳变化的文档，也不触发无事实变化的 docs-only 部署；但继续执行其它安全且已授权的真实推广动作。
- 提前续跑必须保持目标为 active，明确区分“该指标尚未到检查时间”和“推广工作没有可执行项”。不得用长时间 `sleep`、忙轮询、测试账号、开发者流量、重复 indexing request、重复 IndexNow 或虚构反馈制造信号。
- 若所有安全且已授权的立即动作均已完成，而剩余动作确实依赖外部登录、人工授权、平台异步结果或未来样本，则记录精确 blocker、已尝试链路和恢复后的唯一下一步，不把市场推广标记完成。新 chat 先重试该外部门禁，再考虑定时指标。
- 登录态推广写操作采用两阶段交接：当前客户端先只读确认账号、受众、精确目标和写入范围；密码、验证码、身份/职业资料保存及平台要求用户亲自完成的最终公开发布由用户操作，随后当前客户端只读核验结果。会话过期时保留已完成的平台状态并停在精确登录页，不读取或回显 Cookie、session token、DNS 验证值等敏感值；恢复后从同一标签和未完成步骤继续。
- 当唯一可推进动作是社区或社交招募，但需要使用用户账号、公开 maker 身份或联系 moderator 时，不要反复泛问“是否继续”。先只读核对当前登录态和当日规则，再给出边界完整的授权包：指定唯一平台/社区、允许的账号动作、maker 披露、消息/发帖次数、禁止私信与健康细节、追踪 allowlist 和停止条件。只有用户明确接受该授权包后才创建渠道 Story、发送消息或发布；未授权时把它记录为 `external-authorization-required`。
- 当前 UTC 到达 `next_eligible_check_at`，或出现新外部信号、用户明确要求刷新时，从对应检查点恢复一次有边界的真实查询，并据实更新下一时间点。

## 文档维护

只要本轮执行了 MyStartupProject1 相关任务，代码、测试或验证闭环后、最终回复前，必须先判断是否需要落盘，再按判断结果写入。目的是让新 chat 从任一入口恢复当前阶段、阻塞、下一步和已沉淀事实，而不是每轮追加聊天流水。

两侧入口的恢复面相同：`$HOME/.codex/skills/MyStartupProject1/references/recovery-state.md` 保存最新状态与下一步，仓库内 `项目主档案.md` 保存已完成需求事实。不要把快照重新复制进任一 `SKILL.md`，也不要每轮改受保护区。入口门禁变化时，同一任务内最小同步配对入口。

### 先判断

对照本轮已验证结果与将要改的当前文件，逐项判断是否变化；全部为否时不写文件：

1. 当前阶段、外部阻塞、推广检查点或最小下一步是否变化 → `references/recovery-state.md`
2. 已完成需求、稳定产品边界或长期业务事实是否变化 → `项目主档案.md`
3. 与具体需求无关的工程、命令、架构、环境或部署事实是否变化 → `README.md`
4. Story / Epic 状态是否变化 → `stories/sprint-status.yaml`
5. 稳定架构、命令工作流或仓库边界是否变化 → 唯一 `AGENTS.md`
6. 入口门禁、路由或授权边界本身是否变化 → 本 `SKILL.md` 与配对入口（不含受保护区）

判断为不需要更新的情况：只有时间戳变化；早于 `next_eligible_check_at` 且无新外部信号；事实可从源码、测试、README、主档案或 Git 恢复；只是本轮过程、截图或“本轮结论”；下一步列表语义未变。

### 需要时再写

- 先重新读取将被更新的当前文件，检查精确重复、语义重复和过期冲突。
- 直接替换过期状态、blocker 和下一步；禁止按日期追加。
- `recovery-state.md` 只保存不能从源码恢复的阶段、阻塞、检查点和最小下一步；Cursor 与 Codex 读同一份。
- 主档案只沉淀已经做过的需求事实；README 只保留与具体需求无关的通用配置、架构与部署事实。没有这类变化时不更新。
- 不把业务规则、字段、测试数量、部署 ID、验收流水写进 Skill 或快照。
- 别人合并进来的大规模结构变化，Cursor 使用 `/init-project`，Codex 使用 `/initProject`；不得创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- “最新待继续问题(不要修改这部分的子内容)”由用户维护；除非用户明确授权，否则保持标题、位置和子内容原文。已确认完成的条目不自动重做，只有用户本轮重新点名时才执行。
- 早于时间门禁且无新信号时，最终写明“项目阶段和业务下一步未变”。

最终回复必须说明：本次判断是否需要更新、实际更新了哪些文件或全部未变，以及当前最小下一步。默认不列出加载文件清单。

## 项目学习过程(当此模块里有未注释的内容时,表示当前执行的是`学习当前项目的所有代码和配置`的相关任务,每次这种任务执行完之后,你都应该更新此模块的`正在学习的内容`和`已经学习的内容`,下次我继续学习当前项目时,可以知道正在学习什么,已经学了什么)
- 项目学习计划:
  - 从本地 prod 启动开始学。它是整条运行链路的入口：命令、env 文件、Next.js 进程和数据库在这里汇合。先看懂进程怎么起来，再顺着页面、API、领域逻辑和数据模型往下读。不要一上来通读 `项目主档案.md` 或市场研究。
  - 学习时只读代码和配置。`pnpm run prod:dev` 会连 prod 数据库，页面上的登录、保存和开通会写入 prod；未明确要求时不启动这条命令，也不改数据。
  - 每一章读完要能回答该章的「学完标准」，再进入下一章。当前 release 的主路径优先；支付、AI chat 留到后面，避免把遗留资产当成正在上线的功能。
  - 第 0 步，读地图，约一次会话的开头，不单独记为已学完的一章：
    - `README.md` 的「环境」「常用命令」「架构」「运行时入口」「部署」。
    - `package.json` 的 `scripts` 与依赖。
    - 顶层目录：`src/app`、`src/components`、`src/lib`、`prisma`、`e2e`、`scripts`、`content`。
  - 第 1 章，从这里开始：本地 prod 启动。
    - 读 `package.json` 里的 `dev`、`dev:verify`、`prod:verify`、`prod:build`、`prod:dev`、`prod:start`。
    - 读 `scripts/prod-dev.ts`、`scripts/verify-env.ts`、`next.config.ts`。
    - 对照 README 分清三件事：`pnpm dev` 用 `.env.local` 连 dev 库；`pnpm run prod:dev` 把 `.env.production.local` 注入后再跑 `next dev`，`NODE_ENV` 仍是 `development` 以便热更新，`APP_ENV` 来自 prod env；`pnpm run prod:build` 后再 `pnpm run prod:start` 才是本地 `next start` 的 production build。
    - 学完标准：能说出两条本地 prod 命令分别在什么时候用、env 谁覆盖谁、为什么改 `NEXT_PUBLIC_*` 必须重新 build，以及这条链路为什么会碰到 prod 数据。
  - 第 2 章：请求进应用之后先经过什么。
    - `src/app/layout.tsx`，以及三个路由组：`(marketing)`、`(auth)`、`(app)` 各自的 `layout.tsx`。
    - `src/components/providers/`、`src/lib/site.ts`、`src/lib/features.ts`、`src/lib/prisma.ts`、`instrumentation.ts` 与 `sentry.*.config.ts`。
    - 学完标准：能指出公开页、登录页、登录后页面各从哪个 layout 进来，以及当前 release 里 AI chat 开关在哪里关掉。
  - 第 3 章：按真实用户顺序读页面，先页面再点进它调用的组件。
    - `/`：`src/app/(marketing)/page.tsx` 与 `src/components/marketing/`。
    - 登录：`src/app/(auth)/sign-in/page.tsx`、`src/components/auth/`、`src/app/auth/continue`。
    - 开通与计划：`src/app/(app)/onboarding/page.tsx`、`progress/page.tsx`、`day/[day]/page.tsx`、`completion/page.tsx`，以及 `src/components/onboarding/`、`day-plan/`、`completion/`、`feedback/`。
    - 其余公开页：`support`、`legal/*`、`blog/[slug]`、`chat` 暂停页、checkout success/cancelled。
    - 学完标准：能不看文档画出「落地页 → 登录 → onboarding → progress → 某一天 → 完成」这条路径，并标出每步的页面文件。
  - 第 4 章：登录与开通背后的服务端。
    - 认证：`src/lib/auth/`、`src/app/api/auth/`。
    - Onboarding 与开通：`src/app/api/onboarding/`、`src/app/api/checkout/route.ts`、`src/lib/onboarding/`、`src/lib/billing/purchase-service.ts`、`src/lib/program/provisioning-service.ts`。
    - 学完标准：能说明 magic link 如何经 `/auth/continue` 完成，以及当前 release 如何在 onboarding 之后开通 14 天计划，而不是先走付费收银台。
  - 第 5 章：14 天计划怎么跑。
    - `src/app/api/program/` 与 `src/lib/program/`：当前计划、当天练习、完成条件、完成报告、内容从哪里来。
    - `content/` 与 `src/lib/content/blog.ts` 只在读到对应页面时再看。
    - 学完标准：能指出「勾选练习」和「完成当天」分别打到哪个 service，以及服务端在什么条件下才允许完成 Day。
  - 第 6 章：数据库。
    - `prisma/schema.prisma`，按使用顺序看：`User`、`Account`、`Session`、`VerificationToken`、`RecoveryProfile`、`Purchase`、`Program`、`ProgramDay`，然后再看 `MarketingMetricAggregate`。
    - `ChatConversation`、`ChatMessage`、`KnowledgeDocument`、`KnowledgeChunk`、`StripeWebhookEvent` 留到第 7 章。
    - 学完标准：能说出一条用户从注册到完成某一天，会写下哪些表，以及 dev / prod 为什么必须是两套库。
  - 第 7 章：仓库里仍在、但不是当前 release 主路径的代码。
    - 付费遗留：`src/lib/billing/`、`src/app/api/creem/`、`src/app/api/stripe/`、checkout 回跳页。
    - AI chat 暂停资产：`src/app/api/chat/`、`src/lib/chat/`、`src/app/(app)/chat/page.tsx`。
    - 学完标准：能把「当前免费开通」和「以后可能恢复的 Creem / Stripe / AI」分开，不把暂停或 legacy 路由写成现在的产品行为。
  - 第 8 章：测量、隐私、观测、SEO、定时任务。
    - `src/lib/analytics/`、`src/components/analytics/`、`src/components/privacy/`、`src/app/api/analytics/`、`src/app/api/cron/analytics-retention/`。
    - `src/lib/observability/`、`src/lib/seo/`、`scripts/submit-indexnow-once.ts`、`vercel.json`。
    - 学完标准：能说明哪些事件可以进聚合、什么身份能看 summary、opt-out 和 90 天清理在哪里，以及线上部署是 GitHub `main` 到 Vercel Production。
  - 第 9 章：用测试把前面各章对上。
    - `e2e/` 与 `playwright.config.ts`，对照 `package.json` 的 `qa:launch`。
    - 学完标准：能指出登录、计划入口、analytics、观测、Stripe/Creem webhook 各自有哪份测试，以及哪些测试故意不打真实外部服务。
- 正在学习的内容:
  - 第 1 章。`pnpm run prod:dev` 启动到服务器 Ready 的文件链已经讲完。下次逐段读 `scripts/prod-dev.ts` 怎么注入 env；`next.config.ts` 的配置项还没逐项讲。`scripts/verify-env.ts` 不在这条启动链路里。
- 已经学习的内容:
  - 2026-09-23：只核对了目录、启动脚本和 README 工程入口，用来写出上面的大纲。
  - 2026-09-23：讲完 `package.json` 的顶层字段、`engines`、全部 `scripts`、`dependencies` 与 `devDependencies`。`zustand` 只出现在依赖清单里，当前 `src` 没有引用。
  - 2026-09-23：讲完 `pnpm run prod:dev` 启动到 Ready 的项目文件链：`package.json` → `scripts/prod-dev.ts` → 读取 `.env.production.local` → 启动 `next dev` → 加载 `next.config.ts` → 执行 `instrumentation.ts` → 在 Node 运行时加载 `sentry.server.config.ts`。Next 还会读取 `.env.local` 和 `.env`，已经注入的同名变量保持优先。`scripts/verify-env.ts`、`sentry.client.config.ts`、`sentry.edge.config.ts` 和 `src/app/` 页面不在 Ready 之前执行。 

## 最新待继续问题(不要修改这部分的子内容)
<!-- - 借鉴`/Users/stark/.codex/skills/csx-web-react/SKILL.md`,优化当前skill,让每次执行完当前项目相关的任务后,先判断是否需要在当前skill里或者相关文档里更新项目的最新状态和下一步需要做的任务列表,以及沉淀项目的事实,如果需要,再这么做;用于新chat里恢复上下文 -->
<!-- - 精简优化`/Users/stark/Desktop/work/MyStartupProject1/项目主档案.md`和`/Users/stark/Desktop/work/MyStartupProject1/README.md`,项目主档案只沉淀项目里已经做过的所有需求的事实,而`README.md`只保留和具体需求无关的通用的项目配置和架构与部署事实 -->
<!-- - 在prod环境里清除`stark19852020@gmail.com`这个账户,我需要重新测试这个账户 -->
<!-- - 本轮任务执行完毕后,你把当前项目里修改的前后端代码和数据库都重新部署到prod环境 -->
<!-- - 你从真实的prod环境的首页`https://fracturerecoverycoach.com/`开始重新全面手动进行Production 环境全链路验收项目里的每个页面是否正确; -->
  <!-- - 全面检查你测试到的页面显示的数据有没有错误,是否符合这个账号的数据库数据和 api 返回的数据 ,API 是否正确,发现问题你直接修正;如果页面里有需要填写或点击的交互,你直接操作,并检查交互后的前后端逻辑是否正确,如果不正确,直接修改;保证这个页面的显示UI逻辑,交互逻辑,API逻辑,数据库逻辑等所有功能逻辑都验证通过后,在 `/Users/stark/Desktop/work/MyStartupProject1/项目主档案.md`沉淀这个页面已经在 Prod 环境验证通过;然后继续测试和这个页面有关的下个页面;所有页面你都回归测试完成后,再把当前项目推动到 市场推广阶段 -->
<!-- - 你现在开始进行市场推广、真实用户反馈和转化指标观察阶段 -->
