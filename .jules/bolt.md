## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-19 - Safe DOM Caching and Throttling in Vanilla JS
**Learning:** Top-level DOM queries (e.g., `document.getElementById`) can fail if the script is loaded before the DOM is fully parsed. Additionally, caching `NodeList` or element references can lead to stale data if the DOM is dynamically updated (e.g., via `innerHTML`).
**Action:** Implement lazy initialization for DOM caches (e.g., a `getEl` helper). Explicitly reset or invalidate cached DOM collections (set to `null`) whenever the associated DOM structure is modified or re-rendered to ensure updates target the correct elements.
