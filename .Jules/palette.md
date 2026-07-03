## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-03 - Embed Code UX & Modal Accessibility
**Learning:** Providing a dedicated "Copy" button for code snippets with immediate visual feedback (text/color change) is superior to just selecting text on click. Accessibility in modals (like Buy Me a Coffee) is often neglected, specifically associating labels with currency selects and custom inputs.
**Action:** Implement "Copy" buttons for code blocks. Audit all modals and form sections for missing `for`/`id` associations.
