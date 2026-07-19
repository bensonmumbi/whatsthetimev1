## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-19 - Standardizing Timezone Offsets and High-Frequency Throttling
**Learning:** Reconstructing timezone offsets manually using Date parsing of two formatted strings is extremely CPU-heavy in animation loops. Standardizing offset parsing via `Intl.DateTimeFormat` with `longOffset` formatToParts combined with throttling low-frequency updates (`datDisp`, `tzName`, `utcOff`, `weekNum`, `doy`, `qtr`) to run only when minutes change results in a ~67% to ~80% performance speedup (~0.04 ms down to ~0.008 ms).
**Action:** Use modern Intl longOffset and group low-frequency, non-second fields into minute-throttled sections in animation and interval loops.
