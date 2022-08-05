
from pathlib import Path 
#import Path method from pathlib
import csv, re           
#import csv module and regular expression module

home = Path.cwd()                              
#assign home as the class method returns a Path object representing the current working directory or CWD
file_path = home/"project_group"/"csv_reports" 
#use '/'to extend path to extand the file path

PNL = home/"project_group"/"csv_reports"/"Profits and Loss.csv"
#assign PNL as the path for profit and loss.csv

api_key = "IUMVK4SLEPVSK1MW"
#get a api key to use some easier syntax in its place

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

with fp_txt.open(mode = "r",encoding="UTF-8", newline="") as file:
#open the file in read mode to access the data inside
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    #using the function to exchange the currency,assigned it as rate


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
                        np_diff = int(prev_np) - int(np)
                        fnp_diff = f"[NET PROFIT DEFICIT] DAY: {day} AMOUNT: SGD{(np_diff*float(rate) *-1)}"
        #using csv.reader to read the file then by using the function to find the NET PROFIT DEFICIT
                        
                        print(fnp_diff)
                    else:
                        nps = "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
                        print(nps)
                        break
                        #only need to come out one time if all days np is higher than the on before
                prev_day = day
                prev_np = np
            counter += 1 

class summary3:
#assign the function as summary3 for modularisation in main.py

 empty_list = []

 with fp_txt.open(mode="w",encoding="UTF-8",newline="") as file :
      writer=csv.writer(file)
      empty_list.append(nps)
      writer.writerow(empty_list)
 #wrtting 'nps' into summary_report by  using 'w' mode
