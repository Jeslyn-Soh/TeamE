from pathlib import Path
import csv, re

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

PL = home/"project_group"/"csv_reports"/"Profits and Loss.csv"
with PL.open(mode="r",encoding="UTF-8") as file:
    text = file.readlines()
    print(text[1])

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
print(fp_txt.exists())

empty_list = []

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Day", "Net Profit"])
    for info in empty_list:
        empty_list.append(empty_list)
        break
    writer.writerows(empty_list)

empty_list = []

def diff():
    day=4
    a=20
    b=10    
    sind = str(a-b)
    if sind > 0:
        ans_1 = f"[NET PROFIT SURPLUS] DAY: {day}, AMOUNT: SGD{sind}"
        return empty_list.append(ans_1)
    else:
        ans_2 = f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{sind}"
        return empty_list.append(ans_2)