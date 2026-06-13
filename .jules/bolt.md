## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-13 - Comprehensive tick() Loop Optimization
**Learning:** High-frequency loops (1Hz+) in vanilla JS benefit immensely from lazy DOM element caching (using an object + helper) and constant hoisting. Throttling non-essential visual updates (like HH:mm clocks or date labels) to once per minute reduces main-thread work significantly without impacting perceived accuracy.
**Action:** Implement a `getEl(id)` helper with a global `ELS` cache for performance-critical loops. Pass existing `Date` objects to helpers to avoid redundant allocations.
