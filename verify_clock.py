import subprocess
import time
import sys
from playwright.sync_api import sync_playwright

def run_test():
    # Start local server
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
            page = context.new_page()
            page.goto("http://localhost:8000/whatsthetime.html")

            # Check main clock
            main_clock = page.locator("#mainClock")
            initial_time = main_clock.text_content()
            print(f"Initial Time: {initial_time}")

            # Wait for it to change
            time.sleep(1.5)
            new_time = main_clock.text_content()
            print(f"New Time: {new_time}")

            if initial_time == new_time:
                print("Error: Main clock is not ticking!")
                sys.exit(1)
            else:
                print("Success: Main clock is ticking.")

            # Check world cities
            cities = page.locator(".city-time").all()
            if len(cities) == 0:
                print("Error: No world cities found!")
                sys.exit(1)

            city_time = cities[0].text_content()
            if ":" not in city_time:
                print(f"Error: City time format invalid: {city_time}")
                sys.exit(1)
            print(f"First City Time: {city_time}")

            # Check UTC offset
            utc_off = page.locator("#utcOff").text_content()
            if "UTC" not in utc_off:
                print(f"Error: UTC offset invalid: {utc_off}")
                sys.exit(1)
            print(f"UTC Offset: {utc_off}")

            # Check Embed Clock Copy Button
            copy_btn = page.locator("#copyBtn")
            if copy_btn.count() == 0:
                print("Error: Copy button not found!")
                sys.exit(1)

            # Click the copy button
            copy_btn.click()
            time.sleep(0.5)

            # Check text content changes to "Copied!"
            btn_text = copy_btn.text_content()
            print(f"Copy Button Text after click: {btn_text}")
            if "Copied!" not in btn_text:
                print("Error: Copy button text did not change to 'Copied!'")
                sys.exit(1)
            print("Success: Copy button feedback works.")

            print("All basic clock checks passed.")

            # Keep it running for manual check if needed
            # page.screenshot(path="screenshot.png")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_test()
