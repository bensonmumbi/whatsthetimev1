## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-18 - Semantic Buttons & Global Focus Visibility
**Learning:** Using semantic `<button type="button">` elements instead of action-less anchors (`<a>`) provides native keyboard activation (Enter and Space) and better screen reader announcements. Global focus indicators via `:focus-visible` ensure accessibility without cluttering the UI for mouse users.
**Action:** Never use `<a>` for actions that don't change the URL. Always provide a clear focus indicator and avoid `outline: none`.
