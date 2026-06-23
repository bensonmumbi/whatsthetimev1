## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-23 - DOM Caching and Throttling for Clock Performance
**Learning:** Repeated `document.getElementById` calls in a 1s interval loop add unnecessary overhead. Throttling secondary UI updates (date, timezone offset, week number) to once per minute while keeping only high-precision elements (seconds, Unix timestamp) on the 1s path yields an ~85% speedup in `tick()` execution time.
**Action:** Implement lazy DOM element caching using a simple `getEl(id)` helper and move non-second updates into a `minuteChanged` block.
