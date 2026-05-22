## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-22 - Inline Handlers and Element Referencing
**Learning:** When using inline `onclick` handlers in HTML, passing `this` to the function is the most reliable way to reference the triggering element. Relying on `event.currentTarget` inside the function can fail in some contexts as it might be `null`.
**Action:** Always pass `this` to inline handlers if the function needs to modify or reference the triggering element (e.g., for visual feedback).
