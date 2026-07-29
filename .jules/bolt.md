## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-29 - Ultra-High Performance tick() Loop with Lazy DOM Caching and Memoized formatToParts Timezone Offsets
**Learning:** Combining lazy DOM element caching (with a Map-backed `getEl()` function), constant array hoisting, and caching timezone offsets using `OFFSET_CACHE` (with `longOffset` `formatToParts()`) reduces the `tick()` function overhead by over 94% (reducing time from ~0.087ms to ~0.0045ms). This avoids redundant string formatting, double-Date instantiation, and GC thrashing.
**Action:** Cache non-existing DOM queries to avoid continuous unsuccessful lookup overhead. Share a single `Date` reference down to helper functions to avoid redundant object instantiation.
