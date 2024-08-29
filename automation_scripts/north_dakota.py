

#https://apps.nd.gov/tax/tap/_/#1


import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "09999999999"

def output_handle(response):
    if "not" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def north_dakota_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):

    
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://apps.nd.gov/tax/tap/')
    print("launch")
    await asyncio.sleep(2)

    link_class = "Df-1-16"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')
    await page.click(f'#{link_class}')
    

    element_id_type = "ic_Dc-8.FGIC"
    
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'#{element_id_type}')
    
    await asyncio.sleep(1)
    await page.click(f'#{element_id_type}')
    await page.type(f'#{element_id_type}', certification_num)
    

    button_class = "ButtonCaptionWrapper"
    await page.waitForSelector(f'.{button_class}')
    await page.click(f'.{button_class}')
    await asyncio.sleep(1)
    await page.click(f'.{button_class}')
    

    
    span_id = "caption2_Dc-e"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)

    await browser.close()
    res = output_handle(span_content)
    return {
            "result":res
        }
    
    


#asyncio.get_event_loop().run_until_complete(north_dakota_automate(certification_num))
