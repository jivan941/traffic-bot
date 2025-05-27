import asyncio
from pyppeteer import launch
import random

URL = "https://jkmovies24wach.blogspot.com/2025/05/movies.html?m=1"
CLICK_SELECTOR = 'a[href*="target"]'  # Optional: change this to actual selector
VISITS = 2000

async def visit():
    browser = await launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/111.0.0.0 Mobile Safari/537.36")

    for i in range(VISITS):
        print(f"[{i+1}] Visiting site...")
        await page.goto(URL, {'waitUntil': 'domcontentloaded'})
        await page.waitForTimeout(random.randint(2000, 5000))
        try:
            await page.click(CLICK_SELECTOR)
            print(">> Link clicked")
        except:
            print(">> Link not found")
        await asyncio.sleep(random.randint(2, 5))


    await browser.close()

asyncio.get_event_loop().run_until_complete(visit())
      
