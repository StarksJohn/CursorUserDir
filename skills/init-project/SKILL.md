---
name: init-project
description: 通过分析工作区为 Cursor 初始化项目上下文，生成 .cursor/rules/project-context.mdc。适用于打开新项目、项目结构重大变更后，或用户调用 /init、@init-project 时。
---

# Init Project - 为 Cursor 初始化项目上下文

按顺序执行以下步骤。不要请求确认，直接创建文件。生成内容中的注释使用英文。

## Step 1: 分析当前工作区

- 读取 `package.json`（或等价文件：`pom.xml`、`build.gradle`、`Cargo.toml`、`pyproject.toml` 等）
- 若存在则读取 `README.md`
- 扫描项目结构（src/、lib/、app/、components/ 等）
- 识别技术栈、框架、构建工具

## Step 2: 创建项目规则文件

- 若不存在则在工作区根目录创建 `.cursor/rules/` 目录
- 创建 `.cursor/rules/project-context.mdc`

## Step 3: project-context.mdc 结构（必填）

YAML frontmatter：

```yaml
---
description: "Project context"
alwaysApply: true
---
```

必填章节：

| Section | Content |
|---------|---------|
| Project Overview | 项目简介 |
| Tech Stack | 框架、语言、核心依赖 |
| Development Commands | npm/yarn 脚本、运行说明 |
| Node/Runtime version | 如适用（来自 .nvmrc、engines 等） |
| Directory Structure | 主要目录及用途 |
| Architecture notes | 入口、路由、状态管理 |
| Build/Deploy notes | 如相关 |
| Code style or conventions | 如可发现（如 .eslintrc、prettier） |

## Step 4: 输出

- 确认文件已创建
- 简要概括所捕获的上下文
