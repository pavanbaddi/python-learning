name="pavan"

def change_name():
    global name
    name="Harish"
    print("inside function {}".format(name))

# change_name()

print("outside function {}".format(name))