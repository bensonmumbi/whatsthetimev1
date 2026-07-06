## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-06 - Embed Code Copy Button with Visual Feedback
**Learning:** Providing a "Copy" button for code snippets with immediate visual feedback ("Copied!") improves user confidence and streamlines the sharing workflow. Using a relative container for the button overlay keeps the UI compact.
**Action:** Include copy-to-clipboard functionality for any technical snippets or shareable links. Ensure proper timeout management to revert button state.
