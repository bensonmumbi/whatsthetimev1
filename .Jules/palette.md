## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-26 - Semantic Buttons for Interactive Elements
**Learning:** Using `<div>` with `onclick` for interactive elements (like FAQ accordions or selection cards) breaks keyboard accessibility. Screen readers and keyboard users rely on semantic `<button>` elements or links with `href` to identify and interact with controls.
**Action:** Always use `<button type="button">` for non-link interactive elements and apply CSS resets to maintain the design.
