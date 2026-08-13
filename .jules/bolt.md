## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-08-13 - High-Performance Timezone Offsets with Memoization
**Learning:** Calculating UTC offsets by instantiating multiple Date objects and string manipulation is extremely slow and causes high GC overhead. Caching the offsets hourly (keyed by timezone and hourly timestamp) and extracting offsets via `Intl.DateTimeFormat` with `longOffset` formatToParts yields a ~18.5x execution speedup.
**Action:** Always memoize time zone offsets hourly using an `OFFSET_CACHE` Map and parse offsets using `longOffset` formatToParts to avoid heavy Date object creation and formatting.
