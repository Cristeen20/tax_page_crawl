#https://tax.hawaii.gov/
#T-889-999-9999

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "T-889-999-9999"
tax_payer = "bussiness"
dba_name = "hjhjhj"


def output_handle(response):
    if "no" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def hawai_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('https://hitax.hawaii.gov/?Link=LicenseSearch')


        #ic_Dh-5
        element_id = "Dg-4" 
        a = await page.waitForSelector(f'#{element_id}')
        await page.type(f'#{element_id}', tax_payer)

        #ic_Dh-6
        element_id = "Dg-5"
        await page.waitForSelector(f'#{element_id}')
        await page.type(f'#{element_id}', dba_name)
        
        #ic_Dh-6
        element_id = "Dg-6"
        await page.waitForSelector(f'#{element_id}')
        await page.type(f'#{element_id}', certification_num)

        #Dh-8
        element_id = "Dg-7"
        await page.waitForSelector(f'#{element_id}')
        await page.click(f'#{element_id}')

        element_id = "Dg-7"
        await page.waitForSelector(f'#{element_id}')
        await page.click(f'#{element_id}')
        await asyncio.sleep(1)

        try:
            span_id = "caption2_Dh-f"
            #span_id = "CTE CaptionLabel"
            await page.waitForSelector(f'#{span_id}')
            span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
            print(span_content)
        except Exception as e:
            #True cases unhandled
            return {
                "Error":str(e)
            }
        
        await browser.close()

        if span_content:
            res = output_handle(span_content)
        else: raise ValueError("Error in reading certificate status")

        return {
            "result":res
        }
    
    except Exception as e:
        return {"Required values" : "certification_num, tax_payer, dba_name",
                "error": str(e)}

    #asyncio.get_event_loop().run_until_complete(hawai_automate(certification_num,tax_payer,dba_name))
