---
name: ask-mac
description: >-
  Cursor 侧 MAC 系统问题入口 skill；口令 /ask-mac。适用于 MacBook、macOS、
  Mac 维修/回收、Apple 官方支持、VPN/代理/Git 网络、Cursor 与 Codex 在 Mac 上的
  配置协作等问题。进入新 chat 时先恢复 MAC 工作区上下文文件
  `MAC系统相关问题解决方案.md`，并与 Codex 侧 `/mac` 保持同一文件加载顺序、
  上下文门禁、子任务补读规则与交付效果。
---

# ask-mac（Cursor）

## 与 Codex 入口（分别维护）

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-mac\SKILL.md`（本机示例：`C:\Users\Stark8964911\.cursor\skills\ask-mac\SKILL.md`） / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-mac/SKILL.md`（当前 Mac：`/Users/stark/.cursor/skills/ask-mac/SKILL.md`） | `ask-mac` | `/ask-mac` |
| Codex（对口入口） | **Windows** `%USERPROFILE%\.codex\skills\mac\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/mac/SKILL.md`（当前 Mac：`/Users/stark/.codex/skills/mac/SKILL.md`） | `mac` | `/mac` |

两份文件分别维护，但入口、必读顺序、上下文门禁、路由规则与任务验收口径必须保持一致。通过 Cursor 输入框执行 `/ask-mac`，或在 Codex / Cursor 内 Codex 插件输入 `/mac`，应获得同一任务执行效果。

## 目的

本 skill 是 **MAC 系统问题** 在 Cursor 侧的默认入口，用于在新会话或跨工具切换时把任务拉回 MAC 工作区事实与最小必要上下文。

- **恢复项目上下文**：新 chat 优先读取 `MAC系统相关问题解决方案.md`，把既有结论、未完成事项、路径与操作记录拉回当前上下文。
- **统一入口行为**：Cursor 输入 `/ask-mac` 与 Cursor 内 Codex 插件输入 `/mac` 时，必读顺序、上下文边界、活跃需求解释、输出口径保持一致。
- **收敛任务范围**：区分硬件/系统问题、维修/回收、Apple 官方信息、VPN/代理/Git 网络、Cursor/Codex 配置、文档更新等场景，按最小必要上下文推进。
- **路由专项能力**：若任务指向其它 ask、command、skill、BMAD、网页读取或图片资源，先补齐依赖文件，再执行。
- **合并待办来源**：除用户输入框外，本文件「当前活跃需求」及 Codex 对照入口 `/mac` 中未注释的「当前活跃需求」条目，均视为本轮须覆盖的验收范围；用户明确裁剪范围时以用户裁剪为准。
- **沉淀可复用结论**：需要长期保留的结论优先更新 `MAC系统相关问题解决方案.md`，不要新建零散 Markdown。

## 何时使用

- 用户显式输入 `/ask-mac`、`@ask-mac`，或自然语言点名 ask-mac / mac / MAC 系统问题。
- 当前工作区为 **Windows** `D:\work\MAC` 或 **macOS** `/Users/<你的用户名>/Desktop/work/MAC`（当前 Mac：`/Users/stark/Desktop/work/MAC`）。
- 任务涉及 MacBook、macOS、VPN/代理/GitHub 网络、Cursor Git、SourceTree、终端网络、Apple 支持、维修、回收、系统配置、Cursor/Codex 在 Mac 上的配置协作。
- 用户希望 Cursor 与 Cursor 内 Codex 插件中的执行效果对齐。

## 工作区与本 skill 路径

| 用途 | Windows | macOS |
|------|---------|--------|
| MAC 工作区根 | `D:\work\MAC` | `/Users/<你的用户名>/Desktop/work/MAC`（当前 Mac：`/Users/stark/Desktop/work/MAC`） |
| 项目上下文恢复文件 | `D:\work\MAC\MAC系统相关问题解决方案.md` | `/Users/<你的用户名>/Desktop/work/MAC/MAC系统相关问题解决方案.md`（当前 Mac：`/Users/stark/Desktop/work/MAC/MAC系统相关问题解决方案.md`） |
| README | `D:\work\MAC\README.md` | `/Users/<你的用户名>/Desktop/work/MAC/README.md` |
| 本 Cursor skill | `%USERPROFILE%\.cursor\skills\ask-mac\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-mac/SKILL.md` |
| Codex 对照 skill | `%USERPROFILE%\.codex\skills\mac\SKILL.md` | `/Users/<你的用户名>/.codex/skills/mac/SKILL.md` |
| ask 模板 | `C:\Users\Stark8964911\.claude\ask\ask.md` | `/Users/stark/.claude/ask/ask.md` |
| Cursor skills 根 | `%USERPROFILE%\.cursor\skills` | `/Users/<你的用户名>/.cursor/skills`（当前 Mac：`/Users/stark/.cursor/skills`） |
| Cursor 应用数据 | `%APPDATA%\Cursor` | `~/Library/Application Support/Cursor` |
| Codex 配置与 skills 根 | `%USERPROFILE%\.codex` | `/Users/<你的用户名>/.codex`（当前 Mac：`/Users/stark/.codex`） |
| Codex 全局规则 | `%USERPROFILE%\.codex\AGENTS.md` | `/Users/<你的用户名>/.codex/AGENTS.md`（当前 Mac：`/Users/stark/.codex/AGENTS.md`） |

若用户明确给出 fork、分支工作区或临时路径，以用户指定路径为准；否则按上表定位。下文 `{workspace}` 均指当前 IDE 实际打开的 MAC 工作区根；不要把用户目录下的 `.cursor`、`.codex` 或 `.claude` 路径误当成工作区根。

## 图片资源路径

本文中的 `![img_xxx.png](img_xxx.png)` 视为与本文件同目录：**Windows** `%USERPROFILE%\.cursor\skills\ask-mac\`；**macOS** `/Users/<你的用户名>/.cursor/skills/ask-mac/`（当前 Mac：`/Users/stark/.cursor/skills/ask-mac/`）。读取图片时须按引用源 `.md` 所在目录精确拼接文件名；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。

## 新会话必读顺序（恢复上下文）

新 chat 或首次进入 MAC 工作区任务时，按以下顺序读取；已在当前 chat **实际 Read 成功**的文件可不重复读，但不能只凭文件名、打开标签页、历史摘要或用户粘贴片段假设已加载。

1. **本 skill**：入口目标、路径规则、路由、上下文门禁与「当前活跃需求」。
2. **Codex 对照 skill（存在则读）**：**Windows** `%USERPROFILE%\.codex\skills\mac\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/mac/SKILL.md`，用于核对 `/ask-mac` 与 `/mac` 的必读顺序、上下文门禁与活跃需求解释是否一致。
3. **ask 模板**：**Windows** `C:\Users\Stark8964911\.claude\ask\ask.md` / **macOS** `/Users/stark/.claude/ask/ask.md`。
4. **MAC 工作区上下文恢复文件**：`{workspace}/MAC系统相关问题解决方案.md`。新 chat 必读；文件较长时先读目录、最近章节与当前任务相关章节，文件较短时读全文。
5. **项目锚点（存在且相关时读）**：`{workspace}/README.md`、`{workspace}/AGENTS.md`、`{workspace}/.cursor/rules/project-context.mdc`、日志或配置说明等。
6. **任务直接相关文件与素材**：用户输入框或两侧「当前活跃需求」引用的截图、网页、票据、命令输出、配置文件、日志文件、同目录图片。
7. **最新外部事实**：维修政策、Apple 官方说明、回收平台规则、门店营业信息、价格、工具文档、网络服务状态等可能变化的信息，必须基于当天联网核对后再下结论。

若精确路径读取失败，先说明失败路径，再按最小可用上下文继续，或请用户附上对应文件。

## 当前 chat 上下文加载门禁（必读）

- **入口恢复自检**：通过 `/ask-mac` 进入后，执行任务前须已实际读取本 `SKILL.md`、Codex 对照 `SKILL.md`、ask 模板、`{workspace}/MAC系统相关问题解决方案.md` 或已明确缺失。
- **双入口一致性自检**：若 `/ask-mac` 与 `/mac` 的路径表、必读顺序、路由或活跃需求解释出现冲突，以更具体、更新且更贴近当前工作区的条目为准，并在最终回复说明取舍。
- **活跃需求合并**：把用户输入框任务、本 Cursor skill 与 Codex 对照 skill 的「当前活跃需求」未注释条目合并为本轮验收范围；用户明确裁剪范围时，以用户裁剪为准。
- **任务相关文件自检**：列出本步必须依赖的文件或素材（截图、网页、日志、配置、解决方案章节、命令输出等），逐项判断是否已在当前 chat 读取；未读则先按精确路径读取。
- **子 skill 自检**：下一步若执行任意其它 skill（含 `bmad-*`、`code-review`、`init-project`、`ask-cursor` 等）、ask、command、BMAD 工作流或专项模板，须判断当前 chat 是否已读取该 skill 的 `SKILL.md` 及其要求的 `workflow.md` / `checklist.md` / `reference.md` 等；缺一则按 **Windows** `%USERPROFILE%\.cursor\skills\<id>\` / **macOS** `/Users/<你的用户名>/.cursor/skills/<id>/` 或对应 Codex skill 精确补读后再执行。
- **BMAD 硬门禁**：执行任意 `bmad-<identifier>` 前，必须先 `ReadFile` 对应 `SKILL.md` 及同目录依赖文件。
- **图片门禁**：任务引用 skill、ask、command、rule 或项目文档中的图片时，先精确路径读图，再推理；读取失败后再搜索，并明确区分「精确路径读取失败」与「搜索未命中」。
- **网页读取门禁**：用户要求读取网页、当前浏览器页面、dashboard、billing、usage、spending 等页面时，优先按全局规则检查并使用可用的 `chrome-devtools --autoConnect`；不可用时说明缺口和最小排查步骤。
- **任务结束汇报**：最终回复须列出「当前 chat 已加载的关键文件」与「本轮新增读取/加载的文件」；只列对判断、修改或验证有实际影响的项。

## 路由规则（关联 skills / 子任务）

名称通常对应 **Windows** `%USERPROFILE%\.cursor\skills` / **macOS** `/Users/<你的用户名>/.cursor/skills` 或 **Windows** `%USERPROFILE%\.codex\skills` / **macOS** `/Users/<你的用户名>/.codex/skills` 下目录。路由到某 skill 后，必须按上文「子 skill 自检」补读该 skill 全文及依赖后再执行。

| 场景 | 推荐入口 |
|------|----------|
| Cursor 设置、插件、MCP、Rules、Codex 插件行为 | `ask-cursor`、Codex 侧 `/codex` |
| Codex 用户目录、`AGENTS.md`、`config.toml`、skills 维护 | Codex 侧 `/codex` |
| 初次整理某个业务仓库项目规则 | `init-project` / Codex 侧 `initProject` |
| 需要浏览器自动化读取页面 | `chrome-devtools` 可用时按全局 MCP 规则执行 |
| 代码审查或专项工作流 | 对应 `code-review` / `bmad-*`，先补读 skill 及依赖 |

## 当前 Mac VPN / 代理优先级（2026-08-11 复核）

1. Cursor、Cursor 内 Codex 插件、`/Applications/Codex.app`、Git 的统一 HTTP(S) 入口是 `127.0.0.1:4782`；路由脚本为 `/Users/stark/.local/libexec/cursor-vpn-proxy-router.py`，LaunchAgent 为 `/Users/stark/Library/LaunchAgents/com.stark.cursor-vpn-proxy-router.plist`。
2. `4782` 优先使用 Clash Verge mixed HTTP/SOCKS 代理 `127.0.0.1:7897`，并以目标 HTTPS `CONNECT` 成功作为可用判据；Clash 不可用时改走当前 macOS 系统路由。PrivateVPN 连接并以 `utun*` 接管默认公网路由时，系统回退自然经过 PrivateVPN；两个 VPN 都未连接时则普通直连。
3. 持久控制点统一为 `4782`：Cursor 使用 `http.proxy = http://127.0.0.1:4782` / `http.proxySupport = override`，Git 全局 `http.proxy` 与 GUI `launchctl` 的 `HTTP_PROXY` / `HTTPS_PROXY` 使用同一地址；为覆盖 Chrome 等 GUI 应用，`Wi-Fi` 与“深圳办公室 VPN”的 HTTP/HTTPS 系统代理也启用为 `127.0.0.1:4782`，SOCKS 关闭，私网地址保留 bypass。无需依赖 Clash 自己的 System Proxy 开关。
4. 终端层由 `~/.zprofile`、`~/.zshrc`、`~/.profile`、`~/.bashrc` 显式设置大小写 `HTTP_PROXY/HTTPS_PROXY = http://127.0.0.1:4782`，`~/.bash_profile` 从 `~/.profile` 继承；清除 `ALL_PROXY`，并在 `NO_PROXY/no_proxy` 中保留精确主机 `192.168.99.29` 和私网网段，确保新开的 macOS Terminal、Cursor 集成终端、zsh 和 bash 使用同一逻辑且深圳内网继续经 `ppp0`。
5. `/Users/stark/.cursor/scripts/sync-gui-proxy-env.sh` 先写 GUI 环境再启动并等待路由器，以消除登录启动竞态；它只能同步外部 GUI 环境，禁止修改 Cursor/Codex 签名 App 包内的 `Info.plist`。修改配置后须完全退出并重开 Cursor/Codex，让现有进程继承新环境。
6. 验收必须包含 `7897/4782` 监听、`route -n get 1.1.1.1`、`4782` 正常与故障回退、清空继承环境的新 zsh/bash 登录与非登录 shell、公网/深圳内网/Git 实际请求、Cursor/Codex 到 `4782` 的真实连接、Codex app-server `model/list`，以及 Cursor/Codex 的 `codesign` / `spctl` 结果。两个 VPN 都关闭时，本机 `4782` 仍存在，但对外应为普通直连；运行时端口、路由和模型列表仍需现场复核。
7. Cursor `3.15.6` 不接受 OpenAI Codex 的 Secondary Side Bar 容器；本机兼容扩展 `/Users/stark/.cursor/extensions/stark-local.codex-cursor-compat-1.0.0` 会把 Codex 固定到 Activity Bar、重映射原生打开命令，并在 OpenAI 扩展更新后重新修正扩展清单和清除对应用户扩展缓存。不得通过修改 `/Applications/Cursor.app` 处理此问题。

## 执行工作流

1. 确认当前工作区或用户指定路径，并用双平台路径表理解当前机器路径。
2. 按「新会话必读顺序」与「上下文加载门禁」拉取最小有用上下文。
3. 识别请求形态，并合并用户输入框、本 Cursor skill 与 Codex 对照 skill 的「当前活跃需求」未注释条目为验收清单。
4. 判断任务类型：Mac 硬件/系统、维修/回收、Apple 官方政策、VPN/代理/Git 网络、Cursor/Codex 配置、网页读取、文档沉淀。
5. 扩大范围前，先指向最相关的文件或 skill；需子 skill、BMAD、图片、网页或模板时，先补读依赖。
6. 依赖最新外部事实时先联网查证，再给判断；输出中区分用户材料事实、联网核验事实、归纳建议与风险判断。
7. 需长期保留的结论优先更新 `MAC系统相关问题解决方案.md`，而非仅留在对话中。

## 输出约定

- 对用户：**简体中文**（除非用户要求其他语言）。
- 路径、命令、型号、平台名、配置键保持原文。
- 涉及价格、门店、回收规则、维修政策、官方说明、工具能力时，注明结论基于当日可核验信息。
- 不把经验判断写成无条件事实；区分「用户材料直接支持」「联网核验」「我的判断/建议」。
- 不把截图文字摘要替代截图读取；读图失败必须明确说明精确路径读取结果。
- 涉及配置变更时，提醒需要的重启、重载或验证动作。
- **任务结束**：必须包含「当前 chat 已加载的关键文件」「本轮新增读取/加载的文件」。

## 边界

- 不把第三方平台旧报价、旧规则写成长期稳定事实。
- 不在未查证时断言某家维修店、回收平台或网络服务一定可靠/最划算。
- 不新建额外 `.md` 文档，除非用户明确要求。
- 不向 skill、解决方案文档或对话写入真实密钥、Cookie、token、私钥；敏感配置用占位符。
- 不擅自执行高风险系统改动；需要影响全局网络、证书、登录态或账户安全时，先给出可回滚步骤与验证方式。

## 当前活跃需求(不要修改这部分的子内容)
<!-- - 帮我把当前项目的代码push到远程仓库 -->
