# Class is basically the blueprint for objects.
# Object are the production generated out pf class
#---We cannot directly use class in our code, Thus we need to use objects---

'''Syntax: class class_Name:
                related_infos = "related_info" 
                
            variable = class_name()------------------>object
            print(variable.related_infos)...'''

#ex:
'''class Car:
    color = "blue"
    brand = "Porsche"

car1 = Car()
car2 = Car()
print(car1.color)
print(car2.brand)'''

#__init__() function --------------> constructor
#Parameterized constructor-----> These are the constructor with arguments or parameters.
'''class Students:
    def __init__(self,name,roll_no): #------------> self can be changed to any name but self is good!
        self.name = name
        self.roll = roll_no
s1 = Students("Moon",96)#--------> these stored data or variables are known as attributes
print(s1.name, s1.roll)
s2 = Students("Asplin",1)
print(s2.name, s2.roll)'''

#default constructor:
'''class Anything:
    def __init__(self):
        pass #---------> Not used much'''


'''ATTRIBUTES 
   1) class.attr = class attributes
   2) obj.attr   = instance attributes '''

#ex: 
'''class Students:
    college_name = "Great World children's association"
    name = "Anonymous"#---->  priority : obj attr> class attr
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
s1 = Students("Moon", 96)
print("Name:",s1.name,"\nRoll no.:",s1.roll_no,"\nCollege name:",s1.college_name)'''


#Methods : 
'''class Students:
    def __init__(self,name):
        self.name = name
       
    def welcome(self):#-------> metod
        print("Welcome student",self.name)
s1 = Students("Asplin")    
print(s1.welcome())'''

#ex : create student class that takes name and marks of three subjects as argumates in constructor. then create a method to print their average
'''class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.marks1 = marks1 
        self.marks2 = marks2 
        self.marks3 = marks3
        self.name = name
    def avg(self):
        average = int(((self.marks1 + self.marks2 + self.marks3)/3))
        print(average)

s1 = Student('Asplin',96,99,95)
s1.avg()

#or
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hello there",self.name,"your average score is",int(sum/len(self.marks)))
s1 = Student("Asplin",[99,98,99,97,98,99])#------>object atribute
s1.get_avg()

#Staric Methods: ---> methods not using self parameter. (works at class level)
class Student:
    @staticmethod   #decorator
    def college():
        print("Hello!")

FOUR PILLARS OF OOP!
    1)Abstraction 
    2)Encapsulation
    3)Inheritence
    4)Polymorphism

#Abstraction: not clear/unnnecessray info Hidden from user.(basically everything we were writing inside the code)
#define :- Hiding the implementation details of a class and only showing the essential features to the user.
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clth = False
    def start(self):
        self.acc = True
        self.clch = True
        print("Car Started")
car1 = Car()
car1.start()

#Encapsulation: Wrapping data and related funtions into a single unit. (everything we were wtiting so far in a class was encapsulated)

#ex:- create an account class with 2 attributes-balance and account no. create methods to debit,credit and printing balance
class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc
    def debit(self, amtd):
        self.bal -= amtd
        print(" Rs.",amtd,"was debited from your account no.",self.acc,"\n","total balance = ",self.get_balance() )
    def credit(self, amtc):
        self.bal += amtc
        print(" Rs.",amtc,"was credited in your account no.",self.acc,"\n","total balance = ",self.get_balance() )
    def get_balance(self):
        return self.bal

s1 = Account(12000, 859437803)
s1.debit(1000)
s1.credit(5000)'''

#del is a key word to delete some specific properties or deleting the whole object.
#ex: del s1-------->for deleting object
#ex: del s1.name--->for deleting object name
'''class Student:
    def __init__(self,name):
        self.name = name
        
s1 = Student("Moon")
print(s1.name)
del s1.name
print(s1.name)'''       

#Private(like) attribute & methods
# to privatise any information we simply put two unerscores at the start.
#ex:
'''class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("123456","asdf")
print(acc1.acc_no)
#
# print(acc1.acc_pass)'''

#Inheritance: when one class (child / derived) derives the properties and methods of another class (parents / base).
#Types: 1) Single Inheritance   2)Multi-level Inheritance    3) Multiple Inheritance

#ex: Single class:- from single parent to single child
'''class Car:

    @staticmethod
    def start():
        print("Car started...") 

class New(Car):
    #same code as car + modifications
    def __init__(self, name):
        self.name = name
        print(self.name)

car1 = New("fortuner")
print(car1.start())'''

#Multi-level Inheritance:- from grandparents and parents to child  base(parent)--->derived1 (child / parent)--->derived(child)...
'''class Car:
    @staticmethod
    def start():
        print("Car started...") 

class New(Car):
    #same code as car + modifications
    def __init__(self, name):
        self.name = name
        print(self.name)

class New_Car(New):
    def __init__(self, fuel):
        self.fuel = fuel

car1 = New_Car("diesel")
print(car1.start())'''

#Multiple inheritence:- child class derived from more than one parent class
'''class A:
    str1 = "Welcome to class A"
class B:
    str2 = "Welcome to class B"
class C(A,B):
    str3 = "Welcome to class C"

c1 = C()
print(c1.str1)
print(c1.str2)'''         


lst = [1,2,3,4,5]
print(lst[5])

    



