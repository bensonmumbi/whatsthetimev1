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
            page = browser.new_page()
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

            # Grant clipboard permission in context for chrome
            context = page.context
            context.grant_permissions(["clipboard-read", "clipboard-write"])

            # Verify widget Embed Copy button presence
            copy_btn = page.locator("#copyBtn")
            if not copy_btn.is_visible():
                print("Error: #copyBtn is not visible!")
                sys.exit(1)

            btn_text = copy_btn.text_content().strip()
            print(f"Copy button found with text: {btn_text}")
            if btn_text != "Copy":
                print(f"Error: Initial copy button text is not 'Copy': {btn_text}")
                sys.exit(1)

            # Click copy button
            copy_btn.click()
            time.sleep(0.5)

            # Check for text transition
            btn_text_after = copy_btn.text_content().strip()
            print(f"Button text after click: {btn_text_after}")
            if btn_text_after != "Copied!":
                print(f"Error: Copy button did not transition to 'Copied!': {btn_text_after}")
                sys.exit(1)

            # Verify button background color (success green color is rgb(5, 150, 105))
            bg_color = copy_btn.evaluate("el => window.getComputedStyle(el).backgroundColor")
            print(f"Button background color after click: {bg_color}")
            if bg_color != "rgb(5, 150, 105)":
                print(f"Error: Success background color not applied: {bg_color}")
                sys.exit(1)

            # Wait for 2 second timeout to expire and check reset
            print("Waiting for button reset timeout...")
            time.sleep(2.0)
            btn_text_reset = copy_btn.text_content().strip()
            print(f"Button text after reset: {btn_text_reset}")
            if btn_text_reset != "Copy":
                print(f"Error: Copy button text did not reset to 'Copy': {btn_text_reset}")
                sys.exit(1)

            print("All basic clock and widget copy-button checks passed.")

            # Keep it running for manual check if needed
            # page.screenshot(path="screenshot.png")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_test()
