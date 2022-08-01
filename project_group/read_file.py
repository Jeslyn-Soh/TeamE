from pathlib import Path
import csv

home=Path.home()
file_path=home/"TeamE"/"project_group"/"csv_reports"
print(file_path.exists())

for file in file_path.glob("*.csv"):
    print(file)

with file_path.open(mode="r",encoding="UTF-8") as file:
    text=file.read("Cash On Hand")

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