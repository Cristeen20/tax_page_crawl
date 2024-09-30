
#https://tap.revenue.wi.gov/mta/


import automation_scripts.config
import asyncio
from pyppeteer import launch

certification_num = "99-9090909"
tax_payer = "bussiness"
zipcode = "90909"

def output_handle(response):
    if "invalid" in response.lower():
        return "Invalid"
    else:
        return "Valid"

async def wisconsin_automate(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):

    try:
        browser = await launch(handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                headless=True)
        page = await browser.newPage()
        await page.goto('https://tap.revenue.wi.gov/mta/')
        print("launch")
        await asyncio.sleep(1)

        link_class = "l_Df-1-2"
        await page.waitForSelector(f'#{link_class}')
        await page.click(f'#{link_class}')
        await page.click(f'#{link_class}')
        await asyncio.sleep(5)

    
        #radio button click
        label_class = "FastComboButtonItem.FastComboButtonItem_036.FastComboButton.FRC"
        label_for = "Dw-6_1"
        element_id_type = f'label.{label_class}[for={label_for}]'
        await page.click(element_id_type)
        

        
        
        element_id_type = "Dw-8"
        
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.click(f'#{element_id_type}')
        
        #await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', certification_num)
        
        #ic_Dw-b
        element_id_type = "ic_Dw-b.FGIC"
        
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.click(f'#{element_id_type}')
        
        #await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', tax_payer)

        #ic_Dw-c
        element_id_type = "ic_Dw-c.FGIC"
        
        a = await page.waitForSelector(f'#{element_id_type}')
        await page.click(f'#{element_id_type}')
        
        #await asyncio.sleep(1)
        await page.click(f'#{element_id_type}')
        await page.type(f'#{element_id_type}', zipcode)


        button_class = "action_10"
        await page.waitForSelector(f'#{button_class}')
        await page.click(f'#{button_class}')
        #await asyncio.sleep(1)
        #await page.click(f'#{button_class}')
        

        
        span_id = "FastMessageBoxCaption"
        await page.waitForSelector(f'.{span_id}')
        span_content = await page.evaluate(f'document.querySelector(".{span_id}").innerText')
        print(span_content)

        await browser.close()
        res = output_handle(span_content)
        return {
            "result":res
        }

    except Exception as e:
        return str({"Required values" : "certification_num, tax_payer, zipcode",
                "error": e})
    


#asyncio.get_event_loop().run_until_complete(wisconsin_automate(certification_num,last_name,zipcode))
