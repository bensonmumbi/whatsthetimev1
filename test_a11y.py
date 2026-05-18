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

            # Try to tab to the nav links
            page.keyboard.press("Tab") # Should focus logo
            focused_handle = page.evaluate_handle("document.activeElement")
            logo_class = page.evaluate("el => el.className", focused_handle)
            print(f"Focused after 1 Tab: {logo_class}")

            page.keyboard.press("Tab") # Should focus 'Time' link if accessible
            focused_handle = page.evaluate_handle("document.activeElement")
            nav_id = page.evaluate("el => el.id", focused_handle)
            print(f"Focused after 2 Tabs: {nav_id}")

            if nav_id != "nav-time":
                print("FAIL: 'Time' nav link is not focusable via Tab")
            else:
                print("SUCCESS: 'Time' nav link is focusable")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_test()
