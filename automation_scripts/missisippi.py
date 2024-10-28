




import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000001"

def output_handle(response):
    if "invalid" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def missisippi_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
    
        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=['--no-sandbox'])
        page = await browser.newPage()
        await page.goto('https://tap.dor.ms.gov/_/')
        print("launch")
        await asyncio.sleep(2)

        button_class = "l_Df-1-13"
        await page.waitForSelector(f'#{button_class}')
        await page.click(f'#{button_class}')
        await page.click(f'#{button_class}')
        print("click")
        

        element_id_type = "Dd-4"
        text = "Sales "
        await page.waitForSelector(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', text)
        
        await page.keyboard.press('Enter')
        await asyncio.sleep(2)
        

        button_class = "Dd-5"
        await page.waitForSelector(f'#{button_class}')
        await page.click(f'#{button_class}')
        

        element_id = "Dd-5"
        await page.waitForSelector(f'#{element_id}')
        await page.type(f'#{element_id}', certification_num)

        button_id = "Dd-8"
        await page.waitForSelector(f'#{button_id}')
        await page.click(f'#{button_id}')
        await page.click(f'#{button_id}')
        
        span_id = "caption2_Dd-7" #"IconCaptionText"
        await page.waitForSelector(f'#{span_id}')
        span_content = await page.evaluate(f'document.querySelector("#{span_id}").innerText')
        print(span_content)
        await asyncio.sleep(20)
        #await page.screenshot({'path': 'example.png'})

        await browser.close()
        if span_content:
            res = output_handle(span_content)
        else: raise ValueError("Error in reading certificate status")
        return {
                "result":res
            }
    except Exception as e:
        return {"error":str(e)}
    


#asyncio.get_event_loop().run_until_complete(missisippi_automate(certification_num))
