---
name: init-project
description: >-
  Cursor 项目规则刷新入口。用于 /init-project、初始化新项目，或项目技术栈、关键目录、
  构建测试方式、架构边界发生重大变化时；分析当前仓库，只在稳定事实确实变化时更新
  对应 Codex 项目 Skill 同目录的 AGENTS.md，不创建仓库根 AGENTS.md 或 project-context.mdc。
---

# init-project

## 共享规则源

- 激活后先完整读取本 `SKILL.md`，再完整读取 Codex 对照入口：macOS `$HOME/.codex/skills/initProject/SKILL.md`；Windows `%USERPROFILE%\.codex\skills\initProject\SKILL.md`。
- 按 Codex 对照入口的项目映射、最小读取顺序、更新判断、执行流程和验证标准操作。
- 两端唯一写入目标都是对应 Codex 项目 Skill 同目录的 `AGENTS.md`：macOS `$HOME/.codex/skills/<project-skill>/AGENTS.md`；Windows `%USERPROFILE%\.codex\skills\<project-skill>\AGENTS.md`。
- 不创建或刷新仓库根 `AGENTS.md`，也不创建 `.cursor/rules/project-context.mdc`。

## Cursor 执行门禁

1. 确认当前业务仓库 Git 根、未提交改动和 Codex 对照入口中的 `<project-skill>` 映射。
2. 完整读取目标 `AGENTS.md`，再只读取判断本次重大结构变化所需的 manifest、关键配置、受影响目录和相关文档章节。
3. 只有项目身份、主技术栈、核心架构、稳定工作流或长期边界确实变化时，才最小更新目标 `AGENTS.md`。
4. 不写完整目录树、依赖/版本/命令清单、当前任务状态或聊天流水；这些事实从当前源码和配置按需恢复。
5. 若稳定事实没有变化，不修改文件并报告“无需刷新”。
6. 若旧 `.cursor/rules/project-context.mdc` 仍存在，先迁移其中尚未覆盖的唯一稳定事实，再删除该文件，不保留 Cursor 规则副本。
7. 不修改任何项目入口 Skill 的受保护待办区，除非用户明确授权。

## 普通项目任务中的维护

通过 `/ask-<project>` 执行普通任务时，只检查与任务相关的源码、manifest 和配置。若本次任务改变了稳定架构、命令工作流或项目边界，在代码与聚焦测试完成后自动更新共享 `AGENTS.md`；无稳定事实变化时不得全仓扫描。别人合并进来的大规模结构变化使用 `/init-project` 做一次完整刷新。

## 失败与验证

- Codex 对照入口读取失败时，报告精确路径并停止规则刷新；不得改写其它项目或创建仓库内副本。
- 项目映射不唯一时先让用户确认 `<project-skill>`。
- 完成后确认仓库根没有新 `AGENTS.md`、仓库内没有 `project-context.mdc`，并对 `~/.codex` 与 `~/.cursor` 中的相关修改运行 `git diff --check` 和 Skill 校验。
- 不主动运行应用、安装依赖、部署或执行完整测试，除非用户同时明确要求。
