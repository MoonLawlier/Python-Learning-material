#function is a block of code that once initialised can be performed at any part of the code
''' Syntax:
         def var_name(par1,par2...):    ---> () can be empty
              return some work'''

'''to use it:
       var = name(arg1, arg2, ...)
       print(var)'''

#Ex 1: Print the sum of two numbers
'''def cal_sum(a,b):
    return a + b

sum = cal_sum(3000, 2000)
print(sum)'''

#ex 2: print hello 5x.
'''def p():
    print("Hello") ---> without input, without output function example
#when a function doesn't return any value and we try to print it, it returns none!
p()
p()
p()
p()
p()'''

#ex 3 : add two strings
'''def add_strings(a,b):
    new = print(a + b)
    return new

add_strings("Sher","Liam")'''

#ex 4: average of 3 numbers
'''def avg(a,b,c):
   avg1 = print((a+b+c)/3)
   return avg1

avg(1000,2000,3000)'''


'''#Seperator and end of a print function
print("It's me",end = "$")
print("Manaswi") 
#print have built in return set stating that you have seperator as " " and end="\n"
print("It's me","reach", sep= "*")''' 
 
#Their are 2 types of function in python:
# Built in functions of python: print(), len()--> {for mearuring length}, type()--->{for classyfying our variable type}, range()
# user defined functions = the functions we are writing!

#EX 5: convert usd to inr
'''def convert(usd_value):
    inr_value = usd_value * 83
    print(usd_value,"USD","=",inr_value,"INR")

convert(1)'''
#ex 6: WAP to print the length of a list 
'''def cal(my_list):
    return (len(my_list))

    

length = cal([1,2,3,4,52,58,56,6841,6554,515,684])
print(length)'''

#ex 7: WAP to print the elements of a list in a single line.
#?
#ex 8 : WAP to find the factorial of n.
'''def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        i += 1
    print(fact)

cal_fact(3)'''

#ex 9: Wap take an input and check whether even or odd

'''def check(n):
    if n%2 == 0:
        print("Even")
    else:
        print("ODD")

check(5446565.54541)'''

#Recursion = when function calls itself repeatedly || hard version of loops 
#ex 1: WAF for factorial 
'''def fact(n):
    if ( n==1 or n==0):
        return 1
    return fact(n-1)*n

one = fact(3)
print(one)'''

#ex 2:write a recursive function to calculate the sum of first n natural numbers.
'''def sigma(n):
    c = n*(n+1)
    return c / 2

hey = sigma(3)
print(int(hey))'''

#ex 3: WAF to print all elements in a list.

#ex 4: waf name reverse which gets a list of numbers as arguments and return the reversed list
'''def reverse(lst):
    lst.reverse()
    return lst

new_lst = reverse([1,2,3])
print(new_lst)'''

#ex 5:Create a function named values that receives a list as an argument and prints all of the items in the list one after the other.
'''def values(lst):
    for i in range(len(lst)):
        print(lst[i])
        i += 1

new = values([5,9,2,10,2])
print(new)'''

#ex 6:Create a function names transpose that receives one argument: A list that contains lists. and returns a modified list.Your task is to swap the rows and columns of the list. This is usually referred to as transpose in mathematics.
'''def WhatToBuy(price_lst,quantity_lst,budjet,name_lst):
    for i in range(len(price_lst)):
        for j in range(len(quantity_lst)):
            new = quantity_lst[j] * 1
            j += 1
        new_lst = new * price_lst[i]
        i += 1
        return new_lst
    
here = WhatToBuy([6,2],[2,1],10,['table'])
print(here)'''

'''def prod(lst):
    product = 1
    for num in lst:
        product *= num
        num += 1
    return product

new = prod([1,3,3])
print(new)'''


#Lambda function: small functions to transform something
# syntax:- var = lambda parameters : expression
#ex:- 
'''double = lambda x: x*2
cube = lambda x: x*x*x
avg  = lambda x,y,z : int((x+y+z)/3) 
appl = lambda fun, val :  val + fun(val)
print(cube(2))
print(double(2))
print(avg(3,4,1))
print(appl(cube, 2))

#map : higher order function = which takes parameters as function
l = [1,2,3,4]  
sq = lambda x: x*x

newl = list(map(sq,l))
print(newl)

#Filter: takes a function and an iterable
def filter_function(a):
    return a>1

new_newl = list(filter(filter_function, l))
print(new_newl)

#Reduce 
from functools import reduce

prod = lambda x,y : x*y
num = [1,2,3,4]
my_prod = reduce(prod,num)
print(my_prod)'''

def addTwoNumbers(l1, l2):
        new1 = int(map(''.join(l1.reverse())))
        new2 = int(map(''.join(l2.reverse())))
        add = new1 + new2
        return add

var = addTwoNumbers([2,4,3],[5,6,4])
print(var)

