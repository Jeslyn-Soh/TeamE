from pathlib import Path

#file_path= Path.home()/"project_group"/"csv_reports"

#with file_path.open(mode="r",encoding="UTF-8") as file:
    #text=file.read()
#print(text)

home =Path.home()
print(home)

file_path = home/"P4B"
print(file_path.exists())