#https://onlineservices.cdtfa.ca.gov/_/#1


import asyncio
import os
import automation_scripts.config

from pyppeteer import launch

certification_num = "000000000"

async def california_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://onlineservices.cdtfa.ca.gov/_/#1')


    element_id = "l_m-1-4"
    await page.waitForSelector(f'#{element_id}')
    await page.click(f'#{element_id}')

    select_id = "d-3"
    option_value = "SITSUT"
    await page.waitForSelector(f'#{select_id}')
    await page.select(f'#{select_id}', option_value)


    element_id = "d-4"
    
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', certification_num)


    element_id = "d-5"
    await page.waitForSelector(f'#{element_id}')
    await page.click(f'#{element_id}')


    span_id = "caption2_f-2"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)
    
    
    await browser.close()
    return span_content
    


#asyncio.get_event_loop().run_until_complete(california_automate(certification_num))
