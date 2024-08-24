#32083750854
#https://mycpa.cpa.state.tx.us/staxpayersearch/

import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "32083750854"

async def texas_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://mycpa.cpa.state.tx.us/staxpayersearch/')

    element_id = "taxpayerId"
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', certification_num)

    element_id = "btnTaxpayerId"
    await page.waitForSelector(f'#{element_id}')
    await page.click(f'#{element_id}')

    try: 
        span_id = "label label-success"
        await page.waitForSelector(f'#{span_id}')
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
        print(span_content)

    
    await browser.close()
    return span_content
    


#asyncio.get_event_loop().run_until_complete(texas_automate(certification_num))