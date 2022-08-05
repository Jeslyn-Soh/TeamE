from pathlib import Path
import csv
import re


home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"

empty_list = []
with COH.open(mode="r",encoding="UTF-8") as file:
    COHreader = csv.DictReader(file)
    print("Cash On Hand")
    for row in COHreader:
        coh = row["Cash On Hand"]
        print(coh)
    
with COH.open(mode="r",encoding="UTF-8") as file:
    data = csv.reader(file)
    prev_day = 0
    prev_coh = 0
    counter = 0
    for row in data:
        if counter >0:
            day = row[0]
            coh = row[1]
            if counter > 1:
                if int(prev_coh) > int(coh):
                    profit_diff = int(prev_coh) - int(coh)
                    print(f"[Cash Deficit] Day: {day} Amount:SGD{profit_diff}")
            prev_day = day
            prev_coh = coh
        counter += 1






