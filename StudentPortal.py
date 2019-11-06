#A program to maintain a common database of subjects chosen by different students of a school.
#Students can create their own username and passwords and enter their subjects.
UserDetails = {}
class Student():
    def __init__(self):
        self.subjects = []
    def checkPass(self, password):
        digit, char, leng = False, False, False
        for x in password:
            if x.isdigit():
                  digit = True
            elif not x.isalpha():
                  char = True
        if len(password)>=6:
            leng = True
        if digit == True and char == True and leng == True:
            status = True
        else:
            status = False
        return status
    def signUp(self):
        userName = input("Enter your user name: ")
        password = input("Enter your password: ")
        status = self.checkPass(password)
        while status == False:
            print("Enter a password with atleast six digits.")
            print("Password should contain atleast 1 symbol and 1 digit")
            password = input("Enter password: ")
            status = self.checkPass(password)
        UserDetails[userName] = (password, self)
        print("Signed up successfully")
    def logIn(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if UserDetails.get(username) == None:
            print("Sorry, the username and password do not exist. ")
            return False
        else:
            obj = UserDetails[username]
            self.subjects = obj[1].subjects
            if password == obj[0]:
                return True
            else:
                while password!=obj[0]:
                    print("Incorrect password")
                    password = input("Enter password: ")
    def enterSubjects(self):
        choice = 1
        while choice == 1:
            subject = input("Enter subject: ")
            subject = subject.title()
            self.subjects.append(subject)
            print("Current subjects are: ",self.subjects)
            print("Press 1 to enter more subjects, 2 to stop entering subjects")
            choice = int(input())
    def viewSubjects(self):
        print(self.subjects)
        choice = int(input("Enter 1 to choose more subjects, 2 to stop: "))
        if choice == 1:
            self.enterSubjects()
temp = True
while temp == True:
    result = False
    while result == False:
        choice = int(input("Press 1 for log in and 2 for sign up: "))
        s1 = Student()
        if choice == 1:
            result = s1.logIn()
        else:
            s1.signUp()
            result = True
    print("Welcome! ")
    choice = int(input("Press 1 to choose subjects and 2 to view subjects:"))
    if choice == 1:
        s1.enterSubjects()
    else:
        s1.viewSubjects()
    print("Enter 1 to log out, 2 to exit")
    choice = int(input())
    if choice == 2:
        temp = False

