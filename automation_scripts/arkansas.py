import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000000000000"

async def arkansas_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):

    url = 'https://atap.arkansas.gov/_/'    

    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url)
    print("launch")
    await asyncio.sleep(1)

    link_class = "Df-1-14"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')
    await page.click(f'#{link_class}')
    

    element_id_type = "Dc-5"
    text = "SITE"
    a = await page.waitForSelector(f'#{element_id_type}')
    await asyncio.sleep(1)
    await page.click(f'#{element_id_type}')
    await page.select(f'#{element_id_type}', text)

    #Dc-7
    element_id_type = "Dc-7"
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'#{element_id_type}')
    
    await page.type(f'#{element_id_type}', certification_num)
    

    button_class = "ButtonCaptionWrapper"
    await page.waitForSelector(f'.{button_class}')
    await page.click(f'.{button_class}')

    
    span_id = "caption2_Dc-c"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)

    await browser.close()
    return span_content


#asyncio.get_event_loop().run_until_complete(arkansas_automate(certification_num))