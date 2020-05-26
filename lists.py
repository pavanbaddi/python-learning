print("List is a collection which is ordered and changeable, Allows Duplicates")
thisList = ["apple", "banana", "cherry"]
print(thisList)

print("NOW CHANGE THE SECOND ITEM")
thisList[1] = "Black Current"
print(thisList)

print("Create list using list() constructor")
newList = list(("apple", "orange", "mango"))
print(newList)

print("APPEND NEW ITEM TO LIST")
newList.append("Straw Berry")
print(newList)


print("REMOVE ITEM FROM LIST")
newList.remove("Straw Berry")
print(newList)

print("COUNT LENGTH OF LIST ")
print(len(newList))