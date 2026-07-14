## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-14 - Robust Cross-Page Component Navigation
**Learning:** In multi-"page" single-file applications, navigation helpers like `scrollTo` often fail if the target is in a hidden section. Automating the "show page" logic within the scroll helper based on the target's parent container makes global CTAs much more reliable.
**Action:** Use `el.closest('.page')` (or equivalent) in navigation utilities to automatically activate the correct view before attempting to scroll to a specific component.
