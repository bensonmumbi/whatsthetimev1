## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).
## 2026-07-12 - Optimizing high-frequency tick() loop
**Learning:** Average execution time of the `tick()` function was reduced from ~0.060ms to ~0.012ms (~80% improvement) by implementing lazy DOM caching, hoisting constants, and throttling non-second updates. Manual date arithmetic for UTC offsets is significantly slower than using `Intl.DateTimeFormat` with `longOffset`.
**Action:** Always throttle UI updates that don't require second-precision in high-frequency loops. Use `getEl(id)` pattern for lazy DOM caching to avoid redundant lookups.
