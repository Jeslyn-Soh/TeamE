from pathlib import Path 
#import Path method from pathlib
import csv, re           
#import csv module and regular expression module

home = Path.cwd()                              
#assign home as the class method returns a Path object representing the current working directory or CWD
file_path = home/"project_group"/"csv_reports" 
#use '/'to extend path to extand the file path

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"
#assign COH as a path for Cash On Hand
with COH.open(mode="r",encoding="UTF-8") as file:
#"file" is a variable assigned to COH after opening it  
    COHreader = csv.DictReader(file)
    print("Cash On Hand")
    for row in COHreader:
        coh = row["Cash On Hand"]
        print(coh)
    #open the file in read mode to ectract the dat of Cash On Hand
    
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
                    print(f"[CASH DEFICIT] DAY: {day} AMOUNT:SGD{profit_diff}")
            prev_day = day
            prev_coh = coh
        counter += 1







