from pathlib import Path
import csv

home = Path.cwd()
file_path=home/"project_group"/"csv_reports"
print(file_path.exists())

for file in file_path.glob("*.csv"):
    print(file)

COH = home/"project_group"/"csv_reports"/"Cash On Hand.csv"
with COH.open(mode="r",encoding="UTF-8") as file:
    text=file.read()

print(text)


from pathlib import Path
home=Path.home()

file_path1=home/"TeamE"/"project_group"
file_path2=home/"TeamE"/"project_group"/"csv_reports"
file_path3= home/"project_group"/"csv_reports"
file_path4=home/"TeamE"/"project_group"/"csv_reports"/"Cash On Hand"
print(file_path1.exists())
print(file_path2.exists())
print(file_path3.exists())
print(file_path4.exists())