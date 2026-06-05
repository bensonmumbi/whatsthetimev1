## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-05 - Semantic Buttons for Selection Cards
**Learning:** Using `div` elements for selection controls (like donation amounts) breaks keyboard accessibility. Converting them to `<button type="button">` with CSS resets preserves design while enabling tab navigation and screen reader support.
**Action:** Identify interactive "cards" or "tiles" and ensure they use semantic `<button>` elements. Use `appearance: none` and `background: none` for clean resets.
