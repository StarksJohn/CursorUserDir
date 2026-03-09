---
name: react-native-patterns
description: Hooks 组织、平台差异、性能陷阱、键盘与图片体验。适用于 React Native 开发、跨端模式、RN 最佳实践，或用户请求 react native patterns 时。
---

# React Native Patterns

## 触发场景

- 用户输入 `@react-native-patterns` 或提及“RN 最佳实践”“跨端”“Hooks 组织”
- React Native 项目开发与审查
- iOS/Android 平台差异处理
- 性能优化与内存问题排查

## 输入格式

| 输入示例 | 说明 |
|----------|------|
| `@react-native-patterns` | 按 RN 模式审查当前代码 |
| `@react-native-patterns 性能` | 聚焦性能与内存 |
| `@react-native-patterns 键盘` | 聚焦键盘与输入体验 |

## 审查维度

### 1. Hooks 组织

- [ ] Hooks 调用顺序稳定，无条件调用
- [ ] 自定义 Hook 职责单一，可复用
- [ ] 依赖数组完整，避免闭包陈旧
- [ ] 大对象/数组用 `useMemo`/`useCallback` 避免多余重渲染

### 2. 平台差异

- [ ] `Platform.OS` / `Platform.select` 使用正确
- [ ] 条件 require 或动态 import 处理平台资源
- [ ] 尺寸与安全区域（SafeAreaView）考虑
- [ ] 键盘避让（`KeyboardAvoidingView`、`keyboardVerticalOffset`）

### 3. 性能陷阱

- [ ] 长列表使用 `FlatList`/`SectionList`，避免 `ScrollView` 渲染大量项
- [ ] 图片使用 `FastImage` 或类似优化（按项目约定）
- [ ] 避免在 render 中创建新对象/函数
- [ ] 大计算用 `useMemo`，事件用 `useCallback`
- [ ] 警惕 `useEffect` 依赖缺失导致的内存泄漏或重复订阅

### 4. 键盘与输入体验

- [ ] `KeyboardAvoidingView` 的 `behavior` 与平台匹配
- [ ] `keyboardVerticalOffset` 在 iOS 导航栏场景下的设置
- [ ] `ScrollView` 与键盘的 `keyboardShouldPersistTaps`
- [ ] 输入框聚焦时的滚动与遮挡处理

### 5. 图片与内存

- [ ] 大图懒加载、尺寸适配
- [ ] 列表图片使用 `FastImage` 或项目约定方案
- [ ] 避免在循环内创建 Image 组件导致内存激增

## 输出格式

使用标签（按规则不使用 emoji）：

- **[Critical]**: 性能或体验严重问题
- **[Suggestion]**: 建议改进
- **[Nice to have]**: 可选优化

```markdown
# React Native Patterns Review: [范围]
## 摘要
[1–2 句概述]
## Critical
- [文件:行号] [问题与建议]
## Suggestions
- [文件:行号] [建议]
## Nice to have
- [可选改进]
```

## 常用模式速查

| 场景 | 推荐做法 |
|------|----------|
| 平台样式 | `Platform.select({ ios: {...}, android: {...} })` |
| 安全区域 | `SafeAreaView` 或 `react-native-safe-area-context` |
| 键盘避让 | `KeyboardAvoidingView` + `behavior`（ios: padding, android: height 或 undefined） |
| 长列表 | `FlatList` + `getItemLayout`（固定高度时）、`windowSize` 调优 |
| 图片优化 | `FastImage` 或 `Image` + `resizeMode`、合理尺寸 |

## 推荐模型

- 日常 RN 开发：`Composer 1.5` 或 `GPT-5.4`
- 复杂性能/原生桥接：`GPT-5.4`
