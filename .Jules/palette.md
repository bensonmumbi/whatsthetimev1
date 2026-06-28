## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-28 - Clipboard Feedback & ARIA Live
**Learning:** Providing immediate visual and audible feedback for clipboard actions (like "Copy" buttons) is crucial for UX. Using `aria-live="polite"` ensures screen reader users are informed of state changes that don't involve a page reload. Managing timers for transient UI states prevents overlapping transitions.
**Action:** Always include a feedback state for "Copy" actions. Use `aria-live` for dynamic text updates. Ensure timers for feedback states are properly cleared if the action is repeated.
