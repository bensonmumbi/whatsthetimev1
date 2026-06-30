## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-30 - Standardizing Timezone Offsets and DOM Caching
**Learning:** Using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` is significantly more efficient than manual date arithmetic for calculating UTC offsets. However, the output varies by environment (e.g., "GMT+5", "GMT+0500"), requiring regex normalization to maintain a consistent "UTC+/-HH:MM" format. Lazy DOM element caching further reduces overhead in high-frequency loops.
**Action:** Use a helper like `getEl(id)` to cache DOM references and a standardized `utcOff` function with regex-based normalization for all timezone displays.
