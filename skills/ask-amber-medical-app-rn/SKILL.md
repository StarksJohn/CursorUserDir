---
name: ask-amber-medical-app-rn
description: >-
  Cursor：Amber Medical / Heals Pass React Native 项目入口。用于恢复 amber-medical-app-rn
  的工作区、项目规则、当前活跃需求和最小下一步，并路由 RN、TypeScript、API、i18n、
  导航、Figma、原生构建、代码审查或 BMAD 工作流。用户输入
  /ask-amber-medical-app-rn、提及 Amber Medical App / Heals Pass、当前工作区为 Windows
  D:\work\RN\amber-medical-app-rn 或 macOS
  $HOME/Desktop/work/RN/amber-medical-app-rn，或需要继续该仓库任务时使用。
---

# ask-amber-medical-app-rn

## 路径与事实源

- 项目根：**Windows** `D:\work\RN\amber-medical-app-rn`；**macOS** `/Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn`（当前 Mac：`/Users/stark/Desktop/work/RN/amber-medical-app-rn`）。用户指定 fork 或临时工作区时，以用户路径为准。
- 本入口：**Windows** `%USERPROFILE%\.cursor\skills\ask-amber-medical-app-rn\SKILL.md`；**macOS** `/Users/<你的用户名>/.cursor/skills/ask-amber-medical-app-rn/SKILL.md`。
- Codex 对照入口：**Windows** `%USERPROFILE%\.codex\skills\amber-medical-app-rn\SKILL.md`；**macOS** `/Users/<你的用户名>/.codex/skills/amber-medical-app-rn/SKILL.md`。
- 业务逻辑、API 映射、导航、校验、交互和错误处理以当前源码、测试及真实运行证据为准。
- 技术栈、依赖、命令、环境与构建以 `package.json`、原生工程、项目配置和 `README.md` 为准。
- 长期项目约束以 `.cursor/rules/project-context.mdc` 和实际存在的项目规则为准；当前活跃方向以本文件的受保护区块为准。

发生冲突时，当前源码、配置与真实运行证据优先于历史摘要；外部 contract、产品范围与发布结论以负责人最新确认优先。README 可能含敏感账号或凭证，只读取任务必要信息，不复制、输出或沉淀敏感值。

## 新会话读取顺序

1. 完整读取本 `SKILL.md`；只跳过当前 chat 已实际读取成功的文件。
2. 读取项目内实际存在的 `AGENTS.md`、`.cursor/rules/project-context.mdc`、任务相关 `.cursor/rules/*`、`README*`、`CLAUDE.md` 和 `package.json`。
3. 读取当前任务直接相关的源码、测试、配置、原生工程、截图或文档；不要通读 `src/`。
4. 仅在用户要求两端对齐、当前活跃需求明确引用 Codex 入口或需要核对 Codex 专属行为时，读取 Codex 对照入口。
5. 仅在需要平台差异、弃用状态或第三方 contract 时读取当前类型定义和官方文档。
6. 路由到其它 Skill、ask、command 或 BMAD 工作流时，先读取其 `SKILL.md` 及要求的依赖文件。

若仓库锚点缺失，明确缺口后用现有配置和源码继续；不要凭旧 Skill 中的版本号、目录清单或历史结论补造事实。

## 当前活跃需求解释

- 用户给出具体任务时，以用户任务为本轮范围；不要自动执行与其无关的活跃条目。
- 用户只输入入口口令或要求“继续”而未给具体任务时，忽略注释，从本文件首个未完成条目继续。
- 已完成、已注释或能从源码直接恢复的内容不重复执行；外部阻塞未变化时只报告最小下一步。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，否则不得改写、移动、拆分或删除其子内容。

## 实施工作流

1. 确认实际工作区、Git 状态和任务边界；保护无关未提交改动。
2. 先读用户提供或相关规则引用的全部图片；Figma 任务先通过 Figma MCP 取得目标节点事实。
3. 按任务定位最小源码与测试集合；API contract 可由真实页面触发时，优先读取实际请求与响应。
4. 代码任务依次完成项目内业务实现、定向测试/验证，确认无需再改代码后才更新项目外恢复文档。
5. 开发阶段优先单文件、单用例、单设备或局部原生构建；阶段收尾再按风险扩大验证范围。
6. 交付时说明结果、已执行验证、未验证项、风险和最小下一步；未运行应用、真机、构建或测试时如实说明。

## 工程约束

- React Native、React、TypeScript、依赖版本与脚本以当前 `package.json` 为准；TypeScript 保持 strict，复用项目既有组件、API 封装、状态、导航和样式体系。
- 新增用户可见文案时核对 `src/i18n/i18n.ts` 的活跃 locale，并同步对应语言资源；医疗健康文案避免确诊式、替代医嘱式或保证疗效式表述。
- 修改第三方 SDK 或原生桥接前核对当前类型定义与官方平台说明；共享逻辑不得直接使用仅限 iOS 或 Android 的字段而不给另一端分支或降级。
- API 真实结构优先从可触发的页面 Network/响应确认；受登录、权限或状态阻塞后才使用 Swagger、OpenAPI、后端文档或源码辅助判断。
- 不写入或输出 token、Cookie、密码、私钥、证书、keystore 密码、账号或真实环境密钥。

## 专项路由与硬门禁

- 规则缺失或需刷新 `project-context.mdc`：使用 `init-project`。
- RN 实现、类型、i18n、架构等专项任务：读取当前环境中匹配的专项 Skill 后执行；不要仅凭 Skill 名称或历史摘要代替正文。
- 精确 PR/commit 审查：使用当前已安装的 `code-review` 或 `bmad-code-review`，只审指定已提交 diff，并遵守其输出契约。
- 任意 `bmad-<identifier>`：先读取 **Windows** `%USERPROFILE%\.cursor\skills\<bmad-identifier>\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/<bmad-identifier>/SKILL.md`，再按要求读取 `workflow.md`、`checklist.md`、`reference.md`。
- Figma URL、节点或设计还原：先用当前 Cursor 可调用的 Figma MCP 读取目标节点；成功前不实现或验收，不以浏览器截图替代节点事实。
- Markdown 图片引用：以引用源 `.md` 所在目录拼接相对路径精确读取；精确读取失败后才搜索，并区分两种结果。
- 与 `heals-app-rn` 或其它仓库对照：仅在用户明确要求或本仓事实确实依赖时加载；不得默认套用其路径、模块或构建约定。

## 文档维护边界

- `project-context.mdc` 只保存跨会话稳定且不能廉价从源码恢复的项目事实与长期约束。
- `README.md` 只维护工程、运行、构建和发布事实；不得把账号、凭证或一次性会话状态复制到新文档。
- 本 Skill 只保存入口、事实源、加载门禁、恢复状态和最小下一步；不复制业务规则、API 字段、版本清单、测试数量或修复流水。
- 只有恢复状态、外部阻塞、最小下一步或非代码事实实质变化时才更新 Skill；普通代码修改不触发 Skill 改写。
- 不按日期追加流水；更新时替换过期结论并去重。非用户明确要求时不新建 `.md` 或脚本。

## 输出约定

- 面向用户使用简体中文；代码和代码注释使用英文。
- 默认只说明产出、验证、风险和下一步，不列上下文加载清单；仅在用户要求、审查/排障需要溯源、上下文缺失风险或慢任务复盘时列出。
- 不把“端口已监听、环境变量已设置、构建日志无报错”单独当成真实页面、API、设备或发布验收成功。

## 当前活跃需求（不要修改这部分的子内容）

<!-- 在此追加跨会话任务；路径写双平台：Windows D:\work\RN\amber-medical-app-rn / macOS /Users/<你的用户名>/Desktop/work/RN/amber-medical-app-rn（当前 Mac：/Users/stark/Desktop/work/RN/amber-medical-app-rn） -->
