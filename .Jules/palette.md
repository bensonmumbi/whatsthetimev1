## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-21 - Copy to Clipboard & Robust SPA Navigation
**Learning:** Providing quick-copy buttons for technical data (like Unix timestamps) is a high-impact micro-UX. In a multi-page SPA, navigation helpers like `scrollTo` must ensure the correct logical "page" is active before attempting to scroll to an element.
**Action:** Identify technical fields that users might want to copy. Ensure `scrollTo` functions are context-aware of SPA page states.
