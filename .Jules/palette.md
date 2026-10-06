## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-14 - Interactive Anchors Keyboard Focus & Focus Visible Outline
**Learning:** In HTML, `<a>` elements missing an `href` attribute are omitted from native browser tab order, rendering them inaccessible to keyboard-only users. Additionally, relying on default browser focus indicators often fails visual contrast checks across dark or custom themed headers/footers.
**Action:** Always ensure interactive anchor elements use `href="javascript:void(0)"` (or standard URLs) and implement explicit `*:focus-visible` CSS rules with accent outline styles.
