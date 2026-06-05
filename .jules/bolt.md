## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-05 - Holistic Loop Optimization (Caching, Hoisting, and Throttling)
**Learning:** Significant performance gains (~90% reduction in tick duration) in high-frequency loops are achieved by combining multiple micro-optimizations: lazy DOM element caching to avoid `document.getElementById`, hoisting static arrays out of functions to prevent re-allocation, reusing `Date` objects across helper functions, and aggressive throttling of non-second precision visual updates.
**Action:** When optimizing a `setInterval` or `requestAnimationFrame` loop, apply a multi-layered approach: cache DOM references lazily, hoist all constants, reuse temporary objects (like `Date`), and strictly separate high-frequency (1s) from low-frequency (1m) UI updates.
