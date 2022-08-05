from pathlib import Path
import csv

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"

api_key = "IUMVK4SLEPVSK1MW"

from xml.dom import UserDataHandler
#import UserDataHandler method from xml.dom
import requests
#import requests module

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
final_response = response.json()
#get data from the url about the currency exchange rate from USD to SGD

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()

with fp_txt.open(mode = "r",encoding="UTF-8", newline="") as file:
    #open the file in read mode to access the data inside
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    with COH.open(mode="r",encoding="UTF-8") as file:
        data = csv.reader(file)
        prev_day = 0
        prev_coh = 0
        counter = 0
        for row in data:
            if counter > 1:
                day = row[0]
                coh = row[1]
                if counter > 1:
                    if int(prev_coh) > int(coh):
                        COH_diff = int(prev_coh) - int(coh)
                        print(f"[CASH DEFICIT] DAY: {day} AMOUNT: SGD{(COH_diff * rate) * -1}")
                    else:
                        print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                        #only need to come out 1 time if all days coh is higher than the on before
                prev_day = day
                prev_coh = coh
            counter += 1