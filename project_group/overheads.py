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

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    max_OH = max(re.findall(pattern = ("[0-9].+.[0-9].+"), string = text))
    ans = f"[HIGHEST OVERHEADS {max_OH}: SGD{max_OH}]"
    for info in max_OH:
        empty_list.append(ans)
        break
    writer.writerow(empty_list)
