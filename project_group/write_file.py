from pathlib import Path 

home = Path.home()
file_path = home/"TeamE"/"project_group"/"deficit_report.txt"

with file_path.open (mode="w") as file :
    file.write("halo")
    
