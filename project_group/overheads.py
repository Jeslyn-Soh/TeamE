from pathlib import Path
import csv
import re

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"
print(file_path.exists())


OH = home/"project_group"/"csv_reports"/"Overheads.csv"
with OH.open(mode="r",encoding="UTF-8") as file:
    text=file.read()
print(text)


fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
print(fp_txt.exists())
empty_list=[]

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    empty_list=[]
    max1=max(re.findall(pattern="[0-9][0-9].+",string=text))
    cat1=max(re.findall(pattern="[A-Z].+,[0-9][0-9].+",string=text))
    maxt = f"[HIGHEST OVERHEADS] {cat1} SGD:{max1}"
    for ans in text :
        ans=empty_list.append(maxt)
        break
    writer.writerow(empty_list)


