# class Teacher:

#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def show(self):
#         return '''
#             name   : {}\n  
#             course : {}\n  
#             age    : {}\n  
#         '''.format(self.name, self.course, self.age)

# t1 = Teacher("Suresh", "28", "Maths") #passing instance variables

# print(t1.show()) #show is a instance method

#Class Methods 1
# class Teacher:

#     institute_name = "ABC Institute of Technology"
    
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def show(self):
#         return '''
#             name   : {}\n  
#             course : {}\n  
#             age    : {}\n  
#         '''.format(name, course, age)

#     @classmethod
#     def get_institute(cls):
#         return cls.institute_name

# t1 = Teacher("Kiran", "35", "Science")
# print(t1.get_institute()) #Call classmethod using instance t1
# print(Teacher.get_institute()) #Call classmethod using class Teacher

#Class methods 2
# class Teacher:
#     number_of_teachers_in_institute = 0   
#     institute_name = "ABC Institute of Technology"
    
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
    
#     def show(self):
#         return '''
#             name   : {}\n  
#             course : {}\n  
#             age    : {}\n  
#         '''.format(name, course, age)

#     @classmethod
#     def get_institute(cls):
#         return cls.institute_name

#     @classmethod
#     def set_institute(cls, name):
#         cls.institute_name = name
#         return cls.institute_name


#     def count_teachers_in_institute():
#             pass

# t1 = Teacher("Kiran", "35", "Science")
# t2 = Teacher("Sunil", "42", "Hindi")

# Teacher.set_institute("XYZ institute")

# print(t1.get_institute()) #Call classmethod using instance t1
# print(t2.get_institute()) #Call classmethod using instance t2
# print(Teacher.get_institute()) #Call classmethod using class Teacher

#Static Method

available_courses = [
    "python", "electronics", "cs"
]

class Teacher:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    @staticmethod
    def check_is_course_available(course):
        is_course_available = False
        
        if course in available_courses:
            is_course_available = True

        return is_course_available

t1 = Teacher("Kiran", "35", "science")
t2 = Teacher("Sunil", "42", "english")

print("\nIs Computer Science course available in institute : {}".format(Teacher.check_is_course_available("cs"))) 
print("\nIs Web Development course available in institute : {}".format(Teacher.check_is_course_available("web_development"))) 