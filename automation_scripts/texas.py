#32083750854
#https://mycpa.cpa.state.tx.us/staxpayersearch/

import automation_scripts.config
import asyncio
from pyppeteer import launch
import re

certification_num = "32083750854"

def output_handle(response):
    if "active" in response.lower():
        return "Valid"
    else:
        return "Invalid"

async def texas_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('https://mycpa.cpa.state.tx.us/staxpayersearch/')

        element_id = "taxpayerId"
        await page.waitForSelector(f'#{element_id}')
        certification_num = re.sub(r'\D', '', certification_num)
        await page.type(f'#{element_id}', certification_num)
        await page.keyboard.press('Enter')

        try:
            #check type errors
            error_id = "taxpayerIdError"
            await page.waitForSelector(f'#{error_id}',timeout=3000)
            error_content = await page.evaluate(f'document.querySelector("#{error_id}").innerText')
            if error_content:
                await browser.close()
                return {"error":str(error_content)}
        except:
            pass
        

        #element_id = "btnTaxpayerId"
        #await page.waitForSelector(f'#{element_id}')
        #await page.click(f'#{element_id}')

        try: 
            span_id = "label label-success"
            await page.waitForSelector(f'#{span_id}',timeout=6000)
            span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
            print(span_content)
        except:
            span_class = "panel-body"
            await page.waitForSelector(f'.{span_class}')
            span_content = await page.evaluate(f'''
            () => {{
                const div = document.querySelector('.{span_class}');
                const span = div.querySelector('span');
                return span ? span.innerText : null;
            }}''')
            print(span_content) #no response
        

        
        await browser.close()
        if span_content:
            res = output_handle(span_content)
        else: raise ValueError("Error in reading certificate status")
        return {
                "result":res
            }
    except Exception as e:
        return {"error":str(e)}
    


#asyncio.get_event_loop().run_until_complete(texas_automate(certification_num))