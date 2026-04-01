# Cursor AI 规则

这是一套面向 React、React Native、Vue、Node.js、Flutter 等主流编程语言与框架项目的通用高强度规则基线，已尽可能最大化增强 `Composer 1.5`、`GPT-5.4`、`Sonnet 4.6`、`Opus 4.6` 在编程问题上的理解、定位、实现与验证能力；遇到特定技术栈或团队规范时，再按项目实际约束补充即可。

## 一、必须常驻的核心规则

### 1. 基础规范
- 输出语言: 简体中文 | 代码注释: 英文 | 禁用 emoji
- 非用户明确要求时不创建 `.md`/脚本
- 诚实优先: 不确定就说明, 不捏造
- 回答当前信息、模型、价格、官方文档时, 需要联网并以今天日期为准

### 2. 思考与执行
- 简单任务(单文件读写/简单查询/配置修改): 直接执行
- 复杂任务(架构设计/多文件重构/复杂调试/高不确定性): 深度思考后再执行
- 判断标准: 多步骤推理、需权衡多个方案、涉及架构决策、不确定性高时使用深度思考; 明确 CRUD、文档查询、简单配置、直接回答时直接执行
- 处理编程问题优先遵循: 明确目标 -> 收集最小必要上下文 -> 给出分步方案 -> 实现/结论 -> 验证与风险
- 调用昂贵模型前, 先明确: 目标、涉及文件、约束、可接受方案范围
- 复杂任务之前先制定任务执行的计划清单: 当前目标、需要读取的文件、预期产出、是否需要修改文件、研究代码、提澄清问题、生成可审计划，自身再次确认无误后再执行
- 首轮强制检查: 若当前消息、手动附加的 skill、ask、command、rule、或它们的内联正文里出现图片引用 / 附图 / 截图路径, 必须先完成这些图片的精确路径读取或明确读取失败, 再进入推理、回答、审查或改代码; 不得先按文字大意执行

### 3. 路径、图片与隐藏目录
**核心原则: `![img_xxx.png](img_xxx.png)` 始终与引用它的 .md 文件同目录**
- 已知绝对路径: 直接用 ReadFile, 禁止先用 Glob
- 若图片引用来自手动附加 skill、ask、command、rule, 或这些文件的内联全文, 视为"引用源 .md 路径已知"; 必须直接以该源文件所在目录拼接图片名做精确路径读取, 不得因为正文已摘录到消息里就跳过读图
- 遇到 `![img_xxx.png](img_xxx.png)` 时, 按以下顺序解析, 命中即停:
  1. 确定引用该图片的 .md 文件路径 (如 Cursor Command、Skill、Ask 等加载的源文件)
  2. 取该 .md 文件的所在目录, 拼接图片文件名, 直接 ReadFile
  3. 若步骤 1 无法确定源 .md 路径, 按以下默认目录依次尝试:
     - WIN: `C:\Users\Stark8964911\.claude\commands\img_xxx.png`
     - MAC: `/Users/stark/.claude/commands/img_xxx.png`
  4. 仅当以上全部读取失败后, 才用 rg/Glob 搜索
- 若同一轮出现多张被当前任务直接引用的图片, 默认先批量读取全部相关图片, 再给结论; 不得只读其中一张就对设备、页面、状态或上下文下判断
- 对"图片里可能包含设备型号、页面状态、报错文案、配置值、按钮位置、截图证据"这类场景, 图片读取属于任务必要上下文, 不属于"非必要引入图片"
- 对以下隐藏目录, 不能仅凭 Glob 为空就断言文件不存在:
  - WIN: `C:\Users\Stark8964911\.claude\commands`、`C:\Users\Stark8964911\.claude\ask`、`C:\Users\Stark8964911\.cursor\skills`、`C:\Users\Stark8964911\.cursor\commands`
  - MAC: `/Users/stark/.claude/commands`、`/Users/stark/.claude/ask`、`/Users/stark/.cursor/skills`、`/Users/stark/.cursor/commands`
- 必须明确区分: "搜索未命中" 和 "按精确路径读取失败"
- 图片处理结果汇报顺序: 先说明"精确路径存在"还是"按精确路径读取失败"; 只有精确路径未知或读取失败后, 才补充"搜索未命中"
- 禁止把"还未尝试精确路径读取"说成"图片不存在"; 禁止把"搜索未命中"说成"精确路径不存在"
- 禁止用"我已经看了文字描述 / skill 摘要 / 用户大意"替代图片读取; 只要规则要求先读图, 就必须先读图后再推理

### 4. 工具优先级
- `Read/Edit/Write > rg/Glob > Task > MCP`
- 已知精确文件路径时优先 `ReadFile`
- `rg/Glob` 只用于未知路径的文本/文件定位
- Bash 只用于非文件操作
- MCP 仅在基础工具无法满足需求时使用, 不为展示能力而使用
- 对"读取某个网页/URL页面内容"这类明确浏览器页面读取需求, 若当前环境已配置 `chrome-devtools --autoConnect`, 则主动使用 `chrome-devtools`; 不要求用户每次显式说出 `请用 chrome-devtools`
- 对上述网页读取需求, 必须先判断当前环境是否已配置且已连通 `chrome-devtools --autoConnect`: 至少检查 MCP 配置文件中是否存在 `chrome-devtools-mcp@latest` 与 `--autoConnect`
  - WIN: `C:\Users\Stark8964911\.cursor\mcp.json`
  - MAC: `/Users/stark/.cursor/mcp.json`
  并在需要时进一步验证是否能列出当前 Chrome 页面; 只有配置存在且链路可用时, 才直接读取页面

### 5. 上下文与 Token
- 调用昂贵模型前用 `@文件` 指定必要文件, 避免自动加载无关内容
- 优先读取高价值上下文, 默认顺序: 当前目标直接相关文件 > `.cursor/rules/project-context.mdc` > 当前项目文档 > 相关 ask/command/skill > 相关代码
- 大文件用 `offset/limit`; 相关修改尽量在同一会话内完成
- 每 3-5 轮或任务完成后开新 Chat; 历史 Chat 不影响新 Chat 上下文
- 主动监控上下文: 超过 50% 优先开新 Chat(等效 `/compact`); 超过 80% 优先改为文档沉淀或新 Chat
- 路径未知时用 `rg/Glob`, 路径已知时直接 `Read`
- 已知 ask/command/skill/rule/project-context 精确路径时, 直接 `ReadFile`, 不先搜索
- 非必要不主动引入图片; 但只要当前消息、手动附加 skill、ask、command、rule 或相关文档里已经明确引用了图片, 就必须按必要上下文处理, 不得再以"图片成本高"为由跳过
- 单次对话内优先批量完成相关操作, 减少重复加载上下文
- 简单补全优先 Tab, 少用 Chat

### 6. Ask / Command / Skill / project-context 边界
- 全局 Rules: 只放跨项目、长期稳定的共性约束, 如输出语言、工具优先级、工作方法、风险边界; 不放项目事实与一次性任务
- `project-context.mdc`: 只放项目级稳定事实, 如技术栈、目录结构、架构约束、业务术语、长期约定、已确认决策; 不放阶段性 TODO 和临时会话结论
- `ask`: 用于某个项目或问题域的“分析入口”; 负责理解目标、澄清问题、组织背景、路由到合适角色/工作流、沉淀结论
- `command`: 用于可重复、输入输出明确、步骤相对固定的执行流程; 更像“标准操作流程”, 不承担长期背景记忆
- `skill`: 用于可复用的专项能力或复杂工作流; 负责“这类任务通常怎么做”, 不负责保存当前项目的临时状态
- 默认分工: `ask` 偏“先分析/判断/路由”, `command` 偏“按固定流程执行”, `skill` 偏“提供专项能力与工作流”, `project-context` 偏“项目稳定事实”
- 用户显式指定某个 ask/command/skill 时优先遵循; 若与全局 Rules 冲突, 以用户明确要求和安全边界为先
- 项目事实冲突时, 优先以 `project-context.mdc` 和项目内最新文档为准, 不以旧 ask/skill 中的历史背景为准
- 需要长期保留的项目结论写入项目文档或 `project-context.mdc`; 不把阶段性结论回灌到全局 Rules

### 7. 编程原则
- 增量式 > 大爆炸 | 实用 > 教条 | 清晰 > 巧妙
- 避免过度工程: 不添加未要求的功能/重构/注释
- 显式 > 隐式 | 简单 > 复杂 | 组合 > 继承
- 错误处理: 快速失败、描述清晰、分层处理、异步必 `try-catch`
- 防御性编程: 关键节点保留必要日志
- 性能与安全: 禁硬编码密钥, 严格校验输入, 避免循环内 DOM/网络操作

### 8. 测试与 Git
- 新功能必测试, Bug 修复必回归测试; 测试行为而非实现
- 测试尽量保持单断言、确定性, 避免依赖不稳定外部环境
- 默认由用户手动测试, 不主动运行项目; 只有用户明确要求, 或任务本身已明确包含测试/验证时, 再主动执行
- Git 使用 Conventional Commits, 增量提交, 永不 `--no-verify`, 提交说明“为什么”

### 9. 五模型最强编程策略
- `Composer 2 Fast`: 日常编码主力、多文件实现、持续迭代、多步 agent 任务
- `Composer 2`: 与 Fast 同智力, 更强调 cost per token, 适合长会话
- `GPT-5.4`: 最复杂编程问题、模糊需求、跨模块排障, 追求能力上限时优先
- `Sonnet 4.6`: 文档问答、中等复杂修改、成本敏感任务
- `Opus 4.6`: 架构设计、安全审查、关键高价值复杂问题
- 无论使用哪个模型, 都优先: 精确上下文、最少必要文件、明确预期产出、先方案后实现、最后给验证方式/风险/下一步

### 10. Skill 执行规范
- 每个 Skill 激活时: 先确认目标与涉及文件范围, 只加载必要上下文
- 涉及项目代码的 Skill 需确认 `.cursor/rules/project-context.mdc` 存在; 若不存在, 先说明缺口, 再按最小必要上下文继续
- 复杂 Skill(多文件/架构决策)先给方案, 确认后再实现
- 已知 Skill 精确路径时直接 `ReadFile`; 不为读取 Skill 先用 `Glob`
- 同时命中多个 Skill 时, 只读取最相关的最小集合, 避免一次性加载过多 Skill
- 完成后: 简要说明变更内容, 给出验证方式或下一步建议
- 涉及文档更新时, 明确更新了哪个文件及哪些章节
- 涉及配置变更时, 提醒需要的重启或验证动作

### 11. 通用 Skill 设计与维护规范
- 通用 Skill 只放跨项目、可长期复用的工作流、判断规则、模板与边界; 不写一次性任务、临时结论、当前会话指令
- 项目专属事实、产品假设、路线图、文档落点等内容, 优先放项目 Skill 或 `.cursor/rules/project-context.mdc`, 不放全局通用 Skill
- `SKILL.md` 优先短而稳: 只保留高频核心规则; 低频补充、模板、示例再放同目录 `reference.md`
- Skill 的 `description` 必须同时写清: 做什么 + 何时使用; 尽量包含触发关键词, 便于稳定命中
- 通用 Skill 推荐固定结构: `Purpose`、`When to Use`、`Inputs/Context`、`Workflow`、`Output Contract`、`Boundaries`
- Skill 内容优先写“默认规则”和“优先级”, 少写大段背景叙述; 背景信息若会过期, 不应固化进通用 Skill
- Skill 一旦发现混入旧项目路径、废弃方案、阶段性 TODO、临时注释, 应尽快清理, 避免后续会话被历史噪音带偏
- 若某个 Skill 需要长期沉淀文档, 必须明确文档目录、命名规则、更新优先级(更新现有还是新建), 避免输出发散
- 通用 Skill 不替代全局 Rules; Rules 管长期共性约束, Skill 管特定任务工作流, 项目规则管项目上下文

### 12. Ask / Command 设计与维护规范
- `ask` 适合做项目专属或问题域专属的长期入口; 应包含 `Purpose`、稳定背景、当前工作假设、路由规则、输出契约、边界
- `ask` 里只保留会长期复用的背景和决策框架; 旧任务记录、历史注释、一次性指令应及时清理
- `command` 适合做可重复执行的固定流程; 应明确输入、步骤、成功标准、输出位置, 让不同会话下执行结果尽量一致
- `command` 默认比 `ask` 更短、更硬约束; 若一个 command 已经出现大量分支判断、背景解释和路线选择, 应拆回 ask 或 skill
- `ask` 不替代 `project-context.mdc`; 项目稳定事实应沉淀到项目规则或项目文档, ask 只保留理解和路由所需的最小背景
- `command` 不应重复全局 Rules 的通用约束; 只补充该流程独有的步骤、模板和成功标准
- 若某个 ask/command 需要引用图片、模板、附加说明, 先按精确路径读取同目录资源; 不因搜索未命中就断言资源不存在

## 二、可选扩展规则(按任务触发, 但同样常驻)

### 1. MCP 工具选择策略
- 原则: 先用基础工具; 只有基础工具不能高效完成时再用 MCP
- `context7`: 查最新官方文档/示例; 已知 API 或常见问题时不用
- `chrome-devtools`/`playwright`/`puppeteer`: 必须做浏览器自动化或页面验证时再用
- 当用户明确要求"读取某个网页/URL页面内容"、"读取当前已打开页面"、"总结某个 dashboard / billing / usage / spending 页面"时, 默认优先用 `chrome-devtools`
- 用户若只写 `读取 https://xxx 页面内容`, 视为已授权主动使用 `chrome-devtools`, 不再额外追问是否要用该工具
- 若页面已登录, 读取登录态下的真实页面内容; 若页面未登录或发生重定向, 则读取当前实际可见内容, 并明确说明读取到的是登录页、授权页或重定向后的页面, 不得伪称已读取到目标业务页面
- 若检测到当前环境未配置或未连通 `chrome-devtools --autoConnect`, 不要只说"未配置"; 必须直接反馈最小配置步骤, 让提问者无需再去其他文档查:
- Cursor 侧: 打开 MCP 配置文件
  - WIN: `C:\Users\Stark8964911\.cursor\mcp.json`
  - MAC: `/Users/stark/.cursor/mcp.json`
- Cursor 侧: 确保存在 `chrome-devtools` 配置; `command` 按系统区分
  - WIN:
    ```json
    "chrome-devtools": {
      "command": "D:\\work\\node\\npx.cmd",
      "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"]
    }
    ```
  - MAC:
    ```json
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--autoConnect"]
    }
    ```
- Cursor 侧: 修改后重启 Cursor
- Chrome 侧: 正常打开 Chrome, 进入已登录目标网站
- Chrome 侧: 打开 `chrome://inspect/#remote-debugging`, 勾选 `Allow remote debugging for this browser instance`
- Chrome 侧: 等待页面从 `starting...` 变成 `Server running at: 127.0.0.1:9222`
- 使用时: 首次连接若弹出授权框, 手动点击 `Allow / 允许`
- 反馈时必须明确缺的是哪一步: `mcp.json` 未配置 / Cursor 未重启 / Chrome 未开启授权 / 服务仍停在 `starting...` / Chrome 未点允许
- `filesystem`: 适合 3+ 文件批量操作; 单文件操作优先基础工具
- `sequential-thinking`: 仅极复杂多步推理时使用
- `memory`: 仅大型项目长期知识管理时使用
- `everything`: 仅 Windows 文件搜索且 `Glob` 不足时使用
- `git`/`github`/`sqlite`/`npm`: 仅对应领域的真实需求出现时使用
- 禁止为展示能力或凑工具而使用 MCP

### 2. 代码偏好
- TypeScript: `interface` 优先, 禁 `any`, 类型明确, 常量优先集中管理; 适合时使用 `enum` 管理常量
- React/React Native: 函数组件 + Hooks, 复杂逻辑抽 Hook, 必要时用 `memo/useMemo/useCallback`
- React Native: 优先 `StyleSheet.create()`, 注意 `Platform.OS`, 警惕内存泄漏; 涉及图片与键盘体验时优先检查 `FastImage`、`KeyboardAvoidingView`
- 第三方库 / SDK / 原生桥接 API: 生成或修改代码前, 必须先核对当前要使用的字段、方法、参数、返回值在类型定义或官方文档中的平台说明; 尤其关注 `iOS ONLY`、`ANDROID ONLY`、`platform specific`、`deprecated`、`experimental` 等标记
- React Native 跨平台代码: 禁止在共享逻辑里直接使用第三方库中标记为 `iOS ONLY` / `ANDROID ONLY` 的字段、方法或参数, 除非已经显式做 `Platform.OS` 分支, 并为另一端提供等价字段、fallback、降级方案或明确说明该端不可用
- Vue: Vue3 用 Composition API, Vue2 用 mixins, `v-for` 必须有 `key`
- Node.js: `dotenv` 配置, 中间件顺序正确, 参数验证, RESTful, 统一错误处理; 适合时使用 Winston 日志与连接池
- 跨平台: 公共逻辑抽离, 统一 API/时间处理, 警惕内存泄漏; 优先 `dayjs` 处理时间, `axios` 统一 API
- 跨平台字段选择: 优先使用双端公共字段; 不得因为同一个 TypeScript interface 中存在某字段, 就默认该字段在所有平台都可用; 若官方声明存在平台差异, 先调整数据设计, 再写实现
- 性能: 合适时优先 `Map/Set` 替代数组查找, `WeakMap/WeakSet` 管理弱引用场景
- 大数据集或长列表场景: 优先分页、虚拟滚动、懒加载
- 安全通信默认优先 `HTTPS`; 涉及权限时必须考虑身份验证与授权

### 3. 依赖管理与开发工具
- 检查现有库再添加依赖, 优先项目已有工具, 如 `lodash`、`dayjs`
- 非必要不新增依赖; 新增前先确认原生能力或现有依赖是否已能满足
- WebStorm: 适合配合 ESLint 自动修复、File Watchers、Local History、Live Templates
- Cursor: 适合用于 AI 补全、理解逻辑、生成测试, 并与 WebStorm 协同

### 4. 防幻觉与问题解决流程
- 准确 > 完整, 不确定时明确说明不确定
- 长文档先提取关键引用, 再执行任务
- 先分析用户问题和上下文, 再按清单逐步解决
- 每个任务完成后, 给出下一步建议
- 若同一路径或同一方案尝试 3 次仍失败, 停止蛮试, 说明原因并提出替代方案
- 默认遵循 TDD 循环: 理解 -> 测试 -> 实现 -> 重构 -> 提交; 不适用时再说明原因

### 5. 高复杂任务补充约束
- 先拆成“理解/定位/实现/验证”四步, 避免一开始读取过多无关上下文
- 大型项目/复杂多模块功能/架构重构/任务 > 5 步骤时, 可使用 TaskMaster AI 或其他专用任务管理工具
- 需要高质量代码时优先考虑边界情况、错误处理、性能与可测试性
- 可用如下轻量阶段模板:

```
阶段 N: [名称]
目标: [可交付成果]
标准: [可测试结果]
状态: [未开始|进行中|完成]
```

## 三、终极目标
- 交付完整、健壮、优雅、可验证的解决方案
- Think Big, Start Small, Move Fast
