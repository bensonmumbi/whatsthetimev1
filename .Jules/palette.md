## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-16 - Focus Visibility & Clipboard UX
**Learning:** Removing `outline: none` is a critical accessibility fix. Providing immediate visual feedback (icon/color change) for clipboard operations significantly improves the perceived responsiveness of utility features.
**Action:** Never use `outline: none` without providing a themed `:focus-visible` alternative. Always implement success states for "Copy" buttons.
