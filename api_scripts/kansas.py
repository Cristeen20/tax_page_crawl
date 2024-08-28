import requests
from bs4 import BeautifulSoup

def kansas_api(sTaxAcctNum):
    url = "https://www.kdor.ks.gov/Apps/Misc/Miscellaneous/CertDefaultCheckRegNum"
    form_data = {
        'sTaxAcctNum': {sTaxAcctNum}
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
        return res
    else:
        print("No error message found.")

sTaxAcctNum = "000-0000000000-00"
kansas_api(sTaxAcctNum)