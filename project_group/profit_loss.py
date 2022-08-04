from pathlib import Path
import csv, re

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

PL = home/"project_group"/"csv_reports"/"Profits and Loss.csv"

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

