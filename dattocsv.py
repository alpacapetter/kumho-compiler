import subprocess
import re
from os import listdir

# remember to use "/" instead of "\" and remember to put an extra "/" at the end
file_location = "C:/Users/Robert Choi/Desktop/Kumho ENG/Data/4-7-2018 DATA LOG/BM1 DROP DOOR PT-101 DATA/"

# extracting a list of target file names
dirlist = listdir(file_location)
target_file = []
for line in dirlist:
    #regular expression to find a format "0000 00 00 0014 (Float)"
    regex = re.findall(r"[0-9]{4} [0-9]{2} [0-9]{2} [0-9]{2}[1][4] \(Float\)", line)
    if len(regex) == 1:
        target_file.append(regex[0])

# converting dat to csv
for file in target_file:
    file_name = file
    print(file)
    # using subprocess to run the conversion via command line switch
    viewer_location = file_location + "FTViewFileViewer.exe"
    dat_location = file_location + file_name + ".dat"
    csv_location = file_location + file_name + ".csv"
    subprocess.run([viewer_location,"/sd", dat_location, csv_location], shell=True)