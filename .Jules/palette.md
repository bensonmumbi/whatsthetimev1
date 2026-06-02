## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-02 - Semantic HTML for Interactive Elements
**Learning:** Using non-semantic elements (like `div`) for interactive components (FAQs, selection cards) locks out keyboard and screen reader users. Simply adding `onclick` is not enough for accessibility.
**Action:** Always use semantic elements like `<button>` for actions and `<a>` (with `href`) for navigation. Ensure buttons have proper ARIA states (like `aria-expanded`) when toggling content.
