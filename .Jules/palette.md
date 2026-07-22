## 2026-07-22 - Embed Copy Button Overlay & Textarea UX
**Learning:** Textareas with absolute overlay copy buttons must use `resize: none` to prevent layout breakage from manual resize. Immediate visual feedback with a clearable timeout and success color (#059669) creates high-delight interactive moments.
**Action:** Always disable textarea resizing when using overlay actions. Implement clearable timeouts (`clearTimeout(copyTimeout)`) to handle rapid subsequent clicks cleanly.

## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.
