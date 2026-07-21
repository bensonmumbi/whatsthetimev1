## 2026-07-21 - Lazily Caching DOM Elements, Array Hoisting, and Throttling
**Learning:** High-frequency clock tick functions can be optimized up to 5x (~80% execution time reduction) by combining three patterns: (1) Lazily caching DOM elements with a `getEl(id)` Map, (2) Hoisting static lookup arrays (`D_NAMES`, `M_NAMES`) out of the function scope, and (3) Throttling lower-precision display updates (like dates and zone names) to evaluate only when the minute changes.
**Action:** Apply the lazy DOM caching, hoisting, and throttled update pattern to any real-time tick or animation loop.

## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).
