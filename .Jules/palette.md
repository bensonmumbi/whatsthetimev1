## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-11-06 - Accessible Modal Keyboard Navigation and ARIA Semantics
**Learning:** Custom overlay modals without dialog semantics and keyboard traps leave screen reader and keyboard users stranded. Adding `role="dialog"`, `aria-modal="true"`, `aria-labelledby`, focusing the initial actionable element on open, listening for `Escape` to close, and restoring focus to the trigger element transforms the modal into a seamless accessible experience.
**Action:** When implementing or refining overlays/modals, always include dialog ARIA attributes, initial focus management, Escape key listener, and focus restoration to the trigger element.
