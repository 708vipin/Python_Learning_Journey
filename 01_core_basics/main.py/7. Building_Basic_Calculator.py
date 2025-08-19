num1 = input("Enter a number")                 #By default python treats ANY input as string.
num2 = input("Enter another number")
# result = num1 + num2                           #This will add just two strings
# result = int(num1) + int(num2)                 #This will add only integers (give error for decimal values)
result = float(num1) + float(num2)
print(result)