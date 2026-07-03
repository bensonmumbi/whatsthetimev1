## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-03 - Optimizing High-Frequency tick() Loop
**Learning:** Redundant DOM lookups and array allocations in a 1Hz loop (like a clock) consume unnecessary CPU cycles. Throttling updates for UI elements that only change once a minute (Date, Week Number, etc.) significantly reduces main-thread pressure.
**Action:** Use a lazy DOM caching helper (getEl) and throttle all non-second updates in high-frequency loops. Hoist constant arrays (like month/day names) outside the function scope.
