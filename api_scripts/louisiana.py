import requests
from bs4 import BeautifulSoup

def output_handle(response):
    if "not a valid" in response.lower():
        return "Invalid"
    else:
        return "Valid"

def louisiana_api(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    try:
        url = "https://www.revenue.louisiana.gov/SalesTax/ResaleCertificate"
        form_data = {
            'SellerAccountNumber': certification_num,#seller_acc
            'SellerBusinessName': tax_payer,#seller_name
            'BuyerAccountNumber': buyer_acc,#buyer_acc
            'BuyerBusinessName': buyer_name #buyer_name
        }

        response = requests.post(url, data=form_data)
        print("Status Code:", response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        forms = soup.find_all('form')
        print(forms)
        for form in forms:
            if form:
                
                action = form.get('action')
                if action in "/SalesTax/ResaleCertificate":
                    form_text = form.get_text(separator='\n', strip=True)
                    form_text_list = form_text.split('\n')
                    res = form_text_list[-2]
                    
                    res = output_handle(res)
                    return {
                            "result":res
                        }
        
        return {
            "status_code":response.status_code
        }
    except Exception as e:
        return {
            "error":str(e)
        }

seller_acc="999999999"
seller_name="hjhjh"
buyer_acc="8888"
buyer_name="uuuu"

#res = louisiana_api(seller_acc,seller_name,buyer_acc,buyer_name)
#print(res)