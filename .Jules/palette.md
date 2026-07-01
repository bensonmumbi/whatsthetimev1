## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-01 - Accessibility for Grouped Inputs & Interaction Feedback
**Learning:** Grouped inputs (like a time input and a timezone selector) often share a single visual label, which only associates with one element via 'for'. Using 'aria-label' on the other elements provides necessary context for screen readers. Interaction feedback (like a "Copied!" state) significantly improves the perceived utility of utility buttons.
**Action:** When seeing grouped inputs, ensure all are accessible via either explicit labels or ARIA labels. Always provide visual confirmation for clipboard actions.
