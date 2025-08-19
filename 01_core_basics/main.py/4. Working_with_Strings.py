import os
os.system('cls')  #To clear Console

print("Giraffe Academy")
print("Giraffe \nAcademy")             #To add a new line \n
print("Giraffe \" Academy")            #Escape Character

phrase = "Giraffe Academy"             #Creating a VARIABLE
print(phrase + "is cool")

print(phrase.lower())                  #converts to lowercase
print(phrase.islower())        
print(phrase.upper().isupper())        #Combining functions  
print(len(phrase))                     #length of a string
print(phrase[0])                       #Indexing - starts with 0 -Grab a specific character in the string
print(phrase.index("G"))               #Index of a character in a string
print(phrase.index("cad"))
print(phrase.replace("Giraffe", "Elephant"))

