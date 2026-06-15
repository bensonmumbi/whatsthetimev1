## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-15 - Multi-layered Optimization of High-Frequency Loops
**Learning:** In 1s `setInterval` loops, the bottleneck isn't just expensive API calls like `Intl.DateTimeFormat`, but also cumulative DOM lookups (`getElementById`, `querySelectorAll`) and redundant object allocations. Lazy DOM caching combined with aggressive throttling of all non-second UI elements can reduce execution time by over 90%.
**Action:** Implement lazy DOM caching for all elements in hot loops. Hoist static arrays (like DAYS/MONTHS) and reuse state objects (like `Date`) across helper functions to minimize GC pressure.
