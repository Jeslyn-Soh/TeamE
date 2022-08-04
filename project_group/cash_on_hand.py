from pathlib import Path
import csv
import re


home = Path.cwd()
file_path=home/"project_group"/"csv_reports"

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"
with COH.open(mode="r",encoding="UTF-8")as file :
    text = file.read()
print(text)



