from pathlib import Path
import csv

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

PNL = home/"project_group"/"csv_reports"/"Profits and Loss.csv"

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
    with PNL.open(mode="r",encoding="UTF-8") as file:
        data = csv.reader(file)
        prev_day = 0
        prev_np = 0
        counter = 0
        for row in data:
            if counter > 0:
                day = row[0]
                np = row[4]
                if counter > 1:
                    if int(prev_np) > int(np):
                        np_diff = int(np) - int(np)
                        print(f"[NET PROFIT DEFICIT] DAY: {day} AMOUNT: SGD{(np_diff * rate) * -1}")
                    else:
                        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                        #only need to come out one time if all days np is higher than the on before
                prev_day = day
                prev_np = np
            counter += 1