## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-04 - Semantic Buttons & Copy Interaction
**Learning:** Converting interactive 'div' elements to semantic 'button' elements is a low-effort, high-impact accessibility win that provides built-in keyboard support. Adding a 'Copy' button with immediate visual feedback significantly reduces user friction for sharing snippets.
**Action:** Always audit for non-semantic interactive elements and replace them with buttons. Use 'Copied!' state changes to provide clear success feedback for clipboard actions.
