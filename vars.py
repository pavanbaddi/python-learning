name = "Suresh"
marks = {
    "English" : 68,
    "Maths" : 56,
    "Science" : 87,
}

def change_marks():
    print("Marks Scored By {}\n".format(name))
    
    for index, subject_marks in globals()['marks'].items():
        subject_marks += 2
        print("{} : {}\n".format(index, subject_marks))


# Dictionary of Global variables
print("Global Variables : {}\n\n".format(globals()))

change_marks()

# Updating value of Global variable 
globals()["marks"]["English"] = 44

#Updated value of english
print("\n\nUpdated Global variable marks english : {}\n\n".format(globals()["marks"]['English']))

