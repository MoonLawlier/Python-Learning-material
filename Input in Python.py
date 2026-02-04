#Syntax:
#string input:
'''name = input("name: ")
print(name)
#int input:
age = int(input("age: "))
print(age)
#float input:
salary = float(input("salary: "))
print(salary)
#first it will ask for name , will print name then ask age, print age and so on
#Instead
name = input("name: ")
age = int(input("age: "))
salary = float(input("salary: "))
print(name,age,salary )
print(name)
print(age)
print(salary)'''

#is v/s ==
#since list is mutable python makes two different lists in memory though the values are same.
a = [1,2,3]
b = [1,2,3]

print(a is b) #is checks if the two objects as same memory location , i.e. if a and b are one thing ---> False
print(a == b) #== checks the value and since both values are same ---> True

#but when pyhton deals with immutable things like constants, strings and tupples it do not waste memory and accomodate twp values in pne memory location.
#ex: 
a = 5
b = 5
print(a is b) #is checks if the two objects as same memory location , i.e. if a and b are one thing ---> False
print(a == b) #== checks the value and since both values are same ---> True

