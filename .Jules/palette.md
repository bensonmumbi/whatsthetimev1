## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-18 - Keyboard Navigation and Focus States
**Learning:** `<a>` tags without `href` are not keyboard-focusable by default in many browsers. Using `href="javascript:void(0)"` combined with `onclick` is a safe way to make them focusable without triggering page reloads or jumps. Additionally, a global `:focus-visible` outline is essential for keyboard users to navigate effectively.
**Action:** Ensure all interactive elements (links, buttons) are in the tab order. Always implement a clear, consistent `:focus-visible` style across the application.
