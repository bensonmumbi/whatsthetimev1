## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-30 - Keyboard Accessibility & Focus Visibility Patterns
**Learning:** In SPAs using vanilla JS `onclick` handlers, non-semantic triggers (like `div`) must be converted to `button` elements and navigation links need `href="javascript:void(0)"` to be keyboard-accessible. A global `:focus-visible` rule combined with button CSS resets ensures accessibility without sacrificing design.
**Action:** Use `<button type="button">` with appearance/background/border resets for any custom interactive components. Apply a global `:focus-visible` outline to provide clear feedback for keyboard users.
