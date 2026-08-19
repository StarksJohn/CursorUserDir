---
name: ask-CircleAppNew
description: >-
  CircleApp 私有恢复与专项路由入口。仅在用户显式使用独立入口词
  /ask-CircleAppNew 或 @ask-CircleAppNew，或明确要求继续受保护待办、恢复跨会话状态、
  处理外部构建发布阻塞时使用。每个新 chat 先调用本入口；随后强制读取 Codex
  对口 Skill 同目录 AGENTS.md 作为共享仓库规则。
---

# ask-CircleAppNew（Cursor）

## 调用策略

- 激活本 Skill 后，先完整读取本 `SKILL.md`，再立即完整读取 `$HOME/.codex/skills/CircleAppNew/AGENTS.md`（Windows：`%USERPROFILE%\.codex\skills\CircleAppNew\AGENTS.md`）；读取失败时停止项目实现并报告精确路径，不得跳过。
- 每个新 chat 先显式调用本入口，再从共享 `AGENTS.md` 与当前源码开始普通实现、排障、审查和测试；项目根不维护第二份 `AGENTS.md`。
- 本 Skill 只处理私有恢复状态、受保护待办、跨客户端对齐和外部构建/发布上下文。
- 用户给出具体任务时，该任务优先；只有仅调用入口或明确要求“继续”时，才解析未注释待办。

## 路径与事实源

- 项目根：Windows `D:\work\RN\CircleAppNew`；macOS `$HOME/Desktop/work/RN/circleapp`，当前 Mac 为 `/Users/stark/Desktop/work/RN/circleapp`。用户给出 fork、worktree 或其它路径时以用户路径为准。
- 本入口：Windows `%USERPROFILE%\.cursor\skills\ask-CircleAppNew\SKILL.md`；macOS `$HOME/.cursor/skills/ask-CircleAppNew/SKILL.md`。
- Codex 对口入口：Windows `%USERPROFILE%\.codex\skills\CircleAppNew\SKILL.md`；macOS `$HOME/.codex/skills/CircleAppNew/SKILL.md`。
- 稳定工程约束只维护在 Codex 对口目录的 `AGENTS.md`；不创建仓库根 `AGENTS.md` 或 `.cursor/rules/project-context.mdc`。
- 依赖、脚本、环境与工具版本：以 `{workspace}/package.json`、项目配置和原生工程为准。
- 业务逻辑、API、导航、交互与错误处理：以当前源码、测试、真实页面 / 真机和实际请求响应为准。
- 工程、构建与发布说明：仅在任务需要时读取 `{workspace}/README.md`、`CLAUDE.md` 或专项指南。
- 当前待办：以用户本轮明确请求为先；需要恢复待继续任务时，再读取两侧入口的受保护区块。

发生冲突时，当前代码、配置和真实运行证据优先于历史文档；外部 contract 与发布范围以负责人最新确认优先。

## 启用与最小读取顺序

1. 完整读取本 `SKILL.md`。
2. 完整读取 Codex 对口 `SKILL.md`，核对共同门禁、受保护活跃需求和其同目录图片引用。
3. 确认实际 `{workspace}`，读取 Codex 对口目录 `AGENTS.md` 和 `{workspace}/package.json`；只从当前任务需要的源码、配置和原生工程继续恢复事实。
4. 只读取当前任务直接相关的源码、测试、配置或指南；需要命令、原生构建或发布事实时再扩大范围。
5. 图片引用按引用源 `.md` 的目录精确解析并先读取图片；精确路径读取失败后才搜索。
6. 路由到其它 Skill、ask、command 或 BMAD 时，先完整读取对应 `SKILL.md` 及其要求的 `workflow.md`、`checklist.md`、`reference.md` 或图片。

用户给出具体新任务时，以该任务为本轮范围，不自动执行无关活跃项。用户只调用入口、要求“继续”，或没有给出具体任务时，才合并两侧“当前活跃需求”中未注释的条目；用户明确裁剪时以裁剪后的范围为准。

## 实施工作流

1. 判断任务属于需求、实现、排障、审查、Figma、API、i18n、原生构建还是发布，并定位 1～3 个最高价值事实源。
2. 实现前先确认当前行为；UI 读截图 / DOM / 真机，API 可由真实页面触发时先读 Network 实际请求与响应。
3. Figma URL、节点或设计还原任务必须先用 Figma MCP 读取目标节点；浏览器截图不能替代节点事实。
4. 代码任务依次完成真实业务改动、定向测试 / 验证，再更新项目外恢复文档；后续若仍需改代码，回到业务改动闭环。
5. 原生运行或构建仅在用户任务包含该动作时执行；先确认设备、平台、环境脚本和当前进程归属，避免影响其它项目或设备。
6. 开发阶段优先单文件、单用例或单平台验证；阶段收尾再按风险扩大测试矩阵。

## 项目工程约束

- 精确 React Native、React、Node、Gradle、依赖和脚本版本从当前仓库恢复，不在本 Skill 复制。
- 遵循项目现有 TypeScript strict、函数组件、Hooks、Context、样式、路径别名和原生 flavor 约定；不为统一形式改变运行语义。
- 第三方 SDK 或原生桥接字段先核对当前类型定义 / 官方平台说明；平台专属能力必须显式分支并提供另一端 fallback 或限制说明。
- 环境与构建使用仓库现有脚本和 Gradle / Xcode 配置；不要凭旧笔记复制 `.env`、切换 flavor 或改变签名流程。
- 医疗健康类用户可见文案避免确诊式或替代医嘱式表达。
- 不写入或输出密钥、token、Cookie、签名凭据、证书和真实敏感配置。
- 未经用户授权不做无关重构，也不假设 Heals、CS Mobile 或其它仓库与本项目结构相同。

## 文档与双入口维护

- 不把可从源码、测试、`package.json` 或项目规则恢复的版本、依赖表、命令表、目录地图、业务规则、API 字段和测试流水重复写入入口 Skill。
- 若本次任务改变稳定架构、命令工作流或仓库边界，在代码与定向验证稳定后自动最小更新 Codex 对口目录 `AGENTS.md`；否则不全仓扫描。外部合并造成的大规模变化使用 `/init-project` 刷新。
- 运行、构建和发布事实写入 `README.md` 或现有专项指南；阶段性结论不追加为 chat 流水。
- Cursor 与 Codex 入口的共同门禁、事实源优先级、执行范围和文档边界保持一致；只保留客户端名称、口令和用户目录路径差异。
- “当前活跃需求（不要修改这部分的子内容）”由用户维护；除非用户明确授权，不修改其文字、注释状态、层级或图片引用。
- 最终回复默认只说明产出、验证、风险和下一步；仅在用户要求、审查 / 排障需溯源、上下文缺失或慢任务复盘时列文件加载清单。

## 当前活跃需求(不要修改这部分的子内容)

<!-- - **Android / Google Play — 16KB 内存页大小**  
  - 场景：在 `android` 下构建 **prodRelease** AAB 并上传 Play Console 后出现 **Does not support 16 KB** / 原生库未对齐 16KB 页面等提示。  
    - 之前的具体报错是 Libraries that do not support 16 KB:
      base/lib/arm64-v8a/libHealthyMonitor.so
      base/lib/arm64-v8a/libabsl.cr.so
      base/lib/arm64-v8a/libbloodsuger.so
      base/lib/arm64-v8a/libbodytemp.so
      base/lib/arm64-v8a/libc++_chrome.cr.so
      base/lib/arm64-v8a/libc++_shared.so
      base/lib/arm64-v8a/libchrome_zlib.cr.so
      base/lib/arm64-v8a/libfbjni.so
      base/lib/arm64-v8a/libhermes.so
      base/lib/arm64-v8a/libhermestooling.so
      base/lib/arm64-v8a/libicuuc.cr.so
      base/lib/arm64-v8a/libimagepipeline.so
      base/lib/arm64-v8a/libjsi.so
      base/lib/arm64-v8a/liblibox.so
      base/lib/arm64-v8a/libnative-filters.so
      base/lib/arm64-v8a/libnative-imagetranscoder.so
      base/lib/arm64-v8a/liboxygen.so
      base/lib/arm64-v8a/libpartition_alloc.cr.so
      base/lib/arm64-v8a/libpdfium.cr.so
      base/lib/arm64-v8a/libpdfiumandroid.so
      base/lib/arm64-v8a/libreactnative.so
      base/lib/arm64-v8a/libreanimated.so
      base/lib/arm64-v8a/librnscreens.so
      base/lib/arm64-v8a/libworklets.so
      base/lib/x86_64/libHealthyMonitor.so
      base/lib/x86_64/libNskAlgo.so
      base/lib/x86_64/libabsl.cr.so
      base/lib/x86_64/libbloodsuger.so
      base/lib/x86_64/libbodytemp.so
      base/lib/x86_64/libc++_chrome.cr.so
      base/lib/x86_64/libc++_shared.so
      base/lib/x86_64/libchrome_zlib.cr.so
      base/lib/x86_64/libconceal.so
      base/lib/x86_64/libfbjni.so
      base/lib/x86_64/libhermes.so
      base/lib/x86_64/libhermestooling.so
      base/lib/x86_64/libicuuc.cr.so
      base/lib/x86_64/libimagepipeline.so
      base/lib/x86_64/libjsi.so
      base/lib/x86_64/liblibox.so
      base/lib/x86_64/libnative-filters.so
      base/lib/x86_64/libnative-imagetranscoder.so
      base/lib/x86_64/libneuroskybpi.so
      base/lib/x86_64/liboxygen.so
      base/lib/x86_64/libpartition_alloc.cr.so
      base/lib/x86_64/libpdfium.cr.so
      base/lib/x86_64/libpdfiumandroid.so
      base/lib/x86_64/libreactnative.so
      base/lib/x86_64/libreanimated.so
      base/lib/x86_64/librnscreens.so
      base/lib/x86_64/libworklets.so
      Libraries that do not support 16 KB:
      base/lib/arm64-v8a/libHealthyMonitor.so
      base/lib/arm64-v8a/libbloodsuger.so
      base/lib/arm64-v8a/libbodytemp.so
      base/lib/arm64-v8a/libc++_shared.so
      base/lib/arm64-v8a/libfbjni.so
      base/lib/arm64-v8a/libhermes.so
      base/lib/arm64-v8a/libhermestooling.so
      base/lib/arm64-v8a/libimagepipeline.so
      base/lib/arm64-v8a/libjsi.so
      base/lib/arm64-v8a/liblibox.so
      base/lib/arm64-v8a/libnative-filters.so
      base/lib/arm64-v8a/libnative-imagetranscoder.so
      base/lib/arm64-v8a/liboxygen.so
      base/lib/arm64-v8a/libpdfiumandroid.so
      base/lib/arm64-v8a/libreactnative.so
      base/lib/arm64-v8a/libreanimated.so
      base/lib/arm64-v8a/librnscreens.so
      base/lib/arm64-v8a/libworklets.so
      base/lib/x86_64/libHealthyMonitor.so
      base/lib/x86_64/libNskAlgo.so
      base/lib/x86_64/libbloodsuger.so
      base/lib/x86_64/libbodytemp.so
      base/lib/x86_64/libc++_shared.so
      base/lib/x86_64/libconceal.so
      base/lib/x86_64/libfbjni.so
      base/lib/x86_64/libhermes.so
      base/lib/x86_64/libhermestooling.so
      base/lib/x86_64/libimagepipeline.so
      base/lib/x86_64/libjsi.so
      base/lib/x86_64/liblibox.so
      base/lib/x86_64/libnative-filters.so
      base/lib/x86_64/libnative-imagetranscoder.so
      base/lib/x86_64/libneuroskybpi.so
      base/lib/x86_64/liboxygen.so
      base/lib/x86_64/libpdfiumandroid.so
      base/lib/x86_64/libreactnative.so
      base/lib/x86_64/libreanimated.so
      base/lib/x86_64/librnscreens.so
      base/lib/x86_64/libworklets.so
      ,经过我之前修改之后,目前只剩下如图![img_174548.png](img_174548.png)里的 `Linktop SDK` 相关的问题,
  - **本仓库事实源**：优先阅读并维护 `{workspace}/16KB_PAGE_SIZE_SOLUTION_GUIDE.md`（若已存在则以其为流程与结论主文档）。  
  - **可参考先例**：`D:\work\RN\amber-medical-app-rn\16KB_PAGE_SIZE_SOLUTION_GUIDE.md` 中的解决思路（迁移到本仓库时需按当前 Gradle、NDK、依赖版本调整）。  
  - 具体涉及的 `.so` 列表以 **Play 报错或本地分析结果** 为准，不必在 skill 内重复冗长清单。
  - 把你每轮的回答都用最精简的内容更新到 `{workspace}/16KB_PAGE_SIZE_SOLUTION_GUIDE.md`（业务仓库根：**Windows** `D:\work\RN\CircleAppNew`；**macOS** `/Users/<你的用户名>/Desktop/work/RN/circleapp`，当前 Mac：`/Users/stark/Desktop/work/RN/circleapp`）,保证每次开启新的chat后,都可以借助 这个文档 恢复这个项目的最小必要上下文;不要修改 **Windows** `%USERPROFILE%\.cursor\skills\ask-CircleAppNew\SKILL.md` / **macOS** `/Users/<你的用户名>/.cursor/skills/ask-CircleAppNew/SKILL.md` 的 `当前活跃需求` 里的内容 -->

# win
<!-- - 在业务仓库根目录执行（**Windows** `D:\work\RN\CircleAppNew`；**macOS** `/Users/<你的用户名>/Desktop/work/RN/circleapp`，当前 Mac：`/Users/stark/Desktop/work/RN/circleapp`）
  - `cd android; .\gradlew assembleRelease`
    -  `npm run android:dev_win` 把当前项目的debug模式 -->
  <!-- - 的app运行到了如图![img_114112.png](img_114112.png)![img_114124.png](img_114124.png)型号的真机上,真机所在的时区是 `东八区` -->
<!-- - 我现在想 构建 这个项目的 prod 环境的 `.aab` 文件 ; 是否需要先 copy `.env.production` to `.env`,再 执行 `./gradlew bundleProdRelease `; 还是直接执行  `./gradlew bundleProdRelease `? -->

# mac
  - 需要你在 Mac 系统的当前项目根目录执行一条命令(`npm run android:dev`),把当前项目dev环境的debug模式的apk运行到如图![img_114112.png](img_114112.png)![img_114124.png](img_114124.png)型号的真机上,真机所在的时区是 `东八区`真机上
  - 之前在win系统执行的是`npm run android:dev_win`
