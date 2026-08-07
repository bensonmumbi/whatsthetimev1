## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-07 - Interactive Embed Copy Pattern & UI Transitions
**Learning:** Implementing an absolute-positioned Copy button inside code-embed block containers significantly improves user convenience compared to simple manual selection. Green success transitions (`#059669`) with 2-second timeout resets provide excellent visual feedback for async/interactive actions.
**Action:** Use absolute positioning and padding offsets on copyable code containers to house copy buttons neatly. Ensure the copy action uses `navigator.clipboard` with clear fallback options for standard/legacy browser compatibility, and provide aria-labels for assistive screen reader navigation.
