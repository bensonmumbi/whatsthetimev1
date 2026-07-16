## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-16 - Visual Feedback for Clipboard Actions
**Learning:** Adding immediate visual feedback (like "Copied!" text and color change) for clipboard actions provides crucial confirmation to the user, especially when the interaction is otherwise silent.
**Action:** Implement "Copied!" feedback and reset the button state after a short delay (e.g. 2s) for all copy-to-clipboard interactions.
