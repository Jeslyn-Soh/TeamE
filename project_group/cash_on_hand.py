from pathlib import Path
import csv

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"
  
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
                    print(f"[CASH DEFICIT] DAY: {day} AMOUNT: SGD{COH_diff}")
                else:
                    print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
                    #only need to come out if all days coh is higher than the on before
            prev_day = day
            prev_coh = coh
        counter += 1