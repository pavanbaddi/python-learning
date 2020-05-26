# import package_a.modules
# p1 = package_a.modules.Person("Ravi", 21)
# print(p1.show())

# from package_a.modules import Person
# p1 = Person("Suresh", 23)
# print(p1.show())


import package_a.sub_package_1.sub_demo1 
from package_a.sub_package_1 import sub_demo1
from package_a.sub_package_1.sub_demo1 import demo1 

package_a.sub_package_1.sub_demo1.demo1()
print('--------------------------\n')
sub_demo1.demo1()
print('--------------------------\n')
demo1()

