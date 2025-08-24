# r - read mode
# w - write mode - removes everything and writes the new entry
# a - append info at the end
# r+ - read & write



employee_file = open(r"C:\Users\pvipi\Desktop\VIP_GitHub\Python_Learning_Journey\01_core_basics\main.py\25a. employees.txt", "r" )

print(employee_file.readable())           #To check if a file is readable -> readable()
print(employee_file.read())               #To read the whole file
print(employee_file.readline())           #Read the first line
print(employee_file.readlines()[1])       #Read all the arrays and put them in a array and extract the one at index 1
employee_file.close()                     #Remember to close the files.

