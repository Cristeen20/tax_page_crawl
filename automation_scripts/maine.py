# https://revenue.maine.gov/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch


certification_num = "0000000"
account_id = "9999-9999"


async def maine_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):
    try:
        url = 'https://revenue.maine.gov/_/'

        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False)
        page = await browser.newPage()
        await page.goto(url)
        print("launch")
        await asyncio.sleep(2)

        link_class = "Df-1-5"
        await page.waitForSelector(f'#{link_class}')
        await page.click(f'#{link_class}')
        await asyncio.sleep(1)

        #Dd-6
        element_id_type = "Dd-6"
        val = "RESALE"
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.select(f'#{element_id_type}',val)
        
        #ic_Dd-7
        element_id_type = "ic_Dd-7"
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', certification_num)

        #ic_Dd-8
        element_id_type = "ic_Dd-8"
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', account_id)

        #Dc-8
        element_id_type = "Dc-8"
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.focus(f'#{element_id_type}')
        await page.click(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        

        span_id = "FastMessageBoxCaption"
        await page.waitForSelector(f'.{span_id}')
        span_content = await page.evaluate(f'document.querySelector(".{span_id}").innerText')
        print(span_content)

        await browser.close()
        return span_content
    
    except Exception as e:
        return str({"Required values" : "certification_num, account_id",
                "Error": e})


#asyncio.get_event_loop().run_until_complete(maine_automate(certification_num,account_id))
