#https://verify-taxcerts.floridarevenue.com/

import asyncio
import os
import config

from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://verify-taxcerts.floridarevenue.com/')
    await asyncio.sleep(8)

    label_class = "OFFM.SellerVerView.TaxTypeDDKey"
    await page.waitForSelector(f'input#{label_class}')
    await page.click(f'input#{label_class}')
    await asyncio.sleep(5)

    # NOT WORKING

    
    await browser.close()
    


#asyncio.get_event_loop().run_until_complete(main())
