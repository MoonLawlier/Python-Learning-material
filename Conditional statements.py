#Conditional statements { if, elif, else}
'''if (condition):
    statement 1
elif(condition 2):
    statement 2
else:
    statement n'''
#Example 1: Can vote or not
'''age= int(input(" age: "))
if(age>=18):
    print("Can Vote!")
else:
    print("Cannot Vote")'''
#Example 2: Traffic light 
'''color= input("color: ")
if(color == 'Red'):
    print("Stop your vehicle")
elif(color == 'Yellow'):
    print("Wait for the signal to be green!")
elif(color == 'green'):
    print("You can go!")
else:
    print("Light is broken!")'''
#Better version of example 2:
'''color= input(" color of light: ")
if(color == "Red"):
    print(" STOP!")
elif( color == "Yellow"):
    print(" Wait")
elif ( color == "Green"):
    print("GO!")
else:
    print("Light is broken!")'''
#Example 3: Gradding of students
'''percentage = int(input(" Enter your percentage: "))
if(percentage >= 90):
    print("A+")
elif(percentage >=75 and percentage <= 90):
    print("A")
elif(percentage >= 60 and percentage <= 75):
    print("B")
elif(percentage >= 35 and percentage <= 60):
    print("C")
else:
    print("F")'''


#Single line conditional statement 
# Syntax: variable = value1 if condition else value2
# or statement 1 if conndition else statement 2
'''food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")'''

#Clever if 
#Syntax: variable = (false value, true value)[condition]
#Example 4: can vote with clever if
'''age = int(input(" Your age: "))
vote = ("No","yes")[age > 18]
print(vote)'''
#Example 5: Tax on salary
'''sal = int(input(" Your Salary: "))
tax = (0.1 * sal, 0.2 * sal)[sal > 50000]
print(tax)'''

#Nesting: 
#syntax: statement inside a statement 
#Example:
age = int(input("age: "))
if(age >= 18):
    if(age >= 80):
        print("cannot drive!")
    else:
        print("can drive")
else:
    print("cannot drive")
        
   

