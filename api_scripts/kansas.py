import requests
from bs4 import BeautifulSoup


def output_handle(response):
    if "invalid" in response.lower():
        return "Invalid"
    else:
        return "Valid"

def kansas_api(certification_num,tax_payer=None,zipcode=None,dba_name=None,account_id=None,buyer_acc=None,buyer_name=None):
    url = "https://www.kdor.ks.gov/Apps/Misc/Miscellaneous/CertDefaultCheckRegNum"
    form_data = {
        'sTaxAcctNum': {certification_num}
    }

    response = requests.post(url, data=form_data)
    print("Status Code:", response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the element with the class 'validation-summary-errors text-danger'
    error_message = soup.find(class_='validation-summary-errors text-danger')

    # Extract and print the text content, if the element is found
    if error_message:
        print("Error Message:", error_message.get_text(strip=True))
        res = error_message.get_text(strip=True)

        res = output_handle(res)
        return {
                "result":res
            }
    else:
        print("No error message found.")

#sTaxAcctNum = "000-0000000000-00"
#res = kansas_api(sTaxAcctNum)
#print(res)