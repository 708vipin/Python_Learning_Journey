
#Usage of try_except block - to account for inocrrect input

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")