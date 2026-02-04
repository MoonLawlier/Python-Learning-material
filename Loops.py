#Their are two types of loops in python: for and while
'''Syntax :
   var = conditon maker  
   while condition:
      your code 
      (updation)
                  '''
#Ex: print hello 5x .
'''count = 1  #iterators
while count <= 5:
    print("Hello!", count)
    count += 1
#iteration = no.of times we looped the code
#print(count)'''

#q] print numbers from 1 to 100
'''i = 1
while i <= 100:
    print(i)
    i += 1
print("Loop Ended")'''
#q2]print numbers from 100 to 1
'''i = 100
while i >= 1:
    print(i)
    i -= 1
print("Blast off!")
#q3] print the table of number n.
n = 3
i = 1
while i <= 10:
    print(i*n)
    i += 1
#q4] print the elements of the following list using a loop: [1,4,9,16,36,49,81,100]
nums = [1,4,9,16,36,49,64,81,100]
idx = 0
while idx <= len(nums):
    print(nums[idx]) #--->nums[idx] = gives the names of the list
    idx += 1'''
#q5] search for a number x in this tuple using loop
'''tup =  (1,4,9,16,25,36,49,64,81,100)
x = 49
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found your number at index ", i)
    else:
        print("Not available")
    i += 1'''
     
#Break = terminates the loop
#Conti inue = skips / terminates the loop at the point it is written such that the later code is not executed
'''i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue #will skip 3 because 3 turned 4 as directly went to the loop again
    print(i)
    i += 1
while i <= 5:
    if( i == 3):
        break
    print(i)
    i += 1'''

#for loops are used for the data types which have index like list,tupples,etc.
'''Syntax :
         for element in list:
             some work '''

#ex 1:
'''Anime = ["Solo Leveling", "Demon Slayer","Naruto", "Baruto", "Drangon Ball"]
for name in Anime:
    print(name)'''

#ex 2:
'''Manga = ("Desharow Mermaid", "Lying puppies get eaten", "Heaven's offocial Blessing")
for name in Manga:
    print(name)'''

#ex 3:
'''fav = "SherLiam"
for char in fav:
    print(char)
else:
    print("...")'''

#ex 4:Print the elements of the list 
'''list = [1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)'''

#ex 5:Search for a number x in this tupple
'''tup = (1,4,9,16,25,36,49,64,81,100)
x = 100
idx = 0
for el in tup:
    if(el == x):
        print("x found at index", idx)
        break
    idx += 1
    print(el)
else:
    print("None")'''

#range is a function that returns a number of elements of numbers?, etc.
'''Syntax: 
     range( starting value[optional], stopping value, step size[optional])
     start value = where you wanna start or by default 0,
     stop  value = where you wanna stop (given number not included),
     step  size  = from how much you wanna increase[ by default +1].'''

#ex 1:
'''for i in range(3,31,3):
    print(i)'''

#ex 2:Print numbers from 1 to 100
'''for i in range(1, 101):
    print(i)
print("End")
#ex 3:Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)
print("End this loop!")
#ex 4:Print the multiplication table of a number n
n = 5
for i in range(n, 11*n, n):
    print(i)'''

#pass = pass statement is used when we want our loop or if-else condition to have null value
'''for i in range(6):
    pass

if i >100:
    pass
#it is used to as a placeholder for the future code
#if you laze around or excited about the below code and you just don't want to write te code for the loo or if-else you use pass!
print("9")'''


#Bex 2:Wap to find the factorial of first n numbers. (using for)
'''n = 10
fact = 1
for i in range(1,n+1):
    fact *= i
    i += 1

print("factorial =",fact)

#for i in range(1,n+1,)'''

# to iterate over a list use range(len(my_list)):
 #                                my_list[i] 

def change_elements(lst , index, new_element):
   change = lst.insert(index, new_element)
   change = lst.remove(index + 1)
   return change

new = change_elements(['a','b','c'],1,'d')
print(new)
    

    
