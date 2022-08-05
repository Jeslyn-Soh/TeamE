from pathlib import Path 
#import Path method from pathlib
import csv, re           
#import csv module and regular expression module

home = Path.cwd()                              
#assign home as the class method returns a Path object representing the current working directory or CWD
file_path = home/"project_group"/"csv_reports" 
#use '/'to extend path to extand the file path

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"
#with COH.open(mode="r",encoding="UTF-8")as file :
#    text = file.read()
#    print(text("Day"))
empty_list = []
with COH.open(mode="r",encoding="UTF-8") as file:
    COHreader = csv.DictReader(file)
    for row in COHreader:
        list = ([row["Cash On Hand"]])
        

from xml.dom import UserDataHandler
#import UserDataHandler method from xml.dom
import requests
#import requests module

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'
#API URL of a function to change the CURRENCY from USD to SGD

response = requests.get(url)
#use a get method to request access to the function
#assigned it as an object called 'response' 
final_response = response.json()
#get data from the url about the currency exchange rate from USD to SGD

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
#create a new txt file named "summary_report" by using 'touch' method

class summary2:

 with fp_txt.open(mode = "w",encoding="UTF-8", newline="") as file:
    #open the file in read mode to access the data inside
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    #using the function to exchange the currency,assigned it as rate
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
         #using csv.reader to read the file then by using the function to find the NET PROFIT DEFICIT
                    else:
                        print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                        #only need to come out 1 time if all days coh is higher than the on before
                prev_day = day
                prev_coh = coh
            counter += 1
            
