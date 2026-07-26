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

            # Start a context that grants clipboard permissions if possible,
            # or just rely on local server testing.
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

            # Test Copy Embed Button UX
            copy_btn = page.locator("#copyBtn")
            initial_btn_text = copy_btn.text_content()
            print(f"Initial Button Text: {initial_btn_text}")
            if initial_btn_text != "Copy":
                print("Error: Initial button text is not 'Copy'!")
                sys.exit(1)

            # Trigger Copy action
            copy_btn.click()
            time.sleep(0.5)

            new_btn_text = copy_btn.text_content()
            print(f"Clicked Button Text: {new_btn_text}")
            if new_btn_text != "Copied!":
                print("Error: Button text did not change to 'Copied!'!")
                sys.exit(1)

            # Wait for reset
            time.sleep(2.0)
            reset_btn_text = copy_btn.text_content()
            print(f"Reset Button Text: {reset_btn_text}")
            if reset_btn_text != "Copy":
                print("Error: Button text did not reset back to 'Copy'!")
                sys.exit(1)

            print("All clock and Copy Button checks passed successfully!")
            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_test()
