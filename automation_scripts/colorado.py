# https://www.colorado.gov/revenueonline/_/

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000000000"

async def colorado_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):
    
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://www.colorado.gov/revenueonline/_/')
    print("launch")
    await asyncio.sleep(1)

    link_class = "Dg-1-12"
    await page.waitForSelector(f'#{link_class}')
    await page.click(f'#{link_class}')
    await asyncio.sleep(1)

    #radio button click
    label_class = "FastComboButtonItem.FastComboButtonItem_Yes.FastComboButton.FRC"
    label_for = "Dc-7_1"
    element_id_type = f'label.{label_class}[for={label_for}]'
    await page.click(element_id_type)


    #ic_Dc-c
    element_id_type = "ic_Dc-c"
    a = await page.waitForSelector(f'#{element_id_type}')
    await page.click(f'#{element_id_type}')

    await page.type(f'#{element_id_type}', certification_num)
    await page.keyboard.press('Enter')
    
    span_id = "Dc-n-1"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)

    await browser.close()
    return span_content


#asyncio.get_event_loop().run_until_complete(colorado_automate(certification_num))

