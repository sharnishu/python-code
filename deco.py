# dacorator:
# --------->dacorate function
# ---> to inhance the functionality an function

# create decoration

def daco (x):
    def waper():
        print("welcome to my function....")
        print("desigend by sharn")
        x()
        print("thank you for using me")
    return waper

# # we will run that code and cehak the output
# # next .......>

@daco
def xyz():
    print("heloo......")
# xyz()
@daco
def hlo():
    x = int(input("enter your first number"))
    y = int(input("enter your secound number"))
    z = x + y 
    print(z)
hlo()

def daco (x):
    def waper(a ,b ):
        print("welcome to my function....")
        print("desigend by sharn")
        x(a,b)
        print("thank you for using me")
    return waper

# when we have perametrs and arguments ,that time we are use this type of decorators

@daco
def summ(a,b):
    c = a+b
    print(c)
summ(20,30)



# iii) situation:-

def daco (x):
    def waper(*args,**kwargs ):
        print("welcome to my function....")
        print("desigend by sharn")
        x(*args,**kwargs)
        print("thank you for using me")
    return waper


@daco
def summ(a,b,c,d):
    f = a+b+c+d
    print(f)
summ(20,44,45,66)





# program of class veriable:-

    # Class variable
class Student:
    school_name = 'ABC School '
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)


# output :-
# Emma 10 ABC School 
# Jessa 20 ABC School 


#  Access Class Variable in the constructor
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name):
        self.name = name
        # access class variable inside constructor using self
        print(self.school_name)
        # access using class name
        print(Student.school_name)

# create Object
s1 = Student('Emma')