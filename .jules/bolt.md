## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-29 - Optimized High-Frequency Loops and DOM Access
**Learning:** Performance in high-frequency loops (like a 1s clock tick) can be significantly improved by implementing lazy DOM caching, hoisting static constants (like day/month arrays), and throttling updates that don't require second-precision (like UTC offsets or week numbers). Reducing object allocations (e.g., reusing Date objects) also lowers memory pressure.
**Action:** Implement a lazy DOM cache (e.g., a 'getEl' helper) and throttle non-essential updates in recurring functions to minimize main-thread work.
