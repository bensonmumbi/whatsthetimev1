## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-21 - Cross-Page Element Navigation & Smooth Scrolling
**Learning:** In multi-page layouts where elements are hidden/shown dynamically, cross-page jump-links (e.g. hero CTAs scrolling to specific sections on other pages) fail when pages are hidden. Detecting the target element's parent page dynamically and switching pages with an option to skip scroll-to-top prevents layout jumps and ensures smooth scrolling works flawlessly.
**Action:** Use `el.closest('.page')` to dynamically activate the target page before smooth-scrolling, and accept a `skipScroll` parameter to prevent page switching from forcefully resetting scroll position.
