is_male = True
is_tall = True

if is_male or is_tall:
    print("You are tall or male or both")
elif is_male and not(is_tall):
    print("You are a short male")    
else:
    print("You are neither male nor tall") 