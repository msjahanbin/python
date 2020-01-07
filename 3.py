#import
import re

class Checkregister:
    def __init__(self,name,lastname,username,password,email,mobile,code):
        self._name=name
        self._lastname=lastname
        self._username=username
        self._password=password
        self._email=email
        self._mobile=mobile
        self._code=code
    
    def checkname(self,name): #Checking the name returns one if true and returns 0 if it is wrong
        Name= re.findall(r'\b[a-zA-Z]{2,21}\b',name)
        if Name!=[]:
            return 1
        else:
            return 0

    def checklastname(self,lastname): #Checking the last name returns one if true and returns 0 if it is wrong
        LastName= re.findall(r'\b[a-zA-Z]{2,30}\b',lastname)
        if LastName!=[]:
            return 1
        else:
            return 0

    def checkusername(self,username): #Checking the user name returns one if true and returns 0 if it is wrong
        UserName= re.findall(r'\b\S[a-zA-Z@_]{5,50}\b',username)

        if UserName!=[]:
            if username.lower()=='username':
                return 0
            else:
                return 1
        else:
            return 0

    def checkpassword(self,password): #Checking the password as a number first, then a lowercase letter and then a lowercase Latin letter returns one if true, and returns 0 if it is wrong.
        Password= re.findall(r'\S(?=.*\d)(?=.*[a-z@&_%$])(?=.*[A-Z]).{8,50}\b',password)
        if Password!=[]:
            return 1
        else:
            return 0

    def checkemail(self,email): #Checking the email structure returns one if true and returns 0 if it is wrong
        Email= re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b',email)
        if Email!=[]:
            return 1
        else:
            return 0

    def checkmobile(self,mobile): #Checking the mobile number returns one if true and returns 0 if it is wrong
        Mobile= re.findall(r'(09[0-9]{9}|\+98[0-9]{10})',mobile)
        if Mobile!=[]:
            return 1
        else:
            return 0

    def checkcode(self,code): #Checking the national code returns 1 if it is correct and returns 0 if it is incorrect
        if not re.search(r'^\d{10}$',code):
            return 0

        check = int(code[9])
        s = sum([int(code[x]) * (10 - x) for x in range(9)]) % 11
        if (s < 2 and check == s) or (s >= 2 and check + s == 11):
            return 1

if __name__=='__main__':
    check=[]
        
    name=input('Enter your name:')
    check.append(Checkregister.checkname('self',name))

    lastname=input('Enter your lastname:')
    check.append(Checkregister.checklastname('self',lastname))

    username=input('Enter your username(Avoid writing "usename" and "admin"):')
    check.append(Checkregister.checkusername('self',username))

    password=input('Enter your password(for example:123mryAM):')
    check.append(Checkregister.checkpassword('self',password))

    email=input('Enter your email:')
    check.append(Checkregister.checkemail('self',email))

    mobile=input('Enter your mobile number:')
    check.append(Checkregister.checkmobile('self',mobile))

    code=input('Enter your natioal code:')
    check.append(Checkregister.checkcode('self',code))

    m=1
    for i in check:
        m=m*int(i)
    if m==1:
        print('register Ok!')
    else:
        print('regiter Error')
        
