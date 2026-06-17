## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-17 - BMC Modal Accessibility & Focus Indicators
**Learning:** Selection grids often use clickable 'cards' (divs) which are invisible to keyboard users. Converting these to semantic buttons and adding custom focus-visible outlines matching the brand identity provides both accessibility and visual delight.
**Action:** When implementing selection grids or modals, ensure interactive elements use the <button> tag and have explicit :focus-visible states that align with the brand's color palette.
