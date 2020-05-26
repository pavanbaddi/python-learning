#Printing numbers square using while loop
number = 5;
index = 0;
while index <= number:
    print(index**2)
    index+=1

0
1
4
9
16
25

#Printing numbers square using for loop
number = 5
for index in range(0, number+1):
    print(index**2)

0
1
4
9
16
25

# Printing even numbers square using while loop
number = 8
index = 0
while index <= number:
    if (index%2)==0:
        print(index**2)
    index+=1

0
4
16
36
64