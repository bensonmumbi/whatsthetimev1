## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-24 - Comprehensive tick() Optimization
**Learning:** Lazy DOM caching combined with throttling non-critical updates and hoisting constants can reduce main-thread execution time by over 80% in high-frequency loops. Ensuring the cache handles null results (using `in` operator) prevents repeated failing lookups. Reusing the `Date` object across sub-functions further reduces allocation overhead.
**Action:** Implement a robust `getEl` helper and move all non-second-precision logic into throttled blocks. Pass the existing `Date` object to utility functions to avoid redundant `new Date()` calls.
