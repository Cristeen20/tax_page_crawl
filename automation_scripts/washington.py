#https://secure.dor.wa.gov/gteunauth/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch


async def main():

    
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://secure.dor.wa.gov/gteunauth/_/')
    print("launch")
    await asyncio.sleep(2)

    link_class = "Dd-1-2"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')
    await page.click(f'#{link_class}')
    

    #file upload
    await browser.close()
    


#asyncio.get_event_loop().run_until_complete(main())
