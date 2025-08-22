# r - read mode
# w - write mode
# a - append info at the end
# r+ - read & write



employee_file = open(r"C:\Users\pvipi\Desktop\VIP_GitHub\Python_Learning_Journey\01_core_basics\main.py\25a. employees.txt", "r" )

print(employee_file.readable())           #To check if a file is readable -> readable()
print(employee_file.read())
employee_file.close()

