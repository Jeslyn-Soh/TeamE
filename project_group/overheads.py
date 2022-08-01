from pathlib import Path
import csv

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"
print(file_path.exists())

for file in file_path.glob("*.csv"):
    print(file)

OH = home/"project_group"/"csv_reports"/"Overheads.csv"
with OH.open(mode="r",encoding="UTF-8") as file:
    text=file.read()

fp_txt = home/"project_group"/"summary_report.txt"
fp_txt.touch()
print(fp_txt.exists())

with fp_txt.open(mode = "w", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)
    def highest_OH(Category, Overheads):
        return f"[HIGHEST OVERHEADS {max(Category)}: SGD{max(Overheads)}]"
print(highest_OH)

def highest_OH(Category, Overheads):
    return f"[HIGHEST OVERHEADS {Category}: SGD{Overheads}]"
print(max(text))