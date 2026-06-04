## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-04 - Semantic Buttons for Interactive Elements
**Learning:** Using `div` with `onclick` for interactive elements like FAQ toggles or selection cards is a common accessibility trap. It breaks keyboard navigation and screen reader role identification.
**Action:** Convert non-semantic interactive `div` elements to `<button type="button">`. Apply CSS resets (`appearance: none`, `background: none`, `font: inherit`, etc.) to maintain visual parity. Always add `aria-expanded` for collapsible sections.
