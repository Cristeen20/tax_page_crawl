
from automation_scripts.maine import maine_automate #2
from automation_scripts.tennesee import tennesee_automate
from automation_scripts.idaho import idaho_automate
from automation_scripts.georgia import georgia_automate
from automation_scripts.colorado import colorado_automate
from automation_scripts.arkansas import arkansas_automate
from automation_scripts.winsconsin import wisconsin_automate #3
from automation_scripts.north_dakota import north_dakota_automate
from automation_scripts.hawai import hawai_automate #3
from automation_scripts.california import california_automate
from automation_scripts.illinois import illinois_automate
from automation_scripts.missisippi import missisippi_automate
from automation_scripts.texas import texas_automate
from api_scripts.kansas import kansas_api
from api_scripts.louisiana import louisiana_api

import logging
import asyncio
from flask import Flask, jsonify, request

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

app = Flask(__name__)

automate_function_set = {"maine":maine_automate,
                "tennesee":tennesee_automate,
                "idaho":idaho_automate,
                "georgia":georgia_automate,
                "colorado":colorado_automate,
                "arkansas":arkansas_automate,
                "wisconsin":wisconsin_automate,
                "north_dakota":north_dakota_automate,
                "hawai":hawai_automate,
                "california":california_automate,
                "illinois":illinois_automate,
                #"missisippi":missisippi_automate,
                "texas":texas_automate
                }
api_function_set = {
                "kansas":kansas_api,
                "louisiana":louisiana_api
                }

@app.route('/', methods=['POST','GET'])
def load_app():
    return "Trigger /api/get_function for resale certificate verification."

@app.route('/api/get_function', methods=['POST'])
def get_function():
    try:
    
        data = request.json

        state_name = data.get("state_name")
        certification_num = data.get("certification_num")

        try:
            tax_payer = data.get("tax_payer")
            zipcode = data.get("zipcode")
            dba_name = data.get("dba_name")
            account_id = data.get("account_id")
            buyer_acc = data.get("buyer_acc")
            buyer_name = data.get("buyer_name")
        except Exception as e:
            logging.error(str(e))


        try:
            function_name = api_function_set[state_name]
            res = function_name(certification_num,tax_payer,zipcode,dba_name,account_id,buyer_acc,buyer_name)
            return res
        except:
            function_name = automate_function_set[state_name]
            asyncio.set_event_loop(asyncio.SelectorEventLoop())
            res = asyncio.get_event_loop().run_until_complete(function_name(certification_num,tax_payer,zipcode,dba_name,account_id,buyer_acc,buyer_name))

            return res
    except Exception as e:
        return {"error":str(e)}

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8181,debug=True)