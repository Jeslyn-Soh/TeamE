api_key = "IUMVK4SLEPVSK1MW"

from xml.dom import UserDataHandler
import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
final_response = response.json()
print(final_response)

from pathlib import Path
import  re

home = Path.cwd()
file_path = home/"project_group"/"csv_reports"

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()

#function = "FX_WEEKLY"
#from_currency = "USD"
#to_currency = "SGD"

with fp_txt.open(mode = "w") as file:
    #USD = re.findall(pattern = ["1. From_Currency Code.+"], string = final_response)
    #SGD = re.findall(pattern = ["3. To_Currency Code.+"], string = final_response)
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    ans_rate = f"[REAL TIME CURRENCY CONVERSION RATE]  = SGD{rate}"
    for info in url:
        file.write(ans_rate)
        break

