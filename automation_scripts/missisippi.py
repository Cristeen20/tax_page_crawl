




import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000001"

async def missisippi_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):

    
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://tap.dor.ms.gov/_/')
    print("launch")

    button_class = "l_Df-1-13"
    await page.waitForSelector(f'#{button_class}')
    await page.click(f'#{button_class}')
    await page.click(f'#{button_class}')
    print("click")
    

    element_id_type = "Dd-4"
    text = "  Seller's Use Permit"
    await page.waitForSelector(f'#{element_id_type}')
    await page.type(f'#{element_id_type}', text)
    await page.keyboard.press('Enter')
    

    button_class = "Dd-5"
    await page.waitForSelector(f'#{button_class}')
    await page.click(f'#{button_class}')
    

    element_id = "Dd-5"
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', certification_num)

    button_id = "Dd-8"
    await page.waitForSelector(f'#{button_id}')
    await page.click(f'#{button_id}')
    
    span_id = "IconCaptionText"
    await page.waitForSelector(f'.{span_id}')
    span_content = await page.evaluate(f'document.querySelector(".{span_id}").innerText')
    print(span_content)
    await page.screenshot({'path': 'example.png'})

    
    
    await browser.close()
    


#asyncio.get_event_loop().run_until_complete(missisippi_automate(certification_num))
