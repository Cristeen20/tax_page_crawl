# https://idahotap.gentax.com/TAP/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "000000000"

def output_handle(response):
    if "verify" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def idaho_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):

    url = 'https://idahotap.gentax.com/TAP/_/'
    
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url)
    print("launch")
    await asyncio.sleep(1)

    link_class = "Dg-1-11"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')

    #Dl-8
    element_id_type = "Dl-8"
    val = "08"
    a = await page.waitForSelector(f'#{element_id_type}')
    await asyncio.sleep(1)
    await page.click(f'#{element_id_type}')
    await page.select(f'#{element_id_type}',val)
    
    #ic_Dl-9
    element_id_type = "ic_Dl-9"
    a = await page.waitForSelector(f'#{element_id_type}')
    await asyncio.sleep(1)
    await page.click(f'#{element_id_type}')
    await page.type(f'#{element_id_type}', certification_num)

    #action_3
    element_id_type = "action_8"
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'button#{element_id_type}')


    span_id = "caption2_Dl-e"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)

    await browser.close()
    res = output_handle(span_content)
    return {
            "result":res
        }
    


#asyncio.get_event_loop().run_until_complete(idaho_automate(certification_num))
