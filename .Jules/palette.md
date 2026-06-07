## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-07 - Accessible FAQ & Global Focus Indicators
**Learning:** Using non-semantic `div` elements for interactive accordions (like FAQs) completely breaks keyboard navigation and screen reader support. Implementing `:focus-visible` provides a high-contrast focus indicator for keyboard users while remaining invisible to mouse users, maintaining aesthetic polish.
**Action:** Always use semantic `<button>` elements for accordions and toggles. Pair them with `aria-expanded` to communicate state. Use `:focus-visible` globally to ensure accessibility without "ugly" focus rings for mouse users.
