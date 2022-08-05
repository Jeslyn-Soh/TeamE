from pathlib import Path 
#import Path method from pathlib
import csv, re           
#import csv module and regular expression module

home = Path.cwd()                              
#assign home as the class method returns a Path object representing the current working directory or CWD
file_path = home/"project_group"/"csv_reports" 
#use '/'to extend path to extand the file path

OH = home/"project_group"/"csv_reports"/"Overheads.csv" 
#assign OH as a path for Overheads.csv
with OH.open(mode="r",encoding="UTF-8") as file:
#"file" is a variable assigned to OH after opening it  
    text=file.read()
    #assign ".read()" object to text to read OH file

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
#create a new txt file named"summary_report.txt"

empty_list = []
api_key = "IUMVK4SLEPVSK1MW"

import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
final_response = response.json() 
#get the data of real time currency exchange rate

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
#open the file in write mode to find the exchange rate in the data

class summary3:

 with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    #open the file in write mode to place the data of the highest expense in it
    max_OH = max(re.findall(pattern = "[0-9].+.[0-9].+", string = text))
    cat = max(re.findall(pattern = "[A-Z].+ Expense", string = text))
    #use regular expression to find the values and expense
    ans = f"[HIGHEST OVERHEADS] {cat}: SGD{float(max_OH) * float(rate)}"
    #enter output using f-string and convert the USD value to SGD using the data found earlier
    for info in ans:
        empty_list.append(ans)
        break
    writer.writerow(empty_list)
    #append the empty list to insert the answer while will be reflected in the summary_report and break to stop the loop
