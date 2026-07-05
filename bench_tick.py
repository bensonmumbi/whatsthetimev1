import subprocess
import time
import sys
from playwright.sync_api import sync_playwright

def run_benchmark():
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8001"])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8001/whatsthetime.html")

            # Benchmark tick() function
            bench_script = """
            () => {
                const start = performance.now();
                for(let i=0; i<1000; i++) {
                    tick();
                }
                const end = performance.now();
                return (end - start) / 1000;
            }
            """
            # Warm up
            page.evaluate("() => { for(let i=0; i<100; i++) tick(); }")

            avg_time = page.evaluate(bench_script)
            print(f"Average tick() execution time: {avg_time:.6f} ms")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
