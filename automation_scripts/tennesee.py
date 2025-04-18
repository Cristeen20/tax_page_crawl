#https://tntap.tn.gov/eservices/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch
import re

certification_num = "000000000"

def output_handle(response):
    if "no" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def tennesee_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        url = 'https://tntap.tn.gov/eservices/_/'

        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto(url)
        print("launch")
        await asyncio.sleep(1)

        link_class = "Df-1-5"
        await page.waitForSelector(f'#{link_class}')
        await page.click(f'#{link_class}')
        await asyncio.sleep(1)

        #c_Dp-1-6
        link_class = "c_Dp-1-6"
        await page.waitForSelector(f'#{link_class}')
        await page.click(f'#{link_class}')
        await asyncio.sleep(2)

        element_id_type = "Dd-4"
        val = "SLCCERT"
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.select(f'#{element_id_type}',val)
        
        #ic_Dd-5
        element_id_type = "ic_Dd-5"
        
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        certification_num = re.sub(r'\D', '', certification_num)
        await page.type(f'#{element_id_type}', certification_num)

        #action_3
        element_id_type = "Dd-6"
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.click(f'button#{element_id_type}')
        
        
        span_id =  "FGLR.FGFR.Visible.FGPadRow"
        await page.waitForSelector(f'.{span_id}')
        span_content = await page.evaluate(f'document.querySelector(".{span_id}").innerText')
        print(f"response : {span_content}")
            

        await browser.close()
        if span_content:
            res = output_handle(span_content)
        else: raise ValueError("Error in reading certificate status")
        return {
                "result":res
            }
    except Exception as e:
        return {"error":str(e)}
    


#asyncio.get_event_loop().run_until_complete(tennesee_automate(certification_num))
