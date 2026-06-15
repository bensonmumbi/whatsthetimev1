import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        file_path = os.path.abspath('whatsthetime.html')
        await page.goto(f'file://{file_path}')

        # Focus a navigation button
        await page.keyboard.press('Tab')
        await page.keyboard.press('Tab')
        await page.screenshot(path='/home/jules/verification/screenshots/nav_focus.png')

        await browser.close()

asyncio.run(main())
