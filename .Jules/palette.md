## 2026-07-28 - SPA Navigation Keyboard Focusability & Focus Visible Indicator
**Learning:** When using click-only SPA navigation anchors, omitting `href` prevents elements from joining the document tab order. Additionally, without explicit `:focus-visible` outline styles, keyboard users cannot visually trace their focused location.
**Action:** Always specify `href="javascript:void(0)"` for custom action anchors to ensure native focusability, and define global `*:focus-visible` outline offsets with the theme accent color for premium visual accessibility.

## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.
