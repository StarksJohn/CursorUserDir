---
name: ask-MyStartupProject1
description: >-
  MyStartupProject1 私有恢复、BMAD 总控与市场推广持续执行入口。仅在用户显式使用
  /ask-MyStartupProject1 或 @ask-MyStartupProject1，或明确要求恢复项目阶段、继续
  BMAD/市场推广检查点时使用。每个新 chat 先调用本入口；随后强制读取 Codex 对口
  Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-MyStartupProject1

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/MyStartupProject1/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\MyStartupProject1\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md`、当前源码与聚焦测试开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 chat 首次激活时，在主任务前执行共享 `AGENTS.md` 的 “First-chat structural drift gate”；发现重大冲突时立即完整读取并执行 macOS `$HOME/.cursor/skills/init-project/SKILL.md` / Windows `%USERPROFILE%\.cursor\skills\init-project\SKILL.md`，刷新后重新读取共享 `AGENTS.md` 并继续原任务，不要求用户再次输入 `/init-project`。
- 本 Skill 只补充项目阶段、BMAD/市场推广状态机、外部阻塞和受保护待办。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才从未完成门禁续跑。

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

仅在用户显式使用 `/ask-MyStartupProject1` / `@ask-MyStartupProject1`，
或明确要求恢复项目阶段、继续 BMAD / 市场推广检查点时启用；项目名或工作区本身不触发。

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

### 当前全局任务

- 持续推进市场推广、真实用户反馈与转化观察，直到满足本节完成条件形成闭环，或达到已经核验且需要用户/平台外部状态变化才能恢复的明确阻塞；不得把单个渠道动作、暂无数据或时间门禁缩写成任务完成。
- 渠道边界固定为：不在 X 推广；Reddit 不是唯一渠道。当前非 Reddit 公开推广路径为 LinkedIn，owned SEO 与搜索发现动作继续作为已上线入口；新增其它账号、社区、付费渠道或权限连接仍按授权门禁处理。

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

### 时间门禁、轮询节流与立即推进

- 当第一个未完成门禁只依赖未来时间、样本自然增长或平台异步处理时，在检查点写入精确 UTC `next_eligible_check_at`；它只控制固定复查时点，不改变原实验阈值。
- `next_eligible_check_at` 不暂停整个市场推广任务。用户要求“现在继续”“不能等”或“直到完成”时，立即转向当前授权范围内第一个不依赖未来时间的真实动作，不要只核对时间后结束。
- 立即动作按顺序选择：修复 Production/隐私/测量回归；完成研究已批准但尚未上线的 owned SEO 或技术发现入口；执行尚未完成的一次性搜索发现动作；准备或执行已获授权且平台允许的渠道动作；最后才是新增测量能力。需要代码或新增范围时先做影响分析，并按 `create-story -> dev-story -> code-review -> release` 建立有边界的 Story。
- 当前 UTC 早于 `next_eligible_check_at` 时，不重复查询相同 summary、Search Console、DNS、Production API 或 Vercel 日志，不重写只有时间戳变化的文档，也不触发 docs-only 部署；但继续执行其它安全且已授权的真实推广动作。
- 不得用长时间 `sleep`、忙轮询、测试账号、开发者流量、重复 indexing request、重复 IndexNow 或虚构反馈制造信号。
- 若所有安全且已授权的立即动作均已完成，而剩余动作确实依赖外部登录、人工授权、平台异步结果或未来样本，则记录精确 blocker、已尝试链路和恢复后的唯一下一步，不把市场推广标记完成。新 chat 先重试该外部门禁，再考虑定时指标。
- 登录态推广写操作采用两阶段交接：Cursor 先只读确认账号、受众、精确目标和写入范围；密码、验证码、身份/职业资料保存及平台要求用户亲自完成的最终公开发布由用户操作，随后 Cursor 只读核验结果。会话过期时保留已完成的平台状态并停在精确登录页，不读取或回显 Cookie、session token、DNS 验证值等敏感值；恢复后从同一标签和未完成步骤继续。
- 当唯一可推进动作是社区或社交招募，但需要使用用户账号、公开 maker 身份或联系 moderator 时，先只读核对登录态和当日规则，再给出边界完整的授权包；只有用户明确接受后才创建渠道 Story、发送消息或发布。
- 当前 UTC 到达 `next_eligible_check_at` 或出现新外部信号后，从对应检查点恢复一次有边界的真实查询，并据实更新下一时间点。

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
- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
- 本 Skill 的快照只保存当前阶段、最近生产结论、当前阻塞、推广检查点和最小下一步；可从源码、测试、README 或主档案恢复的规则、字段、测试数量和历史流水不写入。
- 本 Skill 快照发生实质变化时，同步核对 Codex 对照入口的阶段、阻塞和最小下一步，避免两侧恢复结果冲突。
- “最新待继续问题”由用户维护；除非用户明确授权修改，否则保持标题及全部子内容原样。已确认完成的条目不自动重做，只有用户本轮重新点名时才执行。
- 最终回复默认只说明产出、验证、风险和下一步；仅在用户要求、审查/排障、上下文读取失败或慢任务复盘时列出加载文件清单。

## 项目状态恢复快照

### 当前阶段

- 项目为 `Fracture Recovery AI Companion`；`project_phase` 为 `market-promotion`。Epic 1-7 已完成；Epic 8 为 `in-progress`，Story 8.1-8.2 与 Story 8.4-8.7 为 `done`，Story 8.3 与 Story 8.8 为 `in-progress`。
- 研究、隐私安全第一方漏斗、Production 全链路、三条高意图 SEO 入口、Article JSON-LD、Search Console 请求、Reddit 归因与唯一版主许可申请、唯一 IndexNow batch、Bing/Spaceship 所有权验证、Day 7 authenticated checkpoint、用户授权的 2026-08-21 提前汇总和 Authorization C 的唯一 LinkedIn 公开帖均已完成。Authorization E 的 YouTube 归因代码、Production 零污染验证和原创长视频已完成，独立频道创建/上传/公开核验未完成。不使用 X，不重发 Reddit 申请、IndexNow batch、Bing 验证或 LinkedIn 帖子。

### Production 基线

- 生产入口为 `https://fracturerecoverycoach.com/`；发布路径为 GitHub `main` -> Vercel Production。Story 8.3 观察窗基线仍为提交 `e218aa1` / deployment `dpl_9jq8UqLbSxUsoSRB1QVhyXafTGbg`。Story 8.7 正式审查修复提交 `22a3744` 由 deployment `dpl_2J8w4aD4aexPbAMesb7zxvsrUZ2H` 精确构建并 Ready；server-only `/indexnow-key.txt`、三篇文章 200/self-canonical/sitemap/robots/单一 Article JSON-LD/安全免费文案、`www` 永久重定向和无污染 LinkedIn controlled URL 均通过真实 Production 验收，Prisma schema/migrations 未变化。
- 社交预览业务提交 `15da940` 已由 deployment `dpl_5gzrrzfiXAoGAc1RbPREwSc8cx8y` 精确构建并 Ready；三篇文章共用由 `force-static` ImageResponse route 生成的 apex `/share-card`，真实 HTML 的 Open Graph/Twitter image 无 query，PNG 为 200、`image/png`、1200×630、93,615 bytes，文案只表达免费教育支持且 clinician guidance 优先。
- Story 8.8 业务提交 `f9443863d3538884c41b45e4b35b1411a774af4d` 由 Production deployment `dpl_7nTViognkWs2ukDYS4k3kB8LUjDK` 精确构建并 Ready；只新增 `youtube:stiffness_after_cast` 受控 pair。公网拦截式 Playwright 1/1 通过，前后 authenticated operator summary 的 YouTube landing/CTA/entry 均为 0，Prisma schema/migrations 未变化。最新状态提交 `b5f761f5a1cb113adce8aa1c3d75148bdebb190a` 已推送，GitHub Production deployment 状态为 `success`；本地与 `origin/main` 相同且 `0 0` divergence，项目仓库 clean。
- 唯一 IndexNow POST 于 `2026-08-20T02:13:35.991Z` 发起、`02:13:37.926Z` 完成，global endpoint 返回 HTTP `202` / `validation-pending`，三条 URL 均为无 query 的 apex canonical，`attemptCount=1`。回执为 `stories/8-7-indexnow-submission-receipt.json`，不含 key；不得重试，也不得解释为抓取、收录、排名、流量或转化。
- 当前 release 免费开通 14 天计划；真实付费 checkout 延后到 v2，AI recovery chat 当前暂停但保留底层代码资产。

### 市场推广执行检查点

- 当前状态：`observation-active/accelerated-interim-read-recorded/linkedin-posted-public/reddit-permission-pending/youtube-channel-terms-user-gate`。Reddit 于 `2026-08-21T03:01:40Z` 只读复核时，私信归档仍只显示一条两年前的无关 Reddit Admin 安全通知，没有 `r/brokenbones` 版主回复且未重发；IndexNow 为 `validation-pending`；LinkedIn 为 `authorization-c/posted-public/verified`；Bing Webmaster Tools 为 `verified/ownership-complete`。旧文章 Search Console 为 `verified-crawled-indexing-pending`，两条新文章为 `discovery-requested-indexing-pending`。自然 `direct` 只表示无受控来源参数，不得写成 organic search。
- Search Console 的“网页会自动重定向”当前只有 `http://fracturerecoverycoach.com/` 一条示例；真实 Production 为一次 `308` 到 `https://fracturerecoverycoach.com/` 后返回 200，HTTPS 根页 URL Inspection 显示“网址已收录到 Google”和“网页采用 HTTPS 协议”。sitemap、canonical、Open Graph 与源码公共 origin 均只使用 HTTPS；这是预期 HTTP -> HTTPS canonicalization，不修改代码、不点击“验证修正情况”，也不解释为文章已收录或新增流量。
- 观察窗从 `2026-08-13T04:29:00Z` 开始。Day 1 截止为 0 次相关 landing occurrence；Day 3 截止为 1 次相关 landing、0 次同入口 CTA、0 activation、0 Day 完成、0 feedback、0 safety signal。该 landing 是非唯一 occurrence，可能含自动化流量，不是已验证真实用户。
- Day 7 authenticated aggregate 于 `2026-08-20T07:42:29Z` 返回 5 次 raw / 4 次 adjusted relevant landing。用户于 2026-08-21 明确授权一次提前汇总：`2026-08-13..2026-08-21` authenticated API 返回 HTTP 200、`private, no-store`，6 次 raw stiffness landing 排除 1 次已知 operator QA 后为 5 次 adjusted occurrence；相关 CTA、activation、Day 1/3/7/14、feedback、safety 与 verified business outcomes 全部为 0。截至 `2026-08-21T02:51:09Z`，观察窗 Vercel Production error-level 与 5xx 查询均为 0。这是提前中期读取，不是 Day 14；样本低于 50，只能定性记录。
- 全站同期为 11 次 landing / 1 次 CTA，9.1% 仅是站点背景，不能冒充 stiffness 实验转化率。已知 QA occurrence 只在分析中排除，不删除数据库聚合；修复后的最终 Production metadata/PNG 验收没有新增 analytics 请求。
- 固定门禁：Day 7 为 `2026-08-20T04:29:00Z`，Day 14 为 `2026-08-27T04:29:00Z`；50/100 次相关 landing occurrence 是动态检查点。最终决策必须同时达到至少 14 天与至少 100 次相关 landing occurrence；若 90 天保留边界先到且仍不足 100，只能 `hold` 或 `stop`。
- `next_eligible_check_at`：用户授权的唯一提前汇总已于 2026-08-21 完成；下一个固定 authenticated summary 时点仍为 `2026-08-27T04:29:00Z`。在新的外部信号、50/100 动态门禁或 P0/P1 事件出现前，不再重复读取同一 aggregate/logs；可只读监看 Reddit 许可回复和 LinkedIn 公开反馈。

### 当前阻塞与进入条件

- 当前没有已确认的 Production 故障，也没有满足立即停止条件；Day 7 与用户授权的 2026-08-21 提前汇总/日志查询均已完成，5 次 adjusted occurrence 且 0 下游结果仍不足以形成转化或增长结论。
- Authorization E 的最终原创上传资产为 `/Users/stark/Movies/Fracture Recovery Companion/finger-stiffness-after-cast-removal-free-recovery-companion-final.webm`，已验证 70.24 秒、1920×1080、VP8 WebM、无音轨且逐帧文字可读。YouTube account switcher 仍显示原 `Bignature` 频道未变；创建表单已填入 `Fracture Recovery Companion` 与 `@FractureRecoveryCompanion`，但点击“创建频道”会接受 YouTube 服务条款，必须由用户本人确认。确认前不得代点、上传到原频道或声称新频道已存在。
- 用户已明确给出 Authorization B：只允许当前登录 Reddit 账号以透明 maker 身份向 `r/brokenbones` moderator 发送至多一条 permission request，并仅在明确获批后发布一次。该许可申请已于 2026-08-19 发送且不得重发；X、`r/HandSurgery`、其它社区、跨社区复制、陌生用户私信、健康细节收集及诊断/疗效/结果声明继续禁止。
- LinkedIn Authorization C 已完成：用户确认当前公开身份/职业资料准确、人工粘贴并亲自发布唯一一帖。公开动态 `https://www.linkedin.com/feed/update/urn:li:share:7496122748025470979/` 于 `2026-08-20T08:37:36Z` 首次核验，`2026-08-21T03:01:40Z` 仍可直接读取；精确正文、controlled URL 和公开可见性均正确。当前显示 7 次平台展示、无可见公开评论或回应计数；这些不是独立用户、first-party landing 或转化。只读监看，不点赞、回复、私信、tag、boost、复制到 X 或重复发布；若评论含健康/身份细节，只做去身份化主题计数，不复制原文。
- Authorization D 已完成：只添加精确 Bing apex property 与 Bing 当页要求的一条 Spaceship CNAME。UI 由 10 项变为 11 项，原 A/`www` CNAME/MX/DMARC/Google verification/DKIM/SPF 均保留；两台权威 NS 都精确返回新 CNAME，Google DoH 的新记录与基线均为 NOERROR。Bing 明确显示 `Congratulations! Site addition successful`。未执行 GSC import/Domain Connect、sitemap/URL 提交、Clarity、付费或重复 IndexNow；不回显或保存验证值，也不重复验证。
- Chrome DevTools 已恢复且 Day 7 operator API 已读取；此前失败的本地/Vercel-injected Supabase 直连凭据不再重试，也不作为 Production 故障证据。任何 Network/会话核验都只输出必要的状态、计数和响应字段，不读取或回显 Cookie、Authorization、session token 或 DNS 验证值。
- Production 结论继续只来自 authenticated operator API、aggregate-only 数据库、live 页面/Network 与当前日志查询；不得把测试账号、QA 事件、搜索结果缺失或开发者访问写成用户转化。

### 最小下一步

1. 用户在当前 YouTube 创建对话框亲自点击“创建频道”接受平台条款，并回复“已创建”；这是恢复 Authorization E 的唯一立即门禁。
2. 恢复后先重开 account/channel switcher，证明活动频道精确为 `Fracture Recovery Companion` 且 `Bignature` 未变；再核验 feature eligibility。任何 phone/video/identity verification 由用户完成；之后只上传上述最终 WebM，填写 Story 8.8 的精确 title/description，设为非儿童、无付费推广、评论关闭、立即 Public，并停在最终公开确认前由用户亲点。发布后核验唯一公开 watch URL、可点击受控链接、设置与无重复上传。
3. 只读监看 `r/brokenbones` moderator 回复和已发布 LinkedIn 帖子的公开反馈；不重发、不互动、不保存身份/健康详情，也不把平台 occurrence 写成 first-party landing、用户或转化。
4. Story 8.3 的下一次固定 authenticated aggregate 读取仍为 `2026-08-27T04:29:00Z` Day 14，同时等待 100 次相关 landing；未来时间不阻塞上述已授权 YouTube 动作。若 90 天保留边界先到且仍不足 100，只能按证据 `hold` 或 `stop`。

## 最新待继续问题(不要修改这部分的子内容)
- 根据 `<项目根目录>` 目录下的 `<项目根目录>/项目主档案.md` 文档恢复这个项目的上下文，继续执行下一步的任务
