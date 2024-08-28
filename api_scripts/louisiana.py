import requests
from bs4 import BeautifulSoup

def louisiana_api(seller_acc,seller_name,buyer_acc,buyer_name):
    url = "https://www.revenue.louisiana.gov/SalesTax/ResaleCertificate"
    form_data = {
        'SellerAccountNumber': '999999999',#seller_acc
        'SellerBusinessName': 'ggugugug',#seller_name
        'BuyerAccountNumber': '9999999999',#buyer_acc
        'BuyerBusinessName': 'mjjj'#buyer_name
    }

    response = requests.post(url, data=form_data)
    print("Status Code:", response.status_code)
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element with the class 'validation-summary-errors text-danger'
    

    forms = soup.find_all('form')
    for form in forms:
        if form:
            action = form.get('action')
            if action in "/SalesTax/ResaleCertificate":
                form_text = form.get_text(separator='\n', strip=True)
                form_text_list = form_text.split('\n')
                res = form_text_list[-2]
                return res
        

seller_acc="999999999"
seller_name="hjhjh"
buyer_acc="8888"
buyer_name="uuuu"

res = louisiana_api(seller_acc,seller_name,buyer_acc,buyer_name)
print(res)