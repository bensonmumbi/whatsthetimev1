## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-16 - DOM Caching and Throttling for High-Frequency Loops
**Learning:** In a 1s clock loop, redundant DOM lookups and unthrottled updates of minute-precision data (like city times and UTC offsets) consume unnecessary CPU cycles. Using `Intl.DateTimeFormat` with `longOffset` is significantly more efficient than manual string parsing for timezone offsets.
**Action:** Use a lazy-loading DOM cache for frequently accessed elements and throttle any UI update that doesn't change every second. Prefer built-in `Intl` features over manual date arithmetic.
