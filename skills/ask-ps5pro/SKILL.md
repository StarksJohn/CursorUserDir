---
name: ask-ps5pro
description: >-
  Cursor：PS5 Pro 项目与资料库的会话入口；name 为 ask-ps5pro，口令 /ask-ps5pro。
  用于恢复当前项目上下文、读取项目 context.md 与规则、收敛 PS5 Pro 相关咨询/资料整理/购买决策/使用排障任务，
  并与 Codex 侧 /ps5pro 保持同一执行流程。工作区为 Windows `D:\work\ps5 pro` 或 macOS
  `/Users/<你的用户名>/Desktop/work/ps5 pro`（当前 Mac：`/Users/stark/Desktop/work/ps5 pro`）。
---

# ask-ps5pro（Cursor）

## 与 Codex 入口（分别维护）

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-ps5pro\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-ps5pro/SKILL.md`（当前 Mac：`/Users/stark/.cursor/skills/ask-ps5pro/SKILL.md`） | `ask-ps5pro` | `/ask-ps5pro` |
| Codex（对照入口） | **Windows** `%USERPROFILE%\.codex\skills\ps5pro\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/ps5pro/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/ps5pro/SKILL.md`） | `ps5pro` | `/ps5pro` |

两份文件分别维护，但入口目标、必读顺序、上下文门禁、`context.md` 归档规则与任务验收口径必须保持一致。通过 Cursor 输入框执行 `/ask-ps5pro`，或在 Codex / Cursor 内 Codex 插件输入 `/ps5pro`，应获得同一任务执行效果。

## 目的

本 skill 是当前 **PS5 Pro** 项目的默认分析入口，用于在新 chat 或跨工具切换时恢复项目事实、收敛任务范围，并避免只凭旧记忆或未加载文件行动。

- **恢复项目上下文**：新会话优先读取项目根 `context.md`，再读项目规则、锚点文件与任务直接相关材料。
- **收敛任务范围**：把用户输入框、本文件与 Codex 对照入口的「当前活跃需求」未注释条目合并为验收范围；用户明确裁剪时以用户裁剪为准。
- **适配 PS5 Pro 任务**：覆盖官方信息核对、价格/库存/保修/政策确认、游戏体验与设置排障、资料整理、截图/网页内容分析等。
- **保证上下文完整**：若入口又指向其它 skill、ask、command、BMAD 工作流、网页、图片或项目文档，须先判断当前 chat 是否已实际读取；缺失则补读后再执行。
- **沉淀项目结论**：需要跨 chat 保留的事实、决策、资料来源与未完成项，优先追加到 `{workspace}/context.md`，不得只留在对话里。

## 何时使用

- 用户显式 `@ask-ps5pro`、`/ask-ps5pro`，或自然语言提及 ask-ps5pro / PS5 Pro 项目入口。
- 当前工作区根目录为 **Windows** `D:\work\ps5 pro` 或 **macOS** `/Users/<你的用户名>/Desktop/work/ps5 pro`（当前 Mac：`/Users/stark/Desktop/work/ps5 pro`）。
- 任务涉及 PS5 Pro、PlayStation 5 Pro、主机购买/对比、配件、游戏兼容与增强、显示设置、账号/订阅、保修、售后、官方网页或截图资料整理。
- 用户未指定文件，但明显在本项目内工作时，优先按本 skill 的加载顺序取上下文。

## 工作区与路径

| 用途 | Windows | macOS |
|------|---------|--------|
| 工作区根（默认） | `D:\work\ps5 pro` | `/Users/<你的用户名>/Desktop/work/ps5 pro`（当前 Mac：`/Users/stark/Desktop/work/ps5 pro`） |
| 项目上下文归档 | `D:\work\ps5 pro\context.md` | `/Users/<你的用户名>/Desktop/work/ps5 pro/context.md` |
| 本 Cursor skill | `%USERPROFILE%\.cursor\skills\ask-ps5pro\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-ps5pro/SKILL.md` |
| Codex 对照 skill | `%USERPROFILE%\.codex\skills\ps5pro\SKILL.md` | `/Users/<你的用户名>/.codex/skills/ps5pro/SKILL.md` |
| Cursor skills 根 | `%USERPROFILE%\.cursor\skills` | `/Users/<你的用户名>/.cursor/skills` |
| Cursor 应用数据 | `%APPDATA%\Cursor` | `~/Library/Application Support/Cursor` |
| Codex 配置与 skills 根 | `%USERPROFILE%\.codex` | `/Users/<你的用户名>/.codex` |
| Codex 全局规则 | `%USERPROFILE%\.codex\AGENTS.md` | `/Users/<你的用户名>/.codex/AGENTS.md` |

下文 `{workspace}` 均指当前 IDE 实际打开的项目根；不要把 `.cursor` 或 `.codex` 用户目录误当成业务项目根。若用户明确给出 fork、迁移路径或临时路径，以用户指定路径为准。

## 新会话必读顺序

进入 `/ask-ps5pro` 后，按以下顺序读取；只有当前 chat 中已经实际读取成功的文件才能跳过。

1. **本 skill**：入口目标、路径规则、上下文门禁、归档规则与当前活跃需求处理方式。
2. **Codex 对照 skill（存在则读）**：`/ps5pro` 的同一入口事实源，尤其是必读顺序、门禁与「当前活跃需求」解释。
3. **项目 `context.md`**：`{workspace}/context.md`。若文件为空或仅有说明头，说明「暂无历史归档」；若已有条目，先概括与本轮问题最相关的近期条目。
4. **项目规则与锚点（存在则读）**
   - `{workspace}/AGENTS.md`
   - `{workspace}/.cursor/rules/project-context.mdc`
   - `{workspace}/README*`
   - `{workspace}/package.json`（若本项目后续变成代码仓库）
5. **任务直接相关文件 / 图片 / 网页**：只读与用户问题或「当前活跃需求」对应的资料、截图、链接、说明文档或代码；不要默认全目录扫描。

## 当前 chat 上下文加载门禁

- **入口恢复自检**：执行主任务前，必须确认本 `SKILL.md`、Codex 对照 `SKILL.md`、`{workspace}/context.md`、以及实际存在且任务相关的项目规则已读取或已明确缺失。
- **双入口一致性自检**：若 `/ask-ps5pro` 与 `/ps5pro` 在路径表、必读顺序、路由或活跃需求解释上冲突，以更具体、更新且更贴近当前工作区的条目为准，并在最终回复说明取舍。
- **子 skill 自检**：下一步若执行任意其它 skill、ask、command、BMAD 工作流或专项模板，先检查当前 chat 是否已读取该 skill 的 `SKILL.md` 及其要求的 `workflow.md` / `checklist.md` / `reference.md` 等；缺失则按 **Windows** `%USERPROFILE%\.cursor\skills\<id>\` / **macOS** `/Users/<你的用户名>/.cursor/skills/<id>/` 精确补读。
- **BMAD 硬门禁**：执行任意 `bmad-<identifier>` 前，必须先读取对应 `SKILL.md` 及同目录依赖文件。
- **图片门禁**：任务引用 skill、ask、command、rule 或项目文档中的图片时，按引用源 `.md` 所在目录精确读取图片；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。
- **网页与时效信息门禁**：涉及当前价格、库存、促销、固件、官方规格、保修、订阅政策、游戏增强列表、发布日期或售后条款时，必须联网核对；优先 PlayStation / Sony 官方来源，其次再用可信零售商或媒体交叉验证，并标明查询日期。
- **任务结束汇报**：最终回复必须列出「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」。

## `context.md` 归档规则

当本轮任务对 PS5 Pro 项目产生可复查结论、资料来源、购买/设置决策、待办或文件变更时，结束前追加到 `{workspace}/context.md`：

- 只写可复查事实：做了什么、关键结论、来源链接或本地路径、后续项。
- 不写密钥、账号 Cookie、订单隐私、完整日志或大段网页原文。
- 默认新条目追加在文件尾部，历史条目不静默改写；若需更正旧结论，新起一条说明「更正」。

推荐条目格式：

```markdown
---

### YYYY-MM-DD — 简述标题

- **触发**：用户诉求一句。
- **结论/交付**：可复查结论。
- **涉及路径/来源**：`path` 或 URL。
- **后续**：无 / 待办。
```

## 路由规则（关联 skills）

名称与 **Windows** `%USERPROFILE%\.cursor\skills` / **macOS** `/Users/<你的用户名>/.cursor/skills` 下目录一致。路由到某 skill 后，必须按上文门禁读取该 skill 及依赖。

| 场景 | Skill / 处理方式 |
|------|------------------|
| 初始化或刷新项目规则 | `init-project`（Cursor）/ `initProject`（Codex） |
| 当前网页、登录态页面、官方页面读取 | 优先按全局规则检查并使用 `chrome-devtools`；不可用时使用浏览器/网络检索并说明限制 |
| 代码仓库化后的代码审查 | `code-review` / `bmad-code-review` |
| 文档结构化、资料归档 | 先读 `context.md` 与相关 `.md`，必要时再路由 `bmad-document-project` |
| Cursor / Codex / MCP 配置问题 | `ask-cursor` 或 `codex` |
| 中英文案和术语 | `chinese-english-translation` |

## 执行工作流

1. 确认当前工作区或用户指定路径，并用双平台路径表理解当前机器路径。
2. 按「新会话必读顺序」读取最小必要上下文；缺失的项目规则或锚点要明确说明。
3. 合并用户输入框、本 Cursor skill 与 Codex 对照 skill 的「当前活跃需求」未注释项，形成验收清单。
4. 对时效性或官方信息先核对来源；对本地资料先读精确路径；对图片先按引用源目录读图。
5. 需要子 skill、BMAD、模板或网页自动化时先补读依赖，再执行。
6. 需要长期保留的结论追加到 `{workspace}/context.md`，并在最终回复说明。

## 输出约定

- 面向用户使用 **简体中文**；路径、命令、产品名、代码标识保持原文。
- 引用网页或官方信息时给出来源链接与查询日期。
- 不向 skill、`context.md` 或对话写入真实密钥、Cookie、订单隐私或账号敏感信息。
- 任务结束必须包含「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」。

## 边界

- 不把未联网核对的价格、库存、政策或发布时间当成当前事实。
- 不把非官方传闻当成官方规格；必要时标注「传闻 / 媒体报道 / 官方确认」。
- 不擅自购买、下单、登录账号或修改账号设置；需要用户确认后再给可执行步骤。
- 除非用户明确要求，默认不创建额外 `.md` 或脚本。

## 当前活跃需求(不要修改这部分的子内容)

- 本 Cursor 入口的当前活跃需求与 Codex 对照入口 **`/ps5pro`** 同步；执行 `/ask-ps5pro` 时必须读取 **Windows** `%USERPROFILE%\.codex\skills\ps5pro\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/ps5pro/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/ps5pro/SKILL.md`）中的「当前活跃需求」，再与用户输入框任务合并为本轮验收范围。
