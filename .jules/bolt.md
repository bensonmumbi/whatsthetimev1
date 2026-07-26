## 2026-07-26 - Hourly Cache for Timezone Offset Calculations
**Learning:** Computing UTC timezone offsets by instantiating Date objects with formatted strings and performing arithmetic/parsing operations is highly inefficient. Extracting timezone offsets via `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` is much cleaner, and caching the computed offsets hourly completely avoids recurring lookup overhead in ticking clock loops.
**Action:** Use `longOffset` formatToParts in `Intl.DateTimeFormat` to retrieve timezone offset strings directly. Memoize timezone offset calculations using an hourly-invalidating key to ensure both extreme speed and safe daylight saving time (DST) transitions.

## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).
