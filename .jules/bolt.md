## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-19 - Throttling and Modern Intl Optimization
**Learning:** Significant performance gains (~71% reduction in tick time) were achieved by combining lazy DOM caching, hoisting static constants, and throttling low-precision updates (minute-level) within a high-frequency loop (second-level). Additionally, `Intl.DateTimeFormat` with `longOffset` is much more efficient than manual Date arithmetic for UTC offsets.
**Action:** In high-frequency loops, always identify which UI elements truly need every-tick updates and throttle the rest. Use modern Intl APIs for timezone calculations instead of complex manual parsing.
