## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-01 - DOM Lookup and Object Allocation in High-Frequency Loops
**Learning:** In a 1s `setInterval` loop, `document.getElementById` and `document.querySelectorAll` calls, as well as `new Date()` allocations, can add up to measurable overhead, especially when multiplied by dozens of elements (like world clocks). A lazy element cache and passing a single `Date` object through the call stack significantly improves efficiency.
**Action:** Implement a global lazy `ELS` cache for IDs and cache `querySelectorAll` results globally. Pass the current time as a `Date` object to all helper functions within the loop to avoid redundant allocations.
