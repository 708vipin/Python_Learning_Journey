lucky_numbers = [2,3,5,7,11,13,17]
friends = ["Rahul", "Shubhanshu", "Divyanshu", "Ram", "Shyam"]

#extend() function: used to append one list to another
friends.extend(lucky_numbers)
print(friends)

#append() function: used to add items onto the end of a list
friends.append("Saddam")
print(friends)

#insert() function: used to add items anywhere in the between the ends of the list
friends.insert(1, "Tripurari")
print(friends)

#remove() function: used to remove any item of the list
friends.remove(11)
print(friends)

#pop() function: removes the last element of the list
friends.pop()
print(friends)

#Check if a specific item is in a list
print(friends.index("Ram"))

#Check how many times an item is in the list
print(friends.count("Shyam"))

#sort() function: To sort the list in ascending order
lucky_numbers.sort()
print(lucky_numbers)

#reverse() function: To reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

#copy() function: To create a copy of a list
friends2 = friends.copy()
print(friends2)

#clear() function: empty the list
friends.clear()
print(friends)



