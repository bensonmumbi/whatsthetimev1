## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-10-17 - Direct UTC Offset Calculation and Main-Loop Throttling
**Learning:** Parsing formatted date strings back into `Date` objects inside high-frequency interval loops (like `setInterval(tick, 1000)`) introduces high overhead. Using `Intl.DateTimeFormat` with `{timeZoneName: 'longOffset'}` computes offsets directly without double `Date` parsing. Furthermore, moving non-second DOM updates (`datDisp`, `tzName`, `utcOff`, `weekNum`, `doy`, `qtr`) into per-minute throttled blocks achieves a ~5x speedup per tick (~81% reduction in per-second main thread execution time).
**Action:** Use `{timeZoneName: 'longOffset'}` for offset calculations and restrict `tick()` loops to only touch DOM elements that physically change every second.
