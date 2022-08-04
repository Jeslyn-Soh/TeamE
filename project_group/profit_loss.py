import csv
with open("pnl.csv",'rt')as f:
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
import csv, re

import csv

with open("pnl.csv",'rt')as f:
    #home = Path.cwd()
    #file_path=home/"project_group"/"pnl.csv"
    #PL = home/"project_group"/"pnl.csv"
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

with PL.open(mode="r",encoding="UTF-8") as file:
    PLreader = csv.DictReader(file)
    print("Day, Net Profit")
    for row in PLreader:
        print(row["Day"],row["Net Profit"])
    #day = int(row["Day"])
    #while day < 50:
        #day += 1
        #print(day)

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
print(fp_txt.exists())

def diff():
    day = 4
    a = 20
    b = 30   
    sind = a-b
    if sind > 0:
        return f"[NET PROFIT SURPLUS] DAY: {day}, AMOUNT: SGD{sind}"
    else:
        return f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{-1 * sind}"
print(diff())

