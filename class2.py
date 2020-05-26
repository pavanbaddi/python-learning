class Login:
    fname = "pavan"
    lname = "baddi"
    password = ""
    orginal_password = "123456"

    def fetchUserData(self):
        print("entered")
        return self.fname+" "+self.lname;

login = Login()

# print(login)
x = login.fetchUserData();
print(x)