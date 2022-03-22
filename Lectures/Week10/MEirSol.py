import os, shutil

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

top_level_directory = "C:/Users/dylan/Desktop/into_to_programming/Lectures/Week10/temperature"

'''
PART 1: MAKE THE DIRECTORY STRUCTURE
'''
os.mkdir(top_level_directory)
os.chdir(top_level_directory)

years = list(range (2000, 2011, 1))
for year in years:          #first iteration the year will be 2000
    os.mkdir(str(year))
    os.chdir(str(year))
    for month in months:
        os.mkdir(month)
    os.chdir(top_level_directory)   

'''
PART 2: RENAME THE EXISTING FILES
'''
ak_temperature_path = "C:/Users/dylan/Desktop/into_to_programming/Lectures/Week10/temperature"
os.chdir(ak_temperature_path)

#pull out all the filenames
files = os.listdir(ak_temperature_path)
print (files)
#parse out the month and year
for file in files:
    month = file[12:14]
    if "." in month:
        month = month.rstrip(".")
    #month number to correspond to an actual month
    month = months[int(month)-1]
    year = file[-8:]
    newName = month + "_" + year
    #rename the file
    os.rename(file, newName)

# An alternative way to parse the year and month would be to use .split e.g.
'''
for file in files:
    fileParts = file.split(".")
    month = months[int(fileParts[3]) - 1]
    year = fileParts [4] + "." + fileParts[5]
    newName = month + "_" + year
    os.rename(file, newName)
'''

'''
PART 3: MOVE THE FILES TO THE DIRECTORY STRUCTURE WE CREATED
'''

os.chdir(ak_temperature_path)
files = os.listdir(ak_temperature_path)

for file in files:
    source = file
    fileParts = file.split("_")
    month = fileParts[0]
    year = fileParts[1].strip(".txt")
    destination = top_level_directory + "/" + year + "/" + month
    shutil.move(source, destination)
