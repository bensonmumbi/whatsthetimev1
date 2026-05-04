# whatsthetime AI Coding Guidance

This repository is a single-page static website. The entire app is contained in `whatsthetime.html` with inline CSS, inline JavaScript, and a few static assets.

## What matters most

- `whatsthetime.html` is the source of truth. There is no separate `src/`, no bundler, no Node tooling, and no test framework in this repo.
- The site is client-side only: all logic runs in-browser, using `Date`, `Intl.DateTimeFormat`, and DOM updates.
- Event wiring is mostly inline via `onclick` attributes and direct DOM IDs/classes.
- CSS is embedded in the `<style>` block at the top of `whatsthetime.html`; keep edits there unless you intentionally refactor to external styles.

## Major components

- Navigation/page switching: `showPage(n)` toggles `.page.active` and updates nav button state.
- Clock/time page: `tick()` updates the main clock, date labels, UTC offset, ISO datetime, week/day/year values, and hero timezone strip every second.
- World cities: `CITIES` array drives `buildCities()`, and timezone offsets are computed via `utcOff(tz)`.
- Calendar: `renderCal()` builds the month grid in DOM, using date math and a simple full-moon heuristic.
- Build page interactions: contact form submission (`submitForm()`), FAQ toggles, and coffee support modal logic are all inline helpers.
- Time conversion: `calcConversion()` computes a timezone conversion from user input and updates `#convResult`.

## Project-specific patterns

- Use `document.getElementById(...)`, `querySelectorAll(...)`, and element `.dataset` values consistently.
- Many elements are identified by hard-coded IDs such as `mainClock`, `datDisp`, `heroTzStrip`, `citiesGrid`, `calGrid`, `bmcModal`, and `convResult`.
- The code uses inline `onclick` handlers in HTML. When changing behavior, update both the HTML trigger and the corresponding JS helper.
- There is no external dependency management. Avoid introducing npm-style assumptions unless you also add a new workflow and repo files.

## Debug / preview workflow

- Preview by opening `whatsthetime.html` in a browser, or serve the folder with any static file server.
- There is no package script or build command present in the repo.
- Assets referenced by the page include `build_page_bg.png`, `map.svg`, and `nw.svg`.

## Integration points

- Google Fonts are loaded from `fonts.googleapis.com` in the `<head>`.
- The page is self-contained; it does not call external APIs or make network requests other than font loading.
- Everything in the script block is executed on page load, ending with `buildCities(); renderCal(); tick(); calcConversion(); setInterval(tick,1000);`.

## When editing

- Preserve the single-file nature unless you intentionally refactor the site structure.
- Keep DOM IDs stable when modifying logic, since many functions rely on them directly.
- If you add new user-facing text or sections, update both HTML and the corresponding JavaScript helper if it depends on the DOM.
- Do not assume a modern module build pipeline; any new code should run in a plain browser environment.

## Notes

- `checklist.md` and `Inventorymanagment.md` are repository documents, but the app itself is `whatsthetime.html`.
- There are no existing `.github` or AI agent guidance files in this repo before this addition.
