## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-06 - Support Modal Keyboard Focus and Selection Accessibility
**Learning:** Selecting items within modal overlays (such as support donation levels) should use semantic `<button>` elements instead of clickable `<div>` elements to guarantee standard tab stop ordering and spacebar/enter execution. Additionally, adding a global high-contrast `:focus-visible` rule using current accent/theme tokens delivers a top-tier keyboard navigation experience without style pollution on default mouse clicks.
**Action:** Always refactor grid-based selection lists into semantic buttons, resetting base button styles gracefully via CSS. Define a strong `:focus-visible` outline for maximum keyboard clarity.
