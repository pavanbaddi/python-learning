
# on list
mylist = [0,1,False]
x = all(mylist)
print("On list : {}\n".format(x))

# # on tuples 
myTuple = (0, False)
x = all(myTuple)
print("On Tuple : {}\n".format(x))

# on sets
mySet = {0, False}
x = all(mySet)
print("On set : {}\n".format(x))

# on dictionary
myDict = {0 : "james", 0 : 12}
x = all(myDict)
print("On Dictionary : {}\n".format(x))

# on string
myStr = "0"
x = all(myStr)
print("On String {}\n".format(x))
