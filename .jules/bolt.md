## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-06 - Optimized UTC Offset and Main Loop Throttling
**Learning:** Manual date arithmetic for UTC offsets (formatting two dates and subtracting) is 3x slower than using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'`. Additionally, throttling non-second updates in a 1Hz loop significantly reduces scripting overhead without affecting user experience.
**Action:** Use `formatToParts` with `longOffset` for timezone offsets. Always throttle DOM updates based on the required precision of the displayed data.
