## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-04 - High-Frequency Loop Optimization (tick)
**Learning:** In a 1Hz loop like `tick()`, DOM lookups (`getElementById`) and redundant object instantiations (`new Date()`, `[]`, `{}`) are major performance drains. Using `formatToParts` with `longOffset` is significantly faster than calculating timezone offsets via date math.
**Action:** Use a lazy DOM cache (`ELS`) and hoist all constants/options. Pass existing `Date` objects to helpers. Use `longOffset` for UTC offsets. Average `tick()` execution time reduced from 0.026ms to 0.005ms (~80% improvement).
