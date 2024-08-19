
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

import asyncio
from flask import Flask, jsonify, request

app = Flask(__name__)

function_set = {"maine":maine_automate,
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
                "missisippi":missisippi_automate,
                "texas":texas_automate
                }

@app.route('/api/get_function', methods=['POST'])
def get_function():

    data = request.json
    state_name = data.get("state_name")
    certification_num = data.get("certification_num")
    tax_payer = data.get("tax_payer")
    zipcode = data.get("zipcode")
    dba_name = data.get("dba_name")
    account_id = data.get("account_id")

    function_name = function_set[state_name]
    asyncio.get_event_loop().run_until_complete(function_name(certification_num,tax_payer,zipcode,dba_name,account_id))


# Run the app
if __name__ == '__main__':
    app.run(debug=True)