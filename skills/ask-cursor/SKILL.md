---
name: ask-cursor
description: 迁移并执行 ask_cursor 工作流，处理 Cursor IDE 配置优化、Claude Code 到 Cursor 的 Rules、Commands、Skills、MCP 迁移，以及相关使用指南更新。Use when the user mentions ask_cursor, Cursor 配置优化, 模型能力发挥, or migrating Claude Code workflows into Cursor.
---

# Ask Cursor

## 目标

把旧的 `claude code` `ask_cursor` 工作流，收敛成一个可在 Cursor 中稳定复用的个人 Skill。

## 必做步骤

1. 先读取 `ask.md` 模板获取执行规范：
   - Windows: `C:/Users/Stark8964911/.claude/ask/ask.md`
   - Mac: `/Users/stark/.claude/ask/ask.md`
2. 若需要兼容旧工作流，再读取：
   - Windows: `C:/Users/Stark8964911/.claude/commands/ask_cursor.md`
   - Mac: `/Users/stark/.claude/commands/ask_cursor.md`
  
## 配置信息
- Windows11系统全局配置数据目录(User 设置、工作区存储、UI 状态等，类似 VS Code):`C:\Users\Stark8964911\AppData\Roaming\Cursor`
- Cursor 用户级命令、技能、MCP 主目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）: 
- cursor提问目录: `C:\Users\Stark8964911\.cursor`（Win11）或 `~/.cursor`（Mac）
- cursor 常打开的项目类型: React Native, React, Vue, iOS, Android, 微信小程序

## 默认迁移策略

- 常驻偏好放 `User Rules`
- 项目长期规则放 `.cursor/rules/*.mdc`
- 按需多步流程放 `~/.cursor/skills/`
- 显式 slash 命令兼容入口放 `~/.cursor/commands/`
- 本地 MCP 配置放 `~/.cursor/mcp.json`

## 当前 ask_cursor 场景的推荐主入口

- Windows: `C:/Users/Stark8964911/.cursor/skills/ask-cursor/SKILL.md`
- Mac: `~/.cursor/skills/ask-cursor/SKILL.md`

这份 Skill 是主入口；旧的 `~/.claude/commands/ask_cursor.md` 只作为历史来源或兼容参考，不再作为长期主维护点。

## 回答要求

1. 先给结论，再给路径和落地方案
2. 已知路径直接读文件，不先全局搜索
3. 只有在回答当前模型、价格、计划、官方文档时，才联网并注明日期
4. 如果命令或文档里引用图片，先按同目录精确路径读取
5. 如果用户要求更新使用指南，同步更新：
   - `C:/Users/Stark8964911/AppData/Roaming/Cursor/Cursor_使用指南与Token优化.md`

## 推荐输出结构

1. 当前结论
2. 迁移路径
3. 使用方式
4. 验证步骤
5. 风险或后续建议

## 当前活跃需求
- 我当前是`cursor Pro+ Annual $48/mo.` 计划的用户
  <!-- - 目前有如图![img_150249.png](img_150249.png)2个计费池,一个是使用高级API的计费池,一个是`Auto + Composer`的计费池 -->
  <!-- - 当前Win11系统之前使用了`claude code`, 全局配置目录在`C:\Users\Stark8964911\.claude`,配置了 `"C:\Users\Stark8964911\.claude\CLAUDE.md"`和很多MCP,还有很多自定义的commands;现在我换成在 `cursor IDE`里使用`claude-4.6-sonnet-medium-thinking`模型,怎么在 `cursor IDE`里进行全面配置,以便达到和之前在`claude code`里同样的模型使用效果 -->
  - 当前Win11系统已经安装了`cursor IDE`
    - 把`C:\Users\Stark8964911\.claude\commands\ask_cursor.md`迁成一个真正的 `cursor Skill`,以后 Win/Mac 都按更稳定的方式迁移和复用
    <!-- - 我需要最大化发挥出 ![img_175558.png](img_175558.png) 这几个模型的编码和架构能力, 还需要进行哪些全局配置优化? -->
  <!-- - 在![img_175437.png](img_175437.png)里创建哪些skills,可以最大化发挥出 ![img_155600.png](img_155600.png) 这几个模型的编码和架构能力?
    - 根据 `C:\Users\Stark8964911\AppData\Roaming\Cursor\Cursor_使用指南与Token优化.md`的![img_180617.png](img_180617.png),我怎么创建 `code-review`这个 skill ? 比如同事在 `https://bitbucket.org/healshealthcare/csx-mobile/pull-requests/437/overview`里 提了一个PR, 我怎么在 cursor 里 使用 `code-review` 这个 skills 来检查这个 PR ?
  - 什么是 OpenClaw? cursor里能否借助GPT‑5.4来使用OpenClaw? -->
- 把以上问题你的解答总结更新到 `C:\Users\Stark8964911\AppData\Roaming\Cursor\Cursor_使用指南与Token优化.md`
