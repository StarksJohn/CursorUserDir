---
name: react-native-ui-verification
description: Runs evidence-based post-change verification for React Native implementations using focused checks, real devices or simulators, UI automation, accessibility hierarchy, screenshots, visual comparison, and runtime logs. Use automatically after changing React Native code and before claiming the task is complete, especially for UI, navigation, interaction, animation, native, or cross-platform changes.
---

# React Native UI Verification

## Purpose

在 React Native 实现完成后建立可复核的证据链。验证目标是降低遗漏风险，不承诺任何工具能证明软件“完全正确”。

## When to Use

- 修改 React Native 业务代码、UI、导航、交互、动画或原生配置后。
- 修复 React Native Bug 后。
- 用户要求真机、模拟器、Figma 还原、视觉或回归验证时。
- 纯解释、只读审查、文档或注释修改不运行设备 UI；明确标记为不适用。

## Inputs and Context

开始前确认：

1. 改动文件、用户验收标准和受影响状态。
2. Android/iOS、flavor/scheme、环境和目标包标识。
3. 项目已有 lint、类型、单测、E2E、截图或视觉回归工具。
4. 可用真机/模拟器及其分辨率、密度、系统版本和语言。
5. 是否有 Figma 节点、基准图或明确视觉规格。

不得为了验证清除用户数据、重置账号、修改生产数据或覆盖无关工作树。新增依赖、E2E 框架或永久基准图前先取得授权。

## Verification Gate

### 0. Detect Capability Levels

先运行：

```bash
python3 "$HOME/.cursor/skills/react-native-ui-verification/scripts/check_toolchain.py" "$PROJECT_ROOT"
```

严格区分三层：

1. `globalAvailable`：CLI/Driver 在本机可启动，不构成项目测试证据。
2. `projectConfigured`：仓库已有本地依赖、配置、flow 或测试，不代表当前版本通过。
3. `currentRunVerified`：针对当前构建、设备和目标状态实际执行并通过，才可作为本次 E2E 证据。

任何全局安装都不得冒充 `projectConfigured` 或 `currentRunVerified`。检测脚本始终将本次运行标记为 false，实际测试命令的结果由当前任务单独记录。

### 1. Classify the Change

按风险选择最小充分矩阵：

- 逻辑或数据：定向类型/lint/单测；用户可见行为变化时增加运行时验证。
- UI、样式、图标、文案：目标页面真机/模拟器验证、截图、控件树、日志。
- 导航、表单、手势：自动或可复现交互、状态断言、截图、日志。
- 动画、键盘、弹窗、滚动：关键时序录屏或多状态截图，并验证遮挡和触控。
- 原生、权限、深链、平台 API：受影响平台真实构建、安装、启动和平台专项行为。
- 共享跨平台代码：Android 与 iOS 都应覆盖；缺少一端时只能判定“部分通过”。

### 2. Establish the Expected Baseline

在运行验收前先确定“正确”意味着什么：

- 有 Figma 页面/节点或任务要求按 Figma 还原时，先执行全局 Figma MCP 硬门禁，读取节点元数据、设计上下文、变量、设计系统信息和截图，再进入实现判断或 UI 验收。
- 没有 Figma 时，使用用户参考图、明确验收标准、项目设计 token、资产和同产品已确认组件建立基线，并明确记录“无精确 Figma 节点”。没有可核对基线时只能验证项目一致性和运行健康，不能宣称与目标设计完全一致。
- 列出要核对的文案、图标、状态、尺寸、间距、颜色、字体、可点击区域、滚动/键盘/弹窗行为和平台差异；只覆盖本次改动直接影响的范围。

### 3. Run Focused Static Checks

优先运行项目已有的定向类型检查、lint、Jest/组件测试和受影响模块测试。不要用全仓历史错误掩盖当前结果，也不要把静态通过写成 UI 已通过。

### 4. Prove the Runtime Target

运行 UI 前记录并核对：

- 设备/模拟器唯一标识和状态。
- 实际安装的 app ID、flavor/scheme 和环境。
- 应用进程、前台 Activity/View Controller 和目标页面。
- 分辨率、密度、方向、字体缩放、语言和主题等会影响 UI 的条件。

Android 使用指定 serial 的 `adb -s`，多设备时禁止依赖默认设备。iOS 使用明确 simulator UDID 或已授权真机。

### 5. Exercise the User Flow

优先级不是固定品牌排名，而是当前项目的集成程度和证据质量：

1. 运行项目已经配置、与当前验收范围匹配且本次可实际执行的 E2E/集成流程。
2. React Native 专项且需要同步应用状态时优先项目已集成的 Detox。
3. 需要低侵入、跨平台黑盒流程时优先项目已有 Maestro flow。
4. 企业 WebDriver/device-farm 流程已存在时使用项目已集成的 Appium client/config。
5. 都不存在时，用 `adb`/`simctl` 执行可复现的最小交互，并结合控件树断言；不能把坐标点击当成稳定 E2E。

断言用户可观察结果：元素可见、文案、选中/禁用状态、页面跳转、输入结果和返回行为。必要时为后续正式自动化建议稳定的 `testID`/accessibility label，但不为单次验证擅自改业务接口。

### 6. Inspect Structure and Rendering

对每个关键状态同时收集：

- 设备/模拟器原始截图，保留系统栏或明确记录裁剪范围。
- Android `uiautomator` 或 iOS accessibility 层级中的文本、identifier、bounds、enabled、clickable/selected。
- 必要时录屏以检查动画、键盘、弹窗、滚动和短暂闪烁。

`uiautomator` 读取的是 Android accessibility/native 视图，不是完整 React 组件树；不可访问的 React Native View 可能缺失。React Native DevTools Components Inspector 可补充 React 树；Android Studio Layout Inspector 可补充原生组件树、属性、快照和参考图 Overlay；iOS Accessibility Inspector 与 Xcode View Debugger 可补充无障碍和平台层级。只有当前代理实际操控或读取到结果时才能列为证据，这些工具都不能代替最终像素和真实交互。

比较视觉结果前先对齐设备、尺寸、主题、语言、动态内容、系统栏和裁剪区域。阈值必须由项目或验收标准确定，不得自行用任意阈值宣称像素级通过。

视觉差异可使用 `scripts/compare_images.py` 生成差异指标和差异图；命令与平台操作见 [reference.md](reference.md)。

### 7. Check Runtime Health

围绕本次操作收集有时间边界、应用进程范围的日志，检查：

- JS exception、LogBox、unhandled rejection。
- Android crash/ANR、native fatal、资源和权限错误。
- iOS crash、native exception、Auto Layout 警告。
- 与改动直接相关的重复请求、明显掉帧或渲染循环。

日志清洁不能证明业务正确，但发现相关错误时验证不得判为通过。

### 8. Iterate Until Stable

发现问题后回到实现，修复并重跑失败步骤和直接相关回归。不要只替换截图或降低阈值。运行环境、数据或权限阻塞时停止伪验证并报告精确阻塞。

## Verdict

仅使用以下结论：

- `通过`：所有适用门禁均有直接证据通过。
- `部分通过`：已通过部分矩阵，但缺少平台、状态、设计基准或外部条件。
- `阻塞`：无法启动/进入目标状态，或存在未解决错误。
- `不适用`：任务没有运行时或 UI 影响，并说明依据。

最终报告必须包含：

1. 验证范围与环境。
2. 实际执行的静态、运行时、交互、结构、视觉和日志检查。
3. 证据路径或关键结果。
4. 未覆盖平台、设备、状态和风险。
5. 上述明确结论。

禁止使用“完全正确”“像素级一致”或“真机没有问题”，除非相应范围和可量化标准已被实际覆盖；即使通过，也只对已验证矩阵负责。

## Boundaries

- 截图是最终渲染证据之一，不是完整工作流。
- Android Studio Layout Inspector、Xcode View Debugger 和人工 GUI 检查可作为补充；未实际执行时不得列为证据。
- Chrome Browser DevTools 不支持替代 React Native DevTools；WebView 内容例外。
- E2E 重点覆盖关键用户旅程，非关键逻辑优先使用更快的 JS/组件测试。
- 全局 Maestro、Appium、Detox CLI 和 Appium Driver 只提供可用能力；没有项目 flow/config/test 和当前成功运行结果时，不得写成稳定 E2E。
- Detox 全局 CLI 只转发到项目本地 `detox`，没有本地依赖和原生 build configuration 时不可运行。
- 未经用户授权，不自动安装 Maestro/Detox/Appium，不创建长期 E2E 基础设施，不写入生产系统。
