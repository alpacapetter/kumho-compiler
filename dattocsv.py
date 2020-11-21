import subprocess
import re
import os
import sys
import time
import concurrent.futures

# time counter to measure program performance
start_time = time.time()

# set file location
## remember to use "/" instead of "\" and remember to put an extra "/" at the end
file_location = "C:/Users/Rob/Documents/Datalog 2018-9-10/BM1(Q MIXER)/PT/BM1 SCRUBBER SC-101-PT-101 DATA/"

#change the current working directory into the parent directory of the file location
os.chdir(file_location)
os.chdir("..")

# create a new directory for the csv file using os module
csv_folder_name = file_location.split("/")
csv_folder_name = csv_folder_name[len(csv_folder_name) - 2] + "_csv"

# set csv_file_location where new csv files will be stored
csv_file_location = os.path.abspath(os.curdir) + "/" + csv_folder_name
csv_file_location = csv_file_location + "/"

try:
    os.mkdir(csv_folder_name)
except:
    sys.exit("There's already a cvs folder created")

# extract a list of target file names
dirlist = os.listdir(file_location)
target_file = []

for line in dirlist:
    ## regular expression to find a format "0000 00 00 0014 (Float)"
    regex = re.findall(r"[0-9]{4} [0-9]{2} [0-9]{2} [0-9]{2}[1][4] \(Float\)", line)
    if len(regex) == 1:
        target_file.append(regex[0])

# convert dat to csv using multi-thread processing
def convert_dat_to_csv(file):
    file_name = file
    print("converting... ", file)
    ## using FTViewer's subprocess to run the conversion via command line switch
    viewer_location = file_location + "FTViewFileViewer.exe"
    dat_location = file_location + file_name + ".dat"
    csv_location = csv_file_location + file_name + ".csv"
    subprocess.run([viewer_location,"/sd", dat_location, csv_location], shell=True)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(convert_dat_to_csv, target_file)

# time counter to measure program performance
print("Finished in %s seconds" % (round(time.time() - start_time, 3)))