import csv
with open("Profits and Loss.csv",'rt')as f:
    data = csv.reader(f)
    prev_day = 0
    prev_profit = 0
    counter = 0
    for row in data:
        if counter >0:
            day = row[0]
            net_profit = row[4]
            if counter > 1:
                if int(prev_profit) > int(net_profit):
                    profit_diff = int(prev_profit) - int(net_profit)
                    print("The Net profit difference between day",prev_day,"and",day,"is $",profit_diff)
            prev_day = day
            prev_profit = net_profit
        counter += 1

empty_list = []
prev_d = "Day"



from pathlib import Path
import csv, re

home = Path.cwd()
PL = home/"project_group"/"csv_reports"/"Profits and Loss.csv"

with open(PL,"rt")as f:

    data = csv.reader(f)
    prev_day = 0
    prev_profit = 0
    counter = 0
    for row in data:
        if counter >0:
            day = row[0]
            net_profit = row[4]
            if counter > 1:
                if int(prev_profit) > int(net_profit):
                    profit_diff = int(prev_profit) - int(net_profit)
                    print("The Net profit difference between day",prev_day,"and",day,"is $",profit_diff)
            prev_day = day
            prev_profit = net_profit
        counter += 1






from pathlib import Path
import csv
import re


home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

COH = home/"project_group"/"csv_reports"/"Profits and Loss.csv"

empty_list = []
with COH.open(mode="r",encoding="UTF-8") as file:
    COHreader = csv.DictReader(file)
    print("Net Profit")
    for row in COHreader:
        coh = row["Net Profit"]
        print(coh)
    
with COH.open(mode="r",encoding="UTF-8") as file:
    data = csv.reader(file)
    prev_day = 0
    prev_profit = 0
    counter = 0
    for row in data:
        if counter >0:
            day = row[0]
            net_profit = row[1]
            if counter > 1:
                if int(prev_profit) > int(net_profit):
                    profit_diff = int(prev_profit) - int(net_profit)
                    print("The Cash On Hand difference between day",prev_day,"and",day,"is $",profit_diff)
            prev_day = day
            prev_profit = net_profit
        counter += 1



