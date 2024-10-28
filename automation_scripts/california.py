#https://onlineservices.cdtfa.ca.gov/_/#1


import asyncio
import os
import automation_scripts.config

from pyppeteer import launch

certification_num = "000000000"

def output_handle(response):
    if " valid " in response.lower():
        return "Valid"
    else:
        return "Invalid"

async def california_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=['--no-sandbox'])
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


        element_id = "d-6"
        await page.waitForSelector(f'#{element_id}')
        await page.click(f'#{element_id}')
        await page.click(f'#{element_id}')

        try:
            span_id = "caption2_f-2" 
            await page.waitForSelector(f'#{span_id}')
            await asyncio.sleep(1)
            element = await page.querySelector(f'#{span_id}')
            span_content = await (await element.getProperty('textContent')).jsonValue()
            print(f"{span_content}")
        except Exception as e:
            print(f"The error is {e}")
            return {"Error":e}


        await browser.close()
        if span_content:
            res = output_handle(span_content)
        else: raise ValueError("Error in reading certificate status")

        return {
                "result":res
            }
    except Exception as e:
        return {"error":str(e)}
    


