## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-28 - Minimizing Allocation and DOM Access in High-Frequency Loops
**Learning:** Beyond caching expensive formatters, minimizing object allocations (like `new Date()`) and DOM access (via lazy caching) in 1s intervals provides a massive performance boost. Hoisting static arrays like day/month names prevents redundant memory pressure.
**Action:** In high-frequency loops, use a shared Date object for all sub-calculations and implement a lazy DOM cache (`ELS` object) to eliminate redundant `document.getElementById` calls.
