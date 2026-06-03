## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-03 - Semantic Buttons for Keyboard Accessibility & Sticky Clearance
**Learning:** Using `<a>` without `href` or `<div>` for interactive elements breaks keyboard navigation. Converting them to `<button type="button">` with CSS resets restores accessibility while preserving design. Floating elements need explicit clearance from other sticky UI components (like ads) to avoid overlap.
**Action:** Audit non-semantic interactive elements and convert them to buttons. Use `:focus-visible` for non-intrusive focus indicators. Verify floating element positioning against all possible sticky banners.
