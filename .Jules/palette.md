## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-28 - Keyboard Accessibility & Semantic Buttons
**Learning:** In SPAs using custom-styled interactive elements (like FAQ accordions or selection cards), using `div` with `onclick` breaks keyboard navigation. Converting them to semantic `<button type="button">` with CSS resets restores accessibility without changing the design. A global `:focus-visible` rule is essential for visibility.
**Action:** Audit all clickable `div` or `span` elements and convert to buttons. Ensure all `<a>` tags have `href` (even if `javascript:void(0)`) to be in the tab order.
