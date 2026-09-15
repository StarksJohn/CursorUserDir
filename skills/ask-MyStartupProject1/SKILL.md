---
name: ask-MyStartupProject1
description: >-
  MyStartupProject1 私有恢复、BMAD 总控与市场推广持续执行入口。仅在用户显式使用
  /ask-MyStartupProject1 或 @ask-MyStartupProject1，或明确要求恢复项目阶段、继续
  BMAD/市场推广检查点时使用。每个新 chat 先调用本入口；随后强制读取 Codex 对口
  Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-MyStartupProject1

## 调用策略与边界

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/MyStartupProject1/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\MyStartupProject1\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得用摘要或项目根副本替代。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md`、当前源码与聚焦测试开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只补充无法安全放进仓库的阶段状态、BMAD/市场推广门禁、外部阻塞和受保护待办。
- 用户给出具体任务时，该任务优先于受保护待办；只有仅调用入口或明确要求“继续”时，才解析未注释待办并从第一个未完成门禁续跑。
- 普通一次性任务优先在新 chat 第一条消息中同时写 `/ask-MyStartupProject1` 和任务正文；只有需要跨 chat、跨设备或长周期恢复时，才把任务放入本文件受保护区后仅输入入口词继续。
- Cursor 入口 `/ask-MyStartupProject1` 与 Codex 显式入口 `$MyStartupProject1` 保持事实优先级、授权边界和恢复语义一致，但不复制客户端专属说明。项目名、工作区路径或仓库名本身不触发本入口。
- 医疗内容保持教育、陪伴、记录和安全提醒定位；不得表述为诊断、确定治疗方案或医生替代。生产写操作、账户清理、付款、数据迁移和破坏性操作必须有明确用户授权，并先用只读检查解析精确目标。

## 路径与事实优先级

- 项目根：macOS `/Users/stark/Desktop/work/MyStartupProject1`；Windows `D:/work/MyStartupProject1`。
- Codex 对照入口：macOS `$HOME/.codex/skills/MyStartupProject1/SKILL.md`；Windows `%USERPROFILE%\.codex\skills\MyStartupProject1\SKILL.md`。
- 已完成需求与稳定产品边界：`<项目根>/项目主档案.md`。
- Story / Epic 状态：`<项目根>/stories/sprint-status.yaml`。
- 工程、命令、环境、构建、数据库和部署：当前源码、`package.json`、配置与相关 `README.md` 章节。
- 市场推广假设、渠道、漏斗、阈值和停止条件：`<项目根>/market-overseas-user-acquisition-and-conversion-research-2026-08-11.md` 的完成版。
- 私有阶段、外部阻塞和最小下一步：仅在继续待办、阶段判断或市场推广检查点时读取 Codex 对照目录 `references/recovery-state.md`。
- 方向筛选、完整生命周期、文档命名和低频模板：仅在需要时读取同目录 `reference.md`。

冲突按以下优先级处理：

1. 当前源码、聚焦测试、真实 DOM / Network / API / Production 响应和当前 Git 状态。
2. Codex 对口 Skill 同目录 `AGENTS.md`、`package.json` 与相关 `README.md` 章节。
3. 用户本轮明确授权或需求来源。
4. 按需读取的主档案、Sprint 状态、市场研究文档与恢复快照。
5. 本文件受保护区块中的历史兼容待办。

快照用于恢复，不替代实时核验。开发状态以 `sprint-status.yaml` 为准；最新执行入口以恢复快照的最小下一步为准。

## 执行工作流

1. 先判断本轮是具体任务还是“继续项目”类恢复请求；具体任务不得被无关待办覆盖。
2. 读取 Codex 对口 Skill 同目录 `AGENTS.md` 和任务直接相关文件；不要通读 README、主档案、市场研究全文、恢复快照或历史附件。
3. 仅在任务依赖已完成需求、产品边界或 Story 状态时读取 `项目主档案.md` 或 `sprint-status.yaml`。
4. 仅在继续待办、判断当前阶段、处理外部阻塞或续跑市场推广时读取 `references/recovery-state.md`。阶段为 `market-promotion` 且正在续跑时，再读市场研究文档的 frontmatter、`Research Synthesis` 与实验阈值；不要重复已完成的研究步骤。
5. 执行 BMAD 或其它专项 Skill 前，完整读取其入口与必需依赖。磁盘存在、历史摘要或上一轮已读，不等于当前 chat 已加载。
6. UI、网页和生产问题先读真实页面、DOM、Network 与直接相关代码；能从真实页面取得 API 请求和响应时，不先用 Swagger 推断。
7. 代码任务依次完成仓库实现、聚焦测试，再进入文档维护判断；未完成前两段时不改 Skill、快照或主档案。
8. 生产发布必须区分前端、API、数据库和部署证据；即使数据库结论是“无 schema 变化”“already in sync”或受外部访问阻塞，也要单独说明。不把恢复快照当成实时 Production 证据。
9. 最终明确区分静态校验、本地运行、Production 核验和外部平台确认，不扩大成功范围。不输出 token、Cookie、密码、私钥、数据库 URL 或部署凭证。
10. 任务收尾先判断是否需要更新恢复状态、下一步列表和项目事实；只有判断为需要时才写入。详见「文档维护」。

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

- 只有真正按某个 `bmad-*` 工作流产出时才加载它。执行前读取 `~/.cursor/skills/<bmad-identifier>/SKILL.md` 或 `%USERPROFILE%/.cursor/skills/<bmad-identifier>/SKILL.md`，再读取其中要求的附属文件。
- 开始单 Story 循环前，读取主档案、Sprint 状态、`epics.md`、目标 Story、上一条相关 Story 和真实代码锚点。
- 子 Skill 的 `review` 与本项目 `code-review` 冲突时，以 `sprint-status.yaml` 为准。
- Epic 1-7 和 Story 1.1-7.4 已完成；除非用户批准新范围，不要因为总控路由自动创建新 Story。重新进入开发时串行 `create-story -> dev-story -> code-review -> done`。详细循环、阶段定义和回退映射见 `reference.md`。
- 当前已完成既有开发 Story 和 Production 全链路验收，处于市场推广执行；普通测量、推广修复和增长验收不要回到方向筛选，除非真实用户证据推翻核心需求或定位。

## 市场推广持续执行

当 `project_phase` 为 `market-promotion`，且用户要求“继续”“开始推广”“直到完成”或只调用本入口而没有更具体任务时，从恢复快照中第一个未完成门禁继续执行，不要只复述计划或等待逐步输入 `C`。

- 持续推进直到形成 go/hold/stop 闭环，或达到已核验且需外部状态变化才能恢复的明确阻塞。不得把单个渠道动作、暂无数据或时间门禁写成任务完成。
- 渠道边界：不在 X 推广；Reddit 不是唯一渠道；当前非 Reddit 公开路径为 LinkedIn；owned SEO 与搜索发现继续作为已上线入口。新增账号、社区、付费渠道、权限连接，或超出 Story 8.3 的开发范围，先取得对应授权。
- 状态机按序推进，发现实现或 Production 问题时回退到最近的代码、测试或发布阶段：`research-complete` -> `measurement-ready` -> `production-verified` -> `campaign-live` -> `observation-active` -> `decision-complete`。
- 完成条件：Production 声明与隐私漏斗已验证；真实合规获客可审计；观察阈值或停止条件已满足；最终指标、风险与下一步已记录；无未处理 P0/P1。不得把 mock、开发者访问、测试账号、自动化流量或免费注册写成真实用户、自然搜索或付费意愿。
- 禁止诊断、疗效保证、14 天痊愈、虚假临床背书、虚假评价和基于健康状态的再营销。
- `next_eligible_check_at` 只节流同一固定指标，不暂停整个推广任务。用户要求“现在继续”时，立即转向当前授权范围内第一个不依赖未来时间的真实动作。
- 立即动作顺序：修复 Production/隐私/测量回归；完成已批准但未上线的 owned SEO 或技术发现；执行尚未完成的一次性搜索发现；准备或执行已授权渠道动作；最后才新增测量能力。需要代码时先做影响分析，并按 `create-story -> dev-story -> code-review -> release` 建立有边界的 Story。
- 当前 UTC 早于该时点时，不重复查询同一 summary、Search Console、DNS、Production API 或 Vercel 日志，不重写仅时间戳变化的文档，也不触发 docs-only 部署。不得用 `sleep`、忙轮询、测试账号、重复 IndexNow 或虚构反馈制造信号。
- 登录态推广写操作两阶段交接：Cursor 只读确认账号、受众、精确目标和写入范围；密码、验证码、身份资料保存和平台要求的最终公开发布由用户完成，随后 Cursor 只读核验。会话过期时停在精确登录页，不回显敏感值。
- 社区或社交招募不要反复泛问“是否继续”。先只读核对登录态和当日规则，再给出唯一平台、允许动作、maker 披露、次数、禁止项和停止条件的授权包；未接受则记为 `external-authorization-required`。

## 文档维护

只要本轮执行了 MyStartupProject1 相关任务，代码、测试或验证闭环后、最终回复前，必须先判断是否需要落盘，再按判断结果写入。目的是让新 chat 只靠入口恢复当前阶段、阻塞、下一步和已沉淀事实，而不是每轮追加聊天流水。

本入口的新 chat 恢复面是 Codex 对照目录 `references/recovery-state.md`（最新状态与下一步）和仓库内 `项目主档案.md`（已完成需求事实）。不要把这些内容重新复制进本 `SKILL.md`，也不要每轮改受保护区。

### 先判断

对照本轮已验证结果与将要改的当前文件，逐项判断是否变化；全部为否时不写文件：

1. 当前阶段、外部阻塞、推广检查点或最小下一步是否变化 → `references/recovery-state.md`
2. 已完成需求、稳定产品边界或长期业务事实是否变化 → `项目主档案.md`
3. 与具体需求无关的工程、命令、架构、环境或部署事实是否变化 → `README.md`
4. Story / Epic 状态是否变化 → `stories/sprint-status.yaml`
5. 稳定架构、命令工作流或仓库边界是否变化 → Codex 对口 `AGENTS.md`
6. 入口门禁、路由或授权边界本身是否变化 → 本 `SKILL.md`（不含受保护区）

判断为不需要更新的情况：只有时间戳变化；早于 `next_eligible_check_at` 且无新外部信号；事实可从源码、测试、README、主档案或 Git 恢复；只是本轮过程、截图或“本轮结论”；下一步列表语义未变。

### 需要时再写

- 先重新读取将被更新的当前文件，检查精确重复、语义重复和过期冲突。
- 直接替换过期状态、blocker 和下一步；禁止按日期追加。
- `recovery-state.md` 只保存不能从源码恢复的阶段、阻塞、检查点和最小下一步；Cursor 与 Codex 读同一份。
- 主档案只沉淀已经做过的需求事实；README 只保留与具体需求无关的通用配置、架构与部署事实。没有这类变化时不更新。
- 不把业务规则、字段、测试数量、部署 ID、验收流水写进 Skill 或快照。不因历史付费、AI 或白名单代码资产仍在仓库，就默认把它们重新纳入当前 release。
- 别人合并进来的大规模结构变化使用 Cursor `/init-project` 刷新；不得创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- “最新待继续问题(不要修改这部分的子内容)”由用户维护；除非用户明确授权，否则保持标题、位置和子内容原文。已确认完成的条目不自动重做，只有用户本轮重新点名时才执行。
- 早于时间门禁且无新信号时，最终写明“项目阶段和业务下一步未变”。

最终回复必须说明：本次判断是否需要更新、实际更新了哪些文件或全部未变，以及当前最小下一步。默认不列出加载文件清单。

## 最新待继续问题(不要修改这部分的子内容)
<!-- - 借鉴`/Users/stark/.codex/skills/csx-web-react/SKILL.md`,优化当前skill,让每次执行完当前项目相关的任务后,先判断是否需要在当前skill里更新项目的最新状态和下一步需要做的任务列表,以及沉淀项目的事实,如果需要,再这么做;用于新chat里恢复上下文 -->
<!-- - 精简优化`/Users/stark/Desktop/work/MyStartupProject1/项目主档案.md`和`/Users/stark/Desktop/work/MyStartupProject1/README.md`,项目主档案只沉淀项目里已经做过的所有需求的事实,而`README.md`只保留和具体需求无关的通用的项目配置和架构与部署事实 -->
<!-- - 在prod环境里清除`stark19852020@gmail.com`这个账户,我需要重新测试这个账户 -->
- 本轮任务执行完毕后,你把当前项目里修改的前后端代码和数据库都重新部署到prod环境
<!-- - 你从真实的prod环境的首页`https://fracturerecoverycoach.com/`开始重新全面手动进行Production 环境全链路验收项目里的每个页面是否正确; -->
  <!-- - 全面检查你测试到的页面显示的数据有没有错误,是否符合这个账号的数据库数据和 api 返回的数据 ,API 是否正确,发现问题你直接修正;如果页面里有需要填写或点击的交互,你直接操作,并检查交互后的前后端逻辑是否正确,如果不正确,直接修改;保证这个页面的显示UI逻辑,交互逻辑,API逻辑,数据库逻辑等所有功能逻辑都验证通过后,在 `/Users/stark/Desktop/work/MyStartupProject1/项目主档案.md`沉淀这个页面已经在 Prod 环境验证通过;然后继续测试和这个页面有关的下个页面;所有页面你都回归测试完成后,再把当前项目推动到 市场推广阶段 -->
- 你现在开始进行市场推广、真实用户反馈和转化指标观察阶段
