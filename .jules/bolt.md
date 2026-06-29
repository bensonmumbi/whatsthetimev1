## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-29 - High-Frequency Loop Optimization (tick)
**Learning:** In high-frequency loops (1Hz+), `document.getElementById` and redundant object instantiation (`new Date()`, static arrays) create measurable overhead. Combining lazy DOM caching with update throttling for non-critical elements (e.g., minute-precision fields) can yield massive performance gains (>90% execution time reduction). Additionally, `Intl.DateTimeFormat` with `longOffset` is significantly faster for UTC offset retrieval than manual string manipulation or multi-date arithmetic.
**Action:** Use a centralized `ELS` cache for DOM elements. Hoist static arrays and constants. Throttle all non-second updates. Pass existing `Date` objects to sub-functions to avoid redundant instantiation.
