---
name: ask-mac
description: >-
  Cursor 侧 MAC 系统问题入口 skill。适用于用户输入 `/ask-mac`，或围绕
  MacBook、macOS、Mac 维修/回收、Apple 官方支持、Cursor 与 Codex 在 Mac 上的
  配置与协作等问题，需要先读取 ask 模板、再按最小必要上下文分析或更新
  既有解决方案文档时。Codex 对口入口为 `/mac`。
---

# ask-mac（Cursor）

## 与 Codex 入口的关系

| 客户端 | `SKILL.md` | `name` | 口令 |
|--------|------------|--------|------|
| Cursor（本文件） | **Windows** `%USERPROFILE%\.cursor\skills\ask-mac\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-mac/SKILL.md` | `ask-mac` | `/ask-mac` |
| Codex（OpenAI） | **Windows** `%USERPROFILE%\.codex\skills\mac\SKILL.md` / **macOS** `/Users/<你的用户名>/.codex/skills/mac/SKILL.md` | `mac` | `/mac` |

两份文件分别维护，但要保持同一套核心流程：

1. 先读取 `ask.md Template`
2. 按任务需要读取既有解决方案文档
3. 只补充当前问题直接相关的图片、网页与资料
4. 若用户要求沉淀结论，优先更新既有解决方案文档

因此，在 Cursor 输入 `/ask-mac`，与在 Cursor 内 Codex 插件输入 `/mac`，应得到同类任务理解、同一文件加载顺序与同一类交付效果。

## 目的

本 skill 是 **MAC 系统问题** 的默认分析入口，用于：

- 统一承接 Mac 硬件故障、macOS 使用问题、维修/回收、Apple 官方支持与相关配置问题
- 先恢复已有问题背景，再回答或更新既有文档
- 避免把一次性截图结论、平台报价、门店信息散落在多处
- 让 Cursor 的 `/ask-mac` 与 Codex 的 `/mac` 使用同一套任务入口语义

## 何时使用

满足以下任一情况时启用本 skill：

- 用户显式输入 `/ask-mac`
- 用户自然语言提及 **ask-mac**、**MAC 系统问题**、**MacBook 故障**、**Mac 维修 / 回收**
- 工作区为 MAC 问题目录，且任务需要基于既有解决方案文档继续推进
- 用户希望将 Cursor 与 Cursor 内 Codex 插件中的执行效果对齐

## 新会话必读顺序

在回答、联网检索、更新文档或继续专项分析之前，按顺序读取：

1. **ask 模板**
   - Windows：`C:\Users\Stark8964911\.claude\ask\ask.md`
   - macOS：`/Users/stark/.claude/ask/ask.md`
2. **既有解决方案文档**
   - Windows：`D:\work\MAC\MAC系统相关问题解决方案.md`
   - macOS：`/Users/<你的用户名>/Desktop/work/MAC/MAC系统相关问题解决方案.md`
   - 当用户只是做一次性简单问答时，可按最小上下文只读取相关章节；若用户要求“总结更新到文档”，则必须读取后再编辑。
3. **与当前任务直接相关的截图、票据、页面资料或额外文档**
   - 若前述 `.md` 中出现 `![img_xxx.png](img_xxx.png)`，图片视为与引用它的 `.md` 文件同目录，必须先按精确路径读取，再据此判断。
4. **最新外部事实**
   - 维修政策、平台回收规则、门店营业信息、报价、官方说明等都可能变化；涉及这类问题时，必须基于当天信息联网核对后再下结论。

## 工作区与文件路径

| 用途 | Windows | macOS |
|------|---------|--------|
| MAC 工作区根 | `D:\work\MAC` | `/Users/<你的用户名>/Desktop/work/MAC` |
| 当前 Mac 机器的实际工作区 | - | `/Users/stark/Desktop/work/MAC` |
| 解决方案文档 | `D:\work\MAC\MAC系统相关问题解决方案.md` | `/Users/<你的用户名>/Desktop/work/MAC/MAC系统相关问题解决方案.md` |
| ask 模板 | `C:\Users\Stark8964911\.claude\ask\ask.md` | `/Users/stark/.claude/ask/ask.md` |
| 本 skill | `%USERPROFILE%\.cursor\skills\ask-mac\SKILL.md` | `/Users/<你的用户名>/.cursor/skills/ask-mac/SKILL.md` |
| Codex 对口 skill | `%USERPROFILE%\.codex\skills\mac\SKILL.md` | `/Users/<你的用户名>/.codex/skills/mac/SKILL.md` |

## Cursor / Codex 目录分工

| 用途 | Windows | macOS |
|------|---------|--------|
| Cursor Agent Skills | `%USERPROFILE%\.cursor\skills\...` | `/Users/<你的用户名>/.cursor/skills/...` |
| Cursor 应用配置与用户数据 | `%APPDATA%\Cursor\` | `~/Library/Application Support/Cursor/` |
| Codex 配置、规则、skills | `%USERPROFILE%\.codex\...` | `/Users/<你的用户名>/.codex/...` |

## 执行工作流

1. 先按「新会话必读顺序」恢复上下文。
2. 判断当前请求属于哪类：
   - Mac 硬件故障判断
   - 维修与回收路径比较
   - 平台规则 / 售后政策核验
   - Cursor / Codex 在 Mac 上的配置与使用问题
   - 对既有解决方案文档做补充、纠错或重组
3. 若问题依赖最新外部事实，先联网查证，再下结论。
4. 若任务要求沉淀结论，优先更新 `MAC系统相关问题解决方案.md`，不要另建新的 Markdown 文件。
5. 输出时区分：
   - 已由用户材料直接支持的事实
   - 通过联网核验得到的最新事实
   - 你的归纳、建议与风险判断

## 输出约定

- 面向用户使用 **简体中文**
- 保持路径、平台名、型号、命令原样
- 涉及价格、门店、平台回收规则、官方售后政策时，必须注明结论基于当日可核验信息
- 不把“平台可能检测出维修痕迹”写成无条件绝对判断；需要分清确定事实、经验判断与平台条款

## 边界

- 不把第三方平台的旧报价、旧规则写成长期稳定事实
- 不把截图文字摘要替代截图读取
- 不在未查证时断言某家维修店“可靠”或“最划算”
- 不新建额外 `.md` 文档，除非用户明确要求

## 当前活跃需求(不要修改这部分的子内容)
- 帮我把当前项目的代码push到远程仓库