#https://gtc.dor.ga.gov/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000000000000"

def output_handle(response):
    if "inactive" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def georgia_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):

    url = 'https://gtc.dor.ga.gov/_/'

    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url)
    print("launch")
    await asyncio.sleep(1)

    link_class = "Df-9-24"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')
    await page.click(f'#{link_class}')
    await asyncio.sleep(1)


    #action_3
    element_id_type = "action_3"
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'button#{element_id_type}')
    

    #label_class
    td_id = "Dl-f-0"  #
    a = await page.waitForSelector(f'td#{td_id}')
    await page.click(f'td#{td_id}')
    await asyncio.sleep(1)
    await page.focus(f'td#{td_id}')
    await page.click(f'td#{td_id}')

    await page.keyboard.type(certification_num)

    #action_3
    element_id_type = "action_3"
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'button#{element_id_type}')
    

    span_id = "Dl-w-1"
    await page.waitForSelector(f'td#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)

    await browser.close()
    res = output_handle(span_content)
    return {
            "result":res
        }


#asyncio.get_event_loop().run_until_complete(georgia_automate(certification_num))