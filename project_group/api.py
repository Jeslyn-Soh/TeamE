api_key = "IUMVK4SLEPVSK1MW"

from xml.dom import UserDataHandler
#import UserDataHandler method from xml.dom
import requests
#import requests module

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
final_response = response.json()
#get data from the url about the currency exchange rate from USD to SGD

from pathlib import Path
#import Path method from pathlib

home = Path.cwd()
#assign home as the class method returns a Path object representing the current working directory or CWD
file_path = home/"project_group"/"csv_reports"
#use '/'to extend path to extand the file path

fp_txt = home/"project_group"/"summary_report.txt"


with fp_txt.open(mode = "w") as file:
    #open the file in write mode to place the data of the exchange rate inside
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    #'rate' is a variable assigned to find the exchange rate from a list in another list
    ans_rate = f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{rate}"
    #'ans_rate' is a variable assigned to enter the output
    for info in url:
        file.write(ans_rate)
        break
    #to write the 'ans_rate' output in the text file and break to stop the loop