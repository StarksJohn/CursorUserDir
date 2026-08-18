---
name: ask-MyStartupProject1
description: >-
  Cursor：MyStartupProject1 项目入口、BMAD 总控与市场推广持续执行器。用于恢复项目、
  路由产品/开发/测试/发布任务，并在 market-promotion 阶段从第一个未完成门禁继续推进
  隐私漏斗、Production 验收、合规获客、真实反馈和增长决策，直到形成可核验的
  go/hold/stop 闭环。用户消息含 /ask-MyStartupProject1、要求继续该项目或市场推广、
  当前工作区为 D:/work/MyStartupProject1 或 $HOME/Desktop/work/MyStartupProject1 时使用。
---

# ask-MyStartupProject1

## 路径与事实源

- 项目根：Windows `D:/work/MyStartupProject1`；macOS `/Users/<你的用户名>/Desktop/work/MyStartupProject1`，当前 Mac 为 `/Users/stark/Desktop/work/MyStartupProject1`。
- Cursor 入口：Windows `%USERPROFILE%/.cursor/skills/ask-MyStartupProject1/SKILL.md`；macOS/Linux `~/.cursor/skills/ask-MyStartupProject1/SKILL.md`。
- Codex 对照入口：Windows `%USERPROFILE%/.codex/skills/MyStartupProject1/SKILL.md`；macOS/Linux `~/.codex/skills/MyStartupProject1/SKILL.md`。两侧分别维护，但阶段、事实源、工作流边界和最小下一步应一致。
- 已完成需求、稳定产品边界和业务状态：以 `<项目根>/项目主档案.md` 为准。
- Epic / Story 状态：以 `<项目根>/stories/sprint-status.yaml` 为准。
- 技术栈、命令、环境、构建、数据库和部署方式：以项目源码、`package.json`、配置与 `README.md` 为准。
- 当前阶段、最新生产结论、外部阻塞和最小下一步：以本 Skill 的“项目状态恢复快照”为准。
- 当前市场推广假设、渠道、漏斗、实验阈值和停止条件：以 `<项目根>/market-overseas-user-acquisition-and-conversion-research-2026-08-11.md` 的完成版为准。
- 文档命名、写入优先级和低频产出模板：仅在需要时读取同目录 `reference.md`。

发生冲突时，当前源码、测试和真实运行证据优先于历史文档；开发状态以 `sprint-status.yaml` 为准；最新执行入口以本 Skill 的最小下一步为准。快照用于恢复，不替代实时核验。

## 启用与最小读取顺序

用户消息含 `/ask-MyStartupProject1`、工作区是本项目或任务明确属于本项目时启用。

1. 完整读取本 `SKILL.md`。
2. 读取 `<项目根>/项目主档案.md` 和 `<项目根>/stories/sprint-status.yaml`。
3. 阶段为 `market-promotion` 时，读取市场研究文档 frontmatter、`Research Synthesis`、实验阈值和本 Skill 的推广检查点；不要重复执行已经完成的研究步骤。
4. 读取当前任务直接相关的项目规则、源码、测试、截图、配置和文档；不要批量加载无关资料。
5. 需要工程命令、环境或部署信息时，再读取 `package.json`、相关配置和 `README.md`。
6. 只有需要文档命名、写入优先级或低频产出模板时，才读取 `reference.md`。
7. 路由到任意 BMAD 或其它 Skill 时，先完整读取对应 `SKILL.md` 及其明确要求的附属文件。

若用户或相关文档引用图片，先按引用源文件所在目录解析并读取图片；读取失败后才搜索。不要以摘要、旧 chat、磁盘存在或上一轮已读代替当前会话实际读取。

## 实施工作流

1. 先确定任务属于回答、诊断、改动、发布还是项目规划，并确认是否需要修改文件或外部状态。
2. UI、网页和生产问题先读真实页面、DOM、Network 与直接相关代码；能够从真实页面取得 API 请求和响应时，不先用 Swagger 推断。
3. 代码任务按以下顺序闭环：
   - 项目内真实业务代码、配置或运行链路。
   - 定向回归、fixture、E2E、单元测试和必要测试文档。
   - 项目外 Skill、ask、恢复快照或其它状态文档。
4. 开发阶段优先运行单用例、单 viewport 或相关文件检查；阶段收尾再按风险扩大到 typecheck、lint、build 或完整回归。
5. 生产发布任务必须闭环前端、后端/API 和数据库结论；即使数据库结论是“无 schema 变化”“already in sync”或受外部访问阻塞，也要明确区分。
6. 生产事实必须用当前 Production 页面、真实 API、Vercel/Git 状态和数据库只读检查重新验证，不把本 Skill 的快照当成实时证据。
7. 不修改任务范围外的用户文件，不输出或写入 token、Cookie、密码、私钥、数据库 URL 或部署凭证。

## BMAD 路由与执行门禁

| 需求类型 | 优先入口 |
| --- | --- |
| 方向、用户、痛点、价值主张、go / no-go | `bmad-agent-analyst` |
| 市场规模、竞品、定价和商业信号 | `bmad-market-research` |
| 医疗、康复、患者旅程和领域术语 | `bmad-domain-research` |
| Product Brief、产品定义和 MVP 边界 | `bmad-product-brief` |
| 路线图、优先级、里程碑和发布范围 | `bmad-agent-pm` |
| 架构、技术方案和模块边界 | `bmad-agent-architect` |
| 单 Story 规格 | `bmad-create-story` |
| 功能实现、修复和部署 | `bmad-dev-story` 或 `bmad-agent-dev` |
| 测试策略和验收 | `bmad-agent-qa` 或 `bmad-qa-generate-e2e-tests` |
| 增量或发布前审查 | `bmad-code-review` 或 `code-review` |
| 实施准备 | `bmad-check-implementation-readiness` |
| Epic / Story 拆解 | `bmad-create-epics-and-stories` |

- 只有真正按某个 `bmad-*` 工作流产出时才加载它；泛泛讨论阶段或角色时不批量读取子 Skill。
- 执行前按当前系统读取 `~/.cursor/skills/<bmad-identifier>/SKILL.md` 或 `%USERPROFILE%/.cursor/skills/<bmad-identifier>/SKILL.md`，再读取其中要求的 `workflow.md`、`checklist.md`、`reference.md`、模板或输入发现文件。
- 开始单 Story 循环前，同时读取主档案、Sprint 状态、`epics.md`、目标 Story、上一条相关 Story 和真实代码锚点；不得只根据历史摘要生成规格或实现。
- 若子 Skill 使用 `review`，而本项目状态机使用 `code-review`，以 `sprint-status.yaml` 为准并说明差异。
- Epic 1-7 和 Story 1.1-7.4 已完成；除非用户批准新范围，不要因为总控路由自动创建新 Story。
- 重新进入开发时，默认串行执行 `create-story -> dev-story -> code-review -> done`；一条 Story 未闭环前不批量生成后续 Story，除非用户明确要求或确有并行开发需要。

## 生命周期与回退

默认生命周期为：

`方向筛选 -> 需求验证 -> 市场与竞品 -> 价值主张 -> go/no-go -> Product Brief -> MVP -> 技术方案 -> 实施准备 -> Story 拆解 -> 开发 -> 测试验收 -> 发布 -> 上线跟踪 -> 迭代决策`

- 关键上游前提未满足时，不强行推进下游。
- 用户、新证据、测试或生产结果推翻当前前提时，回退到最近一个能重新回答问题的阶段；后续产物受影响时明确标记为暂时失效。
- 当前项目已完成既有开发 Story 和 Production 全链路验收，处于市场推广执行；普通测量、推广修复和增长验收不要回到方向筛选，除非真实用户证据推翻核心需求或定位。
- 需要文档命名、写入优先级和低频产出模板时读取 `reference.md`；不要把低频模板重新复制进本入口。

## 市场推广持续执行

当 `project_phase` 为 `market-promotion`，且用户要求“继续”“开始推广”“直到完成”或只调用本入口而没有更具体任务时，直接从推广检查点中第一个未完成门禁继续执行，不要只复述计划或等待用户逐步输入 `C`。

按以下状态机串行推进；发现实现或 Production 问题时自动回退到最近的代码、测试或发布阶段修复：

1. `research-complete`：定位、渠道、漏斗、阈值和停止条件已落盘。
2. `measurement-ready`：健康声明与隐私审计、最小真实漏斗和结构化反馈已实现并测试。
3. `production-verified`：build、Git/Vercel、前端/API/数据库和真实 Production 事件链已验证；测试账号和内部流量不计入市场指标。
4. `campaign-live`：至少一个高意图内容入口和一个合规获客动作已真实上线，并记录受控 source/campaign。
5. `observation-active`：持续读取真实外部用户 Day 1/3/7/14、错误和结构化反馈；样本或时间未到时保持 active，不把“暂无数据”写成完成。
6. `decision-complete`：达到预注册样本与观察窗，或触发明确停止条件；形成有证据的 go/hold/stop 决策和下一迭代入口。

只有 Production 与隐私漏斗已验证、真实合规获客可审计、观察阈值或停止条件已满足、最终指标与风险已记录且无未处理 P0/P1 问题时，才标记市场推广完成。不得把 mock、开发者访问、测试账号、自动化流量或免费注册写成真实用户、自然搜索或付费意愿。

用户已明确授权市场推广时，可在研究文档允许的渠道范围内执行普通公开发布；需要新账号、付费、身份或医疗资质声明、接受平台条款、向具体个人发送消息、扩大敏感数据处理或新建超出 Story 8.3 的开发范围时，先取得对应授权。禁止诊断、疗效保证、14 天痊愈、虚假临床背书、虚假评价和基于健康状态的再营销。

### 时间门禁与轮询节流

- 当第一个未完成门禁只依赖未来时间、样本自然增长或平台异步处理时，在检查点写入精确 UTC `next_eligible_check_at`；它只控制固定复查时点，不改变原实验阈值。
- 当前 UTC 早于该时间，且没有新证据、Production 告警、平台通知或明确刷新要求时，不重复查询 Chrome、Search Console、DNS、Production API 或 Vercel 日志，不重写只有时间戳变化的文档，也不触发 docs-only 部署。
- 提前续跑时只核对本机时间、工作树和检查点自洽性；保持目标 active，明确这是时间门禁而非产品 blocker。不得用长时间 `sleep`、忙轮询、测试账号、开发者流量或重复 indexing request 制造信号。
- 时间到达或出现新外部信号后，从对应固定检查点恢复一次有边界的真实查询，并据实更新下一时间点。

## 项目与安全边界

- 医疗内容保持教育、陪伴、记录和安全提醒定位；不得表述为诊断、确定治疗方案或医生替代。
- 当前解释要清楚区分前端、服务端、数据库和部署证据，避免用单层验证替代全链路结论。
- 不因历史付费、AI 或白名单方案仍存在代码资产，就默认把它们重新纳入当前 release。
- 生产写操作、账户清理、付款、数据迁移和破坏性操作必须有明确用户授权，并先用只读检查解析精确目标。

## 文档维护与任务结束门禁

- 完成 MyStartupProject1 相关任务后，核对本 Skill 的恢复快照和最小下一步；只有阶段、生产基线、外部阻塞或长期工作流发生实质变化时才更新，不能按日期追加聊天流水。
- 项目代码任务必须先闭环业务实现，再补测试，最后才更新项目外的 Cursor/Codex Skill 或恢复文档；若验证又发现代码问题，先回到业务实现。
- 稳定需求事实、产品边界或业务下一步变化时，更新 `项目主档案.md`；不要每轮机械写“本轮结论”。
- 工程命令、架构、环境或部署方式变化时，更新 `README.md`；Story / Epic 状态变化时，更新 `stories/sprint-status.yaml`。
- 本 Skill 的快照只保存当前阶段、最近生产结论、当前阻塞、推广检查点和最小下一步；可从源码、测试、README 或主档案恢复的规则、字段、测试数量和历史流水不写入。
- 本 Skill 快照发生实质变化时，同步核对 Codex 对照入口的阶段、阻塞和最小下一步，避免两侧恢复结果冲突。
- “最新待继续问题”由用户维护；除非用户明确授权修改，否则保持标题及全部子内容原样。已确认完成的条目不自动重做，只有用户本轮重新点名时才执行。
- 最终回复默认只说明产出、验证、风险和下一步；仅在用户要求、审查/排障、上下文读取失败或慢任务复盘时列出加载文件清单。

## 项目状态恢复快照

### 当前阶段

- 项目为 `Fracture Recovery AI Companion`；`project_phase` 为 `market-promotion`。Epic 1-7 已完成；Epic 8 为 `in-progress`，Story 8.1-8.2 为 `done`，Story 8.3 为 `in-progress`。
- 市场研究、隐私安全第一方漏斗、Production 发布验证和首个高意图 SEO 入口均已完成；当前只继续真实聚合观察与证据受限的增长决策，不重新执行研究或 measurement 实现。

### Production 与推广检查点

- 生产入口为 `https://fracturerecoverycoach.com/`；发布路径为 GitHub `main` -> Vercel Production。市场实验运行时基线为提交 `e218aa1` / deployment `dpl_9jq8UqLbSxUsoSRB1QVhyXafTGbg`；最新状态文档提交 `5514c38` 的 docs-only deployment 已接管正式域名，未改变运行时。
- 当前 release 免费开通 14 天计划；真实付费 checkout 延后到 v2，AI recovery chat 暂停但保留底层代码资产。
- 当前状态为 `observation-active`；首个渠道是 `/blog/finger-stiff-after-cast-removal`，campaign 为 `stiffness_after_cast`。Search Console Domain Property 和 sitemap 已验证，目标文章已成功抓取但尚未编入索引；不得宣称已有排名或自然搜索流量。
- 观察窗从 `2026-08-13T04:29:00Z` 开始。截至 `2026-08-18T07:24:44Z`，相关 landing occurrence 为 1，同入口 CTA、activation、Day 1/3/7/14、feedback、safety 和 verified business outcomes 均为 0；error-level 与 5xx 查询均为 0。该 occurrence 可能含自动化流量，不代表唯一真实用户。
- 固定门禁：Day 7 为 `2026-08-20T04:29:00Z`，Day 14 为 `2026-08-27T04:29:00Z`；最终决策必须同时达到至少 14 天和至少 100 次相关 landing occurrence。少于 50 次只作定性记录；若 90 天保留边界先到且仍不足 100，只能 `hold` 或 `stop`。
- `next_eligible_check_at` 为 `2026-08-20T04:29:00Z`。在此之前，除非出现新证据、Production 告警、平台通知或用户明确要求刷新，不重复查询相同 API、日志、DNS 或 Search Console 状态。

### 当前阻塞与进入条件

- 当前没有已确认的 Production 故障，也没有触发立即停止条件；未达到时间和样本门禁是实验状态，不是代码 blocker。
- Reddit 社区推广需要逐社区核对规则并在必要时先获 moderator 许可；从个人 X 账号发布会产生公开身份和 maker 披露。未经明确授权，不发帖、不发消息、不登录或创建新账号、不接受新条款。
- analytics allowlist 尚无 Reddit 或 build-in-public 对应 source/campaign；新增来源、IndexNow 或其它推广代码属于 Story 8.3 既定 T5 之外的新范围，必须先授权、测试、发布和验证。
- 本地 `.env.production.local` 的数据库连接当前被 Supabase 拒绝，不能作为新的直连数据库证据；同期 authenticated operator API 可正常读取 Production 聚合，因此这不是线上故障。

### 最小下一步

1. 到 `2026-08-20T04:29:00Z` 后，查询 `2026-08-13` 至当天的 authenticated operator summary、aggregate-only Production counts、feedback/safety marginal counts 和 error/5xx 状态，记录 Day 7。
2. 同时复核 Search Console 目标文章状态与公开 exact-URL / `site:` 结果；未完成索引只记录为异步状态，不重复频繁提交 indexing request，也不把 `direct` 写成 organic search。
3. 如要启用社区或社交渠道，先获得 Story 范围和外部发布授权，增加经测试的 allowlist source/campaign pair，完成 Production 发布验证后再执行平台动作。
4. 到 `2026-08-27T04:29:00Z` 后记录 Day 14，并持续观察 50/100 次相关 landing occurrence；达到 Day 14 与 100 次后才评估 `go / hold / stop`。

## 最新待继续问题(不要修改这部分的子内容)
- 根据 `<项目根目录>` 目录下的 `<项目根目录>/项目主档案.md` 文档恢复这个项目的上下文，继续执行下一步的任务
