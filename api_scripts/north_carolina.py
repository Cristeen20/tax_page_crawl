#https://eservices.dor.nc.gov/salesdatabase/SAUQueryServlet


import requests
from bs4 import BeautifulSoup

def north_carolina_api(acc_no,taxpayer_name,result_no):
    url = "https://eservices.dor.nc.gov/salesdatabase/SAUQueryServlet"
    form_data = {
        'AccountNo': acc_no,
        'TaxpayerName': taxpayer_name,
        'ResultNo': result_no,
        'Submit': "Submit"
    }

    response = requests.post(url, data=form_data)
    print("Status Code:", response.status_code)
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Find the element with the class 'validation-summary-errors text-danger'
    

   # database system faliure
        

acc_no="999999999"
taxpayer_name="hjhjh"
result_no="100"
submit="uuuu"



res = north_carolina_api(acc_no,taxpayer_name,result_no)
print(res)