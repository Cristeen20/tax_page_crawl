


import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000001"

def output_handle(response):
    if "not" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def illinois_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None):

    #https://www.ascdi.com/verifyresalecertificate/
    
    browser = await launch(handleSIGINT=False,
                            handleSIGTERM=False,
                            handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto('https://www.revenue.state.il.us/app/bgii/servlet/BGIInquiry')
    print("launch")

    button_class = "Dd-5"
    await page.waitForSelector(f'#{button_class}')
    await page.click(f'#{button_class}')
    print("click")

    element_id_type = "Dd-5"
    text = " License Number"
    await page.waitForSelector(f'#{element_id_type}')
    await page.type(f'#{element_id_type}', text)
    await page.keyboard.press('Enter')


    button_class = "Dd-7"
    await page.waitForSelector(f'#{button_class}')
    await page.click(f'#{button_class}')

    element_id = "Dd-7"
    await page.waitForSelector(f'#{element_id}')
    await page.type(f'#{element_id}', certification_num)

    button_id = "Dd-a"
    await page.waitForSelector(f'#{button_id}')
    await page.click(f'#{button_id}')
    
    #caption2_Dd-j
    span_id = "caption2_Dd-j"
    await page.waitForSelector(f'#{span_id}')
    span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
    print(span_content)


    await browser.close()
    res = output_handle(span_content)
    return {
            "result":res
        }
    


#asyncio.get_event_loop().run_until_complete(illinois_automate(certification_num))
