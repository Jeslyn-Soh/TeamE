from pathlib import Path
import csv, re

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

OH = home/"project_group"/"csv_reports"/"Overheads.csv"
with OH.open(mode="r",encoding="UTF-8") as file:
    text=file.read()
    print(text)

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
print(fp_txt.exists())

empty_list = []

#MEEEE
with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    max1=max(re.findall(pattern="[0-9][0-9].+",string=text))
    cat1=max(re.findall(pattern="[A-Z].+,[0-9][0-9].+",string=text))
    maxt = f"[HIGHEST OVERHEADS] {cat1} SGD:{max1}"
    for ans in text :
        ans=empty_list.append(maxt)
        break
    writer.writerow(empty_list)

#JESLYN
api_key = "IUMVK4SLEPVSK1MW"

import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
final_response = response.json()


with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    rate = (final_response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    max_OH = max(re.findall(pattern = "[0-9].+.[0-9].+", string = text))
    cat = max(re.findall(pattern = "[A-Z].+Expense", string = text))
    ans = f"[HIGHEST OVERHEADS] {cat}: SGD{float(max_OH) * float(rate)}"
    for info in ans:
        empty_list.append(ans)
        break
    writer.writerow(empty_list)