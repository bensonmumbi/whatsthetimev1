## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-23 - JavaScript RegExp Replacement String Capture Group Reference Gotcha
**Learning:** In JavaScript `String.prototype.replace()`, specifying `$10` inside the replacement string is parsed by the engine as the tenth capture group, NOT group 1 followed by a literal "0". If less than 10 capture groups exist, it evaluates to an empty string.
**Action:** Always use a replacement function `(match, p1, p2) => p1 + '0' + p2` when you want to append a literal digit immediately after a capture group reference in a replacement string.
