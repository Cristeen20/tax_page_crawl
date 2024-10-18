import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "00000000000000"

def output_handle(response):
    if "not found" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def arkansas_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        url = 'https://atap.arkansas.gov/_/'    

        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True,
                                args=[
                                    '--no-sandbox',
                                    '--disable-setuid-sandbox',
                                    '--disable-dev-shm-usage'
                                ])
        page = await browser.newPage()
        await page.goto(url)
        print("launch")
        await asyncio.sleep(1)

        link_class = "Df-1-14"
        await page.waitForSelector(f'#{link_class}')
        await page.click(f'#{link_class}')
        await page.click(f'#{link_class}')
        

        element_id_type = "Dd-3"
        text = "SITE"
        a = await page.waitForSelector(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.select(f'#{element_id_type}', text)


        #Dc-7
        element_id_type = "Dd-5"
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', certification_num)
        await page.click(f'#{element_id_type}')


        button_class = "Dd-6"
        await page.waitForSelector(f'#{button_class}')
        await page.click(f'#{button_class}')
        await asyncio.sleep(1)
        await page.click(f'#{button_class}')

        element = await page.querySelector(f'#{button_class}')

        
        span_id = "caption2_Dd-8"
        await page.waitForSelector(f'#{span_id}')
        element = await page.querySelector(f'#{span_id}')
        span_content = await page.evaluate('(element) => element.innerText', element)
        print(span_content)

        await browser.close()
        res = output_handle(span_content)
        return {
                "result":res
            }
    except Exception as e:
        return {"error":str(e)}
    


#asyncio.get_event_loop().run_until_complete(arkansas_automate(certification_num))