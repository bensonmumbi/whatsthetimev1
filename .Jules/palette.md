## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-31 - Semantic Interactive Elements & Focus Visibility
**Learning:** Using semantic `<button>` elements for FAQ toggles and selection grids, paired with explicit `:focus-visible` styles, significantly improves keyboard navigability. Standardizing CSS resets for these buttons preserves visual design while meeting accessibility standards.
**Action:** Audit 'onclick' handlers on non-interactive elements (divs, spans) and convert them to semantic buttons with resets. Ensure global focus visibility is never suppressed.
