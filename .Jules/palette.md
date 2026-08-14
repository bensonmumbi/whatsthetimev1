## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-14 - Interactive Anchors without Href and Focus Indicators
**Learning:** Anchor tags without an `href` attribute are excluded from the browser's tab order and are completely inaccessible to keyboard-only users. Re-introducing `href="javascript:void(0)"` restores standard keyboard tab accessibility. Combining this with a global `*:focus-visible` outline using the app's accent color produces an intuitive and highly visible keyboard focus state.
**Action:** Always verify that interactive `<a>` elements possess an `href` attribute and check for visible focus styles across all key navigation paths.
