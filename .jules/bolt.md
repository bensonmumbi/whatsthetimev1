## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-30 - Efficient DOM Caching and Throttling
**Learning:** Redundant calls to even a cached element lookup (e.g., `if(getEl(x)) getEl(x)....`) are less efficient than single assignment to a local variable. Throttling non-second updates (Date, Timezone name, World Clock) within a 1s loop provides a massive performance boost (~90%+ reduction in execution time) compared to micro-optimizing lookups alone.
**Action:** Always assign cached lookups to local variables in hot loops. Prioritize throttling logical updates over micro-optimizing DOM access for cold paths.
