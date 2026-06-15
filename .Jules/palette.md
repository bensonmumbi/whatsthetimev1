## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-15 - Floating Action Button & Sticky Ad Collision
**Learning:** Floating Action Buttons (FABs) like "Buy Me a Coffee" often collide with sticky advertisement banners or mobile navigation bars. A fixed offset (e.g., `bottom: 70px`) is necessary to ensure visibility and prevent accidental clicks on ads.
**Action:** When a project uses sticky bottom elements, audit the positioning of all floating UI components to ensure they clear the sticky zone.
