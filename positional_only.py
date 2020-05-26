
# 1. a normal function with arguments
# def show_student_details(fname, lname="", age=""):
#     print(f"Student name is {fname} {lname} and this age is {age}")


# show_student_details("pavan", "baddi", 26)

#-----------------
# start small example of positional params
def my_func(a, b, c, /):
    print(f"""
        a : {a} \n
        b : {b} \n
        c : {c} \n  
    """);

#my_func(11,12,10)#works
#my_func(a=11,b=12,c=10) #works

#after adding positional /
#my_func(a=11,b=12,c=10) # when added / the throws  TypeError: my_func() got some positional-only arguments passed as keyword arguments: 'a, b, c'

#my_func(10,11,12) #works

#-------------
# function with both positional and named args
def test_func(a,b,c,/,**kwargs):
    print(f"""
        a : {a} \n
        b : {b} \n
        c : {c} \n  
        d : {kwargs['d']} \n  
        e : {kwargs['e']} \n  
    """);


#test_func(10,11,12,13,14) #works
#test_func(10,11,12,d=13,e=14) #works
#test_func(10,11,12,e=14,d=13) #works even if we switch position on d and e
#test_func(10,11,c=12,e=14,d=13) #does not work throws  got some positional-only arguments passed as keyword arguments: 'c'
test_func(10,11,12,e=14,d=13) #works




# def add_marks(englist)
