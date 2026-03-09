---
name: typescript-strict
description: 约束 any、收紧类型边界、审查接口定义。适用于 TypeScript 严格模式、类型安全审查、接口设计，或用户请求 typescript strict 时。
---

# TypeScript Strict

## 触发场景

- 用户输入 `@typescript-strict` 或提及“类型收紧”“去 any”“接口审查”
- 准备开启或强化 `strict` 配置
- 审查类型定义与接口设计
- 迁移 JS 到 TS 时的类型策略

## 输入格式

| 输入示例 | 说明 |
|----------|------|
| `@typescript-strict` | 审查当前文件/项目的类型用法 |
| `@typescript-strict 去除 any` | 聚焦 any 替换 |
| `@typescript-strict 接口 X 定义` | 审查特定接口 |

## 审查维度

### 1. 禁止与替代

- [ ] 禁止 `any`，改用 `unknown` 或具体类型
- [ ] 禁止隐式 `any`，显式标注或启用 `noImplicitAny`
- [ ] 泛型约束是否充分，避免 `T extends any`

### 2. 类型边界

- [ ] 函数参数与返回值类型完整
- [ ] 可选属性与 `undefined` 区分
- [ ] 联合类型是否收窄得当
- [ ] 类型断言是否必要且安全

### 3. 接口与类型设计

- [ ] `interface` 优先于 `type`（对象形态）
- [ ] 避免 `type` 与 `interface` 重复定义
- [ ] 导出类型是否稳定、可复用
- [ ] 泛型参数命名与约束清晰

### 4. 配置建议

- [ ] `strict: true` 或等价子项
- [ ] `noUncheckedIndexedAccess`（按需）
- [ ] `exactOptionalPropertyTypes`（按需）
- [ ] `strictNullChecks` 已开启

## 输出格式

使用标签（按规则不使用 emoji）：

- **[Critical]**: 类型漏洞或安全风险
- **[Suggestion]**: 建议改进
- **[Nice to have]**: 可选优化

```markdown
# TypeScript Strict Review: [范围]
## 摘要
[1–2 句概述]
## Critical
- [文件:行号] [问题与建议类型]
## Suggestions
- [文件:行号] [建议]
## Nice to have
- [可选改进]
```

## 常见 any 替代

| 场景 | 替代方案 |
|------|----------|
| 未知 JSON | `unknown` + 校验或 `zod`/`io-ts` |
| 泛型默认 | `unknown` 或显式约束 |
| 第三方无类型 | 声明 `.d.ts` 或 `@ts-ignore`（最小范围） |
| 动态 key | `Record<string, T>` 或 `{[k: string]: T}` |

## 推荐模型

- 日常类型审查：`GPT-5.4` 或 `Claude Sonnet 4.6`
- 复杂泛型与工具类型：`GPT-5.4`
