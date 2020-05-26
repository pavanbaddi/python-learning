

class Person:
    
    def __str__(self):
        return "{} | {}".format(self.name,self.age)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "Name : {} \nAge : {}\n".format(self.name, self.age)