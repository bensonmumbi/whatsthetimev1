## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-15 - Copy-to-Clipboard UX Feedback
**Learning:** Providing immediate visual feedback (e.g., "Copied!" with a color change) for copy actions is essential for user confidence. Using absolute positioning for copy buttons within textareas requires 'resize: none' to prevent UI breakage.
**Action:** Always implement a success state (text change + color) for copy-to-clipboard interactions. Use 'resize: none' on inputs with overlay actions.
