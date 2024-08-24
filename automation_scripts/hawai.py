#https://tax.hawaii.gov/
#T-889-999-9999

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "T-889-999-9999"
tax_payer = "bussiness"
dba_name = "hjhjhj"

async def hawai_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://hitax.hawaii.gov/?Link=LicenseSearch')


    #ic_Dh-5
    element_id = "Dh-5"
    a = await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', tax_payer)

    #ic_Dh-6
    element_id = "Dh-6"
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', dba_name)
    
    #ic_Dh-6
    element_id = "Dh-7"
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', certification_num)

    #Dh-8
    element_id = "Dh-8"
    await page.waitForSelector(f'#{element_id}')
    await page.click(f'#{element_id}')

    element_id = "Dh-8"
    await page.waitForSelector(f'#{element_id}')
    await page.click(f'#{element_id}')
    await asyncio.sleep(1)

    
    span_id = "caption2_Dj-f"
    #span_id = "CTE CaptionLabel"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)
    

    await browser.close()
    return span_content
    

#asyncio.get_event_loop().run_until_complete(hawai_automate(certification_num,tax_payer,dba_name))
