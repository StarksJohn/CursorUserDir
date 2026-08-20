# React Native Verification Reference

只执行与当前改动相关的命令，并用真实值替换示例变量。产物优先写入临时目录或项目已忽略的验证目录，不提交包含账号、通知或医疗数据的截图、层级和日志。

## Android

### Target and runtime

```bash
adb devices -l
adb -s "$SERIAL" shell getprop ro.product.model
adb -s "$SERIAL" shell getprop ro.build.version.release
adb -s "$SERIAL" shell wm size
adb -s "$SERIAL" shell wm density
adb -s "$SERIAL" shell settings get system font_scale
adb -s "$SERIAL" shell pidof "$APP_ID"
adb -s "$SERIAL" shell dumpsys window
```

从 `dumpsys window` 结果核对 `mCurrentFocus`/`mFocusedApp`，不要只根据启动命令判断页面已显示。

### Screenshot and hierarchy

```bash
mkdir -p "$ARTIFACT_DIR"
adb -s "$SERIAL" exec-out screencap -p > "$ARTIFACT_DIR/state.png"
adb -s "$SERIAL" shell uiautomator dump /sdcard/rn-ui-window.xml
adb -s "$SERIAL" pull /sdcard/rn-ui-window.xml "$ARTIFACT_DIR/window.xml"
adb -s "$SERIAL" shell rm /sdcard/rn-ui-window.xml
```

检查 `window.xml` 中目标元素的 `text`、`resource-id`、`content-desc`、`bounds`、`enabled`、`clickable`、`selected`。层级缺失时检查组件是否暴露 accessibility/testID，不得假定元素不存在。

### Interaction and recording

```bash
adb -s "$SERIAL" shell input tap "$X" "$Y"
adb -s "$SERIAL" shell input text "$TEXT"
adb -s "$SERIAL" shell input keyevent KEYCODE_BACK
adb -s "$SERIAL" shell screenrecord --time-limit 30 /sdcard/rn-ui-flow.mp4
adb -s "$SERIAL" pull /sdcard/rn-ui-flow.mp4 "$ARTIFACT_DIR/flow.mp4"
adb -s "$SERIAL" shell rm /sdcard/rn-ui-flow.mp4
```

坐标交互只用于临时 smoke check。可重复流程应使用稳定 identifier 的项目 E2E。

### Scoped logs

先记录目标进程，再对本次操作使用短时间窗口：

```bash
APP_PID="$(adb -s "$SERIAL" shell pidof "$APP_ID" | tr -d '\r')"
adb -s "$SERIAL" logcat --pid="$APP_PID" -T 5m -d -v threadtime
```

限制输出并重点检查 `FATAL EXCEPTION`、`AndroidRuntime`、`ANR`、JS exception、unhandled rejection、权限和资源错误。不要默认清空设备的全部日志。

## iOS Simulator

```bash
xcrun simctl list devices booted
xcrun simctl io "$UDID" screenshot "$ARTIFACT_DIR/state.png"
xcrun simctl io "$UDID" recordVideo "$ARTIFACT_DIR/flow.mov"
xcrun simctl launch "$UDID" "$BUNDLE_ID"
xcrun simctl get_app_container "$UDID" "$BUNDLE_ID" app
```

停止录屏使用 `Control-C`。日志使用短时间范围和目标进程/子系统 predicate，避免输出整机日志。真机优先使用项目既有 Xcode/自动化流程；不要把 simulator 通过写成真机通过。

## Existing E2E Tools

每个 React Native 项目任务先检测能力层级：

```bash
python3 "$HOME/.cursor/skills/react-native-ui-verification/scripts/check_toolchain.py" \
  "$PROJECT_ROOT"
```

输出中的 `globalAvailable` 只表示命令可用，`projectConfigured` 只表示仓库存在集成材料。检测脚本不会把任何工具标记为 `currentRunVerified`；只有本次针对当前构建执行相应测试并成功，才能在最终证据报告中人工记录为已验证。

先读取项目配置和脚本，不猜命令：

- Detox：全局 `detox-cli` 只转发到项目本地 `detox`；需要仓库依赖、`.detoxrc`、原生 build configuration 和测试。
- Maestro：全局 CLI 可直接驱动 accessibility，但稳定 E2E 仍需要项目内针对 app ID、状态和断言编写的 flow。
- Appium：全局 server/Driver 仍需要项目 client、capabilities、测试数据和断言；只启动 server 不是 E2E。

若项目没有 E2E，不因单次 UI 修改擅自引入框架。关键流程需要长期回归时，向用户说明维护成本、目标平台和测试数据后再安装。

## Visual Difference

当前 Skill 提供 Pillow 工具：

```bash
python3 "$HOME/.cursor/skills/react-native-ui-verification/scripts/compare_images.py" \
  "$EXPECTED_IMAGE" \
  "$ACTUAL_IMAGE" \
  --output "$ARTIFACT_DIR/diff.png"
```

需要按已确认阈值判定时：

```bash
python3 "$HOME/.cursor/skills/react-native-ui-verification/scripts/compare_images.py" \
  "$EXPECTED_IMAGE" \
  "$ACTUAL_IMAGE" \
  --output "$ARTIFACT_DIR/diff.png" \
  --channel-threshold 16 \
  --max-diff-ratio 0.01
```

只有设备、截图尺寸、主题、语言、字体缩放、动态数据、系统栏和裁剪范围一致时，差异比例才有可比性。工具退出码：

- `0`：分析完成，且指定判定阈值时未超标。
- `1`：差异比例超过指定 `--max-diff-ratio`。
- `2`：输入、尺寸、裁剪或依赖错误。

## Evidence Report

```text
结论: 通过 | 部分通过 | 阻塞 | 不适用
范围: <平台、设备、app ID、环境、页面/流程>
静态检查: <命令与结果>
运行目标: <构建/安装/进程/前台页面证据>
交互断言: <步骤与可观察结果>
结构检查: <identifier/text/bounds/state>
视觉检查: <截图、Figma/基准、差异指标>
运行日志: <时间窗口与相关错误>
未覆盖: <平台、设备、状态、外部条件>
```
