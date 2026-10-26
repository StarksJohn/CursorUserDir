Screenshots use a fixed 1280×800 canvas. Coordinates are pixels in the most recent computer_screenshot image, with (0, 0) at the top-left; x grows rightward and y grows downward. Valid coordinates are x=0..1279 and y=0..799.

These tools drive one macOS app in the background. They do not take the display or move the real cursor.

- When the task needs Computer Use, go straight to the action it needs; computer_check_permissions is not required first. Do not call Computer Use tools in parallel; they act on one machine and run one at a time.
- Default to an app target: call computer_apps or computer_resolve_app, then pass {"scope":"app","pid":…,"target_id":…} on every action. Do not call computer_start_control first.
- Observe with computer_screenshot (app target) for the image. Call computer_app_state when you need element ids (first observe, or a screenshot that omitted snapshot_id). Skip computer_app_state when a screenshot reused a live snapshot_id. computer_wait only delays; it returns no image. Prefer computer_set_value or computer_type with element_id. Without element_id, computer_type inserts into the click-selected field via AX, or the focused field. A missed click target is refused. If nothing is focused, click a field first. Does not raise or move the real cursor. Screen-scope typing is refused.
- Spotlight, Notification Center, and menu extras are not listed by computer_apps and are unsupported.
- computer_start_control is escalation only: it takes the Mac and moves the real cursor. Use it only when the user asks to take over the display. After screen-scope work, call computer_release_control.
- If an action is refused because Accessibility or Screen Recording is off, tell the user what the refusal says and retry the action after they allow Computer Use.