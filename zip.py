# Zip is a iterator function which can iterate over one or more list or tuple items.
# This can be helpful when we have two lists that need to be iterated at once.
#
# First we'll look at non-pythonic ways of iterating over many items from different lists in a single loop
# 
# ₹5,976.00
 # 

# start-----
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Suzan")

# x = zip(a,b)

# for i,j in x:
#     print("{} -- {}".format(i,j))
# end-----

# without zip function
# names = ["Sam", "John", "Harry"]
# marks_scored = [78.5,61.5,80]

# i=0
# while i<len(names):
#     print("{} has scored {} marks".format(names[i],marks_scored[i]))
#     i+=1


#with zip function
# names = ["Sam", "John", "Harry"]
# marks_scored = [78.5,61.5,80]
# merged_list = zip(names,marks_scored) 
# for name,marks in merged_list:
#     print("{} has scored {} marks".format(name,marks))

# names = ["Sam", "John", "Harry", "Karen"]
# marks_scored = [78.5,61.5,80]
# merged_list = zip(names,marks_scored) 
# for name,marks in merged_list:
#     print("{} has scored {} marks".format(name,marks))

names = ["Sam", "John", "Harry", "Karen"]
marks_scored = [78.5,61.5,80]
subjects = ["English", "Maths", "Science"]

merged_list = zip(names,marks_scored,subjects) 
for name,marks,subject in merged_list:
    print("{} has scored {} marks in {}".format(name,marks,subject))