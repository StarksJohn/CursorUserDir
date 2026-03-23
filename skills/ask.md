> **[已归档] 本文件内容已合并到 User Rules（`Cursor AI 规则.md` 第 9 条"Skill 执行规范"），所有会话自动生效，无需任何 Skill 单独加载本文件。此文件仅保留作为历史参考。**

# Cursor Skills 通用执行规范

---

## 适用范围

本文件为 Cursor Skills 提供通用前置规范。  
仅当某个 SKILL.md 的步骤中显式要求"先读取通用执行规范"时才会被加载。  
本文件 **不会** 自动对所有 Skill 生效；真正的全局规范由 User Rules 承担。

## 与 User Rules 的关系

- **User Rules**: 每个会话自动生效，负责输出语言、工具优先级、编程原则、Token 优化等全局约束
- **本文件**: 补充 User Rules 未覆盖的 Skill 执行流程规范，不重复 User Rules 已有内容

## Skill 执行流程

### 前置检查

1. 确认本次 Skill 的目标（审查 / 初始化 / 迁移 / 其他）
2. 明确涉及的文件范围，只加载必要上下文
3. 若 Skill 涉及项目代码，确认 `.cursor/rules/project-context.mdc` 已存在

### 执行中约束

- 先理解目标 -> 收集最小上下文 -> 给出方案 -> 实现 -> 验证
- 复杂 Skill（涉及多文件或架构决策）先给方案，等确认后再实现
- 路径已知时直接 ReadFile，不先 Glob
- 不主动创建未要求的文件或文档

### 完成标准

- 简要说明已完成的内容与关键变更
- 给出验证方式或下一步建议
- 若涉及文档更新，明确更新了哪个文件及哪些章节
- 若涉及配置变更，提醒需要的重启或验证动作

## 文件保护

**严格禁止** 任何 Skill 修改以下文件:

- Win11: `C:\Users\Stark8964911\.cursor\skills\ask.md`
- Mac: `~/.cursor/skills/ask.md`

## 配置信息速查

| 项目 | Win11 | Mac |
|------|-------|-----|
| Cursor 用户主目录 | `C:\Users\Stark8964911\.cursor` | `~/.cursor` |
| Cursor 配置数据 | `C:\Users\Stark8964911\AppData\Roaming\Cursor` | `~/Library/Application Support/Cursor` |
| Skills 目录 | `C:\Users\Stark8964911\.cursor\skills` | `~/.cursor/skills` |
| Commands 目录 | `C:\Users\Stark8964911\.cursor\commands` | `~/.cursor/commands` |
| MCP 配置 | `C:\Users\Stark8964911\.cursor\mcp.json` | `~/.cursor/mcp.json` |
