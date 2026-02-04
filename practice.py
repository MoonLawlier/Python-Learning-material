#Q1] write a program to input 2 numbers and print their sum
'''num1 = int(input("num1: "))
num2 = int(input("num2: "))
sum = num1 + num2
print("Answer = ",sum)'''

#Q2] write a program to enter side of a square and print its area
'''side = float(input(" enter the value of the square's side: "))
area = side*side
print(area)
side **= 2
print(side)'''

#Q3] wap to input 2 floating numbers and print their average
'''num1 = float(input("num1= "))
num2 = float(input("num2= "))
avg = (num1 + num2)/2
print("average of the given two numbers is= ",avg)'''

#Q4] wap to input 2 int numbers, a and b. print true if a is greater than or equal to b. if not print false
'''a = int(input(" num1: "))
b = int(input("num2: "))
print(a >= b)
print(not(a >= b))'''

#Q5] wapto input user's first name and print its length
'''name = input("name: ")
length = len(name)
print(length)'''

#Q6] wap to find the occurrence of '$' in a string
'''str = input(" str : ")
print(str.count("$"))'''

#Q7] wap to check if a number entered is even or odd
'''n = float(input("no. :"))
if ( n%2 == 0):
    print(" The given number is even.")
else:
    print("The given number is odd.")'''

#Q8] wap to find the greatest of 3 numbers entered by user
'''num1 = float(input(" num1: "))
num2 = float(input(" num2: "))
num3 = float(input(" num3: "))
if (num1 >= num2 and num1 >= num3):
    print("num1 is the greatest")
elif (num2 >= num1 and num2 >= num3):
    print(" num2 is the greatest")
else:
    print("num3 is the greatest")'''


#Q9] wap to check if a number is a multiple of 7 or not
'''num = float(input("num: "))
if ( num%7 == 0):
    print("Yes! This number is divisible by 7.")
else:
    print("No! This number is not divisible by 7.")'''

#Q10] wap to ask the user to enter names of their 3 favorite movies and store them in a list
'''mov1 = input(" mov1: ")
mov2 = input(" mov2: ")
mov3 = input(" mov3: ")
movie = [ mov1, mov2, mov3]
print(movie)
#or
movie = []
movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)'''

#***wap to check if a list contains a palindrome of elements.***
'''list = [1,2,2,1]
list1 = list.copy()
list1.reverse()
if(list == list1):
    print("yes")
else:
    print("no")

#wap to count the number of students with the "A" grade in the following tuple.
tuple = ("A","A","A","B","C","D")
tup1 = tuple.count("A")
print(tup1)

#store the above values in a list &sort them from "A" to "D
list = [ "A", "C", "F", "A", "D", "A"]
list.sort()
print(list)'''

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with sn empty dictionary and add one by one.
'''sub1 = int(input("sub1: ")) 
sub2 = int(input("sub2: ")) 
sub3 = int(input("sub3: ")) 
score = { }
print(score)
sub_1 = { "sub1": sub1}
score.update(sub_1) 
sub_2 = { "sub2": sub2}
score.update(sub_2)
sub_3 =  { "sub3": sub3}
score.update(sub_3)
print(score)'''

#Store 9 and 9.0 as two different values in the set.
'''store = set()
val1 = ("float",9.0)
val2 = ("int", 9)
store.add(val1)
store.add(val2)
print(store)'''
#or
'''store = { "9" , 9.0}
print(store)'''

#Bex 1:WAP to find the sum of first n numbers.(using while)
'''n = 2
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum = ",sum)'''

 #fun = values --> arg = list
 #  it prints the values of list one after another
 # to iterate over a list use range(len(my_list)):
 #                                my_list[i] 

#ex : change an element in a list using fun.
'''def change_element(lst,inx,new_element):
    lst.insert(inx, new_element)
    lst.pop(inx + 1)
    return lst
    
new_lst = change_element([1,2,3],0,9)  
print(new_lst)'''

'''#ex : WAF to get the numbers of the lst as arguments and multiply them all.
ex :The first input indicates how many times to do iterations, and the last two inputs are numbers that we will do operations on.

Create a function that receives two arguments and returns the bigger number of the two. if both are equal then return one of them.

Iterate iterations times and for each iteration do:

Call the function with num1, num2, and save the result in a variable.
Divide the bigger number of the two by 2, and then replace the original larger variable with the new result value.
print the new value.  
Continue doing it until the program iterated iterations times or one of the numbers is smaller than 2.

def bigger(iteration,n1,n2):
    greater = max(n1,n2)
    for i in range(iteration):
        greater /= 2
        i += 1
        if greater < 2:
            continue
        print(greater)
    return greater
def bigger(n1,n2):
    greater = max(n1,n2)
    return greater
iterations = int(input())
n1 = int(input())
n2 = int(input())
for i in range(iterations):
    if n1 < 2 or n2 <2:
        break
    old = bigger(n1,n2)
    old /= 2
    print(old)'''


#ex : evaluate the difference and age of your twin brother while you stay in neverland.
'''in1 = int(input())
in2 = int(input())
x = in1 + in2
y = x - in1
print("My twin is",x,"years old and they are",y,"years older than me")''' 
#ex : count the vowels of the string.
'''your_string = input()
lst = list(your_string)
for counter in lst:
    if counter != 'a' or counter !='e' or counter != 'i' or counter != 'u' or counter != 'A' or counter != 'E' or counter !='I' or counter !='O' or counter != 'U':
        continue
    counter += 1
print(counter)'''

#ex : Do you need batman for your backup?
'''criminals = int(input()) 
if criminals < 5:
    print("I got this!")
elif criminals >= 5 and criminals < 10:
    print("Help me Batman")
else:
    print("Good Luck out there!")'''

#ex : Which currency to use?

'''pesos = int(input())
dollars = int(input())
cents = 1
dollars = 100 * cents
pesos = 2*cents
choose = min(dollars,pesos)
if choose == dollars:
    print("Dollars")
else:
    print("Pesos")'''


#ex : calculate the sum of all the multiples of 3 and 5 in the given integer
'''in1 = input()
lst = list(in1)
count = 1
while count <= len(lst):
    if count%3 == 0 or count%5 == 0:
       add = sum(lst.items())
    count += 1
print(add)'''

#ex : determine the no. of flamingoes need to be purchased
'''in1 = int(input())
in2 = int(input())
in1 /= 2
in2 /= 2
out = (in1 + in2)*2
print(int(out))'''

#ex : no. of candles you need to order?
'''in1 = int(input())
print(9 * (in1+1))'''

#ex: cheer leading
'''in1 = int(input())
if in1 >= 10:
    print("High Five")
elif in1 < 1:
    print("shh")
else:
    for i in range(in1):
        print("Ra", end="!")'''

#ex : fruit bowl.
'''in1 = int(input())
if in1%2 == 0:
    in1 = int(in1/2)
    in1 = int(in1/3)
    print(in1)
else:
    print("")'''

#ex [m]: convert us to eu dates
'''in1 = int(input())
in2 = int(input())
in3 = in1 + in2
if in3%3 == 0:
    print("Give away")
else:
    print("eat them yourself")'''

#ex *: alter the first and last element of the string
'''s = "william"
a = list(s)
a[0],a[-1] = a[-1],a[0]
res = ''.join(a)
print(res)'''

#ex : extra-terrestrial language
'''txt = input()[::-1]
print(txt)'''

#ex :skee-ball
'''score = int(input())
price = int(input())
ticket = int(score/12)
if ticket > price:
    print("Buy it!")
else:
    print("Try again")'''

#ex :easter eggs
'''total = int(input())
my = int(input())
his = int(input())
if total == my + his:
    print("Candy Time")
else:
    print("Keep Hunting")'''

#ex : hovercraft:
'''num = int(input())
num *= 3000000
cost = 21000000
if num > cost:
    print("Profit")
elif num < cost:
    print("Loss")
else:
    print('Broke Even')'''

# no.of inputs and sum it all
'''n = int(input())#---- no.of inputs
res = 0
for i in range(n):
    a = int(input())
    res += a
    i += 1
print(res)'''

'''iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1 > arg2:
        return arg1
    else:
        return arg2

for i in range(iterations):
    if num1 < 2 or num2 < 2:
        break
    big = bigger(num1, num2)
    if big == num1:
        num1 /= 2
        print(num1)
    else:
        num2 /= 2
        print(num2)'''

#carrot cake --- (x)
'''carrot = int(input())
box = int(input())
res = carrot * box
if res%2 == 0:
    print("I need to buy 7 more")
elif res%2 != 0:
    pick = res%2
    print("I need to buy",pick,"more")
elif res%2 == 7:
    print("Cake Time")
else:
    print("")'''

#That's odd:
'''n = int(input()) 
res = 0

for i in range(n):
    a = int(input())
    if a%2 == 0:
       res += a
       i += 1
    else:
        continue
       
print(res)'''

#Duty free
'''price = input()
price = int(price)
pricess = price.split(" ")
price_lsts = list(pricess)
for i in price_lsts:
    i *= 1.1
    if i > 20:
        print("On to the teminal")
    else:
        print("Back to the store")
    i += 1'''

#Flat Asterisk pyramid:
'''n = int(input())
if n >= 1 and n<1000:
    for i in range(n):
        if i%2 != 0:
            continue
        for j in range(i+1):
            print("*",end="")
        print("")'''

#Goods and construction
'''def whatToBuy(price,quantity,restriction,names):
    if len(price) == 0 and len(quantity) == 0:
        return [[],0]
    avg_price = sum(price)/len(price)
    avg_quantity = sum(quantity)/len(quantity)
    res = []
    removed = 0
    for i in range(len(price)):
        total = (price[i]*quantity[i])/(avg_price*avg_quantity)
        if total<restriction:
            res.append(names[i])
        else:
            removed += 1
    res.sort()
    return[res,removed]

print(whatToBuy([],[],0.5,[]))

with open("practice.txt","w") as f:

    data = f.write("Hi everyone\nwe are learning File I/O\nusing java\nI like programming in java.")
    print(data)

with open("practice.txt","r") as f:
    data = f.read()
    new_data =data.replace("java","Python")
    print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)'''

#check if word "learning" exist in the file or not
'''with open("practice.txt","r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("found")
    else:
        print("not found")'''
#the line where the word learning occur first
'''def find_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(find_line())
def c(lst):
    return lst[0] + lst[1:-1]
l =c(['c','h','o','c','o','l','a','t','e'])
print(l)'''

#It's a sign
'''a,b,c,d = input("").split()
rev_string = string[::-1]
if string == rev_string:
    print("Open")
else:
    print("Trash")

inp = int(input())
lst = list(inp)
even = []
odd = []
for i in lst:
    if i in range(0,len(lst),2):
        even.append(i)
    else:
        odd.append(i)
print("Sum even:",sum(even))
print("Sum odd:",sum(odd))
   
mov = input()
pop = input()
people = int(input())
pay = int(input())

price = 200

def movie(mov,price):
   if (mov == "comedy"):
      price += 30
      
   elif (mov == "action"):
      price += 40
     
   else:
      price += 20
   return price
print(price)

def popcorn(pop, price):
   if (pop == "S"):
      price += 100
   elif (pop == "M"):
      price += 150
   else:
      price += 200
   return price

print(price)

def payment(pay,price):
   if(pay == 1):
      price = (price - int((price * 10) / 100))*people

   else:
      price *= people

   return price

print(price)



print(f"${price}")

mov = input()    # comedy / action / other
pop = input()    # S / M / L
people = int(input())
pay = int(input())  # 1 = card (10% discount), else = cash

price = 200

def movie(mov, price):
    if mov == "comedy":
        price += 30
    elif mov == "action":
        price += 40
    else:
        price += 20
    return price   # return updated price

def popcorn(pop, price):
    if pop == "S":
        price += 100
    elif pop == "M":
        price += 150
    else:
        price += 200
    return price   # return updated price

def payment(pay, price, people):
    if pay == 1:
        price = (price - int((price * 10) / 100)) * people
    else:
        price *= people
    return price   # return updated price

# Apply functions step by step
price = movie(mov, price)
price = popcorn(pop, price)
price = payment(pay, price, people)

print(f"${price}")'''

#vowel counter:
'''sen = input().strip().lower()
count = 0
for i in sen:
    if (i == 'a' or i == 'e'  or i == 'i'  or i == 'o'  or i == 'u'):
        count += 1

print(count)'''

#popsicles
'''sib = int(input())
pop = int(input())

if pop%sib == 0:
    print("give away")
else:
    print("eat them yourself")'''

#izzy the iguana
'''sen = input().lower().strip()
count = 0
for i in sen:
    if i == "lettuce":
        count += 5
    elif i == "carrot":
        count += 4
    elif i == "mango":
        count += 5
    elif i == "Cheeseburger":
        count += 0
    else:
        count *= 1
print(count)
if count >= 10:
    print("Come on Down!")
else:
    print("Time to wait")'''

#cheer creator 
'''yard = int(input())

if yard > 10:
    print("High Five")
elif yard < 1:
    print("shh")
else:
    print("Ra!"*yard)'''

#Leetcode: add one
'''def one(digits):
    num = int(''.join(str(i) for i in digits))
    num += 1
    nums = str(num)
    nums = list(map(int,nums))
    return list(nums)

var = one([4,3,2,1])
print(var)

def sort(a,b,c):
    lst = list(a,b,c)
    lst = list(map(int,lst))
    for j in range(len(lst)):
        for i in range(len(lst)-i-1):
            if lst[i] > lst[i+1]:
               lst[i],lst[i+1] = lst[i+1],lst[i]
           
    return lst
var = sort(2,5,3)
print(var)'''


'''def removeElement(nums, val):
        for value in nums:
            if value == val:
                nums.remove(value)
                nums.append("_,")
        return nums
        
var = removeElement([3,2,2,3],3)
print(var)'''

'''def hammingWeight(n):
        new = int(n)
        num = bin(new)
        nums = list(num)
        pro = nums.count("1")
        return pro


var = hammingWeight(11)
print(var)
'''
'''a, b, c = map(int,input(" ").split( ))
lst = [a,b,c]
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i],lst[i+1] = lst[i+1],lst[i]
    
print(f"{lst[0]} {lst[1]} {lst[2]}")'''

'''def add(a1, a2, a3):
    lst = [a1,a2,a3]
    var = max(lst)
    var *= var
    lst.remove(max(lst))
    lst.append(var)
    return sum(lst) 

var = add(1,2,3)
print(var)'''

#izzy the iguana
'''dict = {
    "Lettuce" : 5,
    "Carrot" : 4,
    "Mango": 9,
    "Cheeseburger": 0
}

def total_points(foods):
    points = 0'''

'''#password generator
import string
import random
one = random.choices(string.ascii_lowercase,k=2)

three = random.choices(string.ascii_uppercase, k=2)

num1 = random.randint(48,57)
sym = random.choices(string.punctuation,k=2)

str = ''.join(one + three + sym + list(str(num1)))
print(str)'''

'''char = input()
text = input()
lst = list(text)
lst.reverse()
for i in range(len(lst)):
    if i%2==0:
        lst.insert(i,char)
    else:
        continue
    string = ''.join(lst)
print(string)

def count_bits(n):
    bin_num = bin(n)
    bin_lst = list(bin_num)
    cnt_one = bin_lst.count('1')
    return cnt_one

print(count_bits(5))

def get_sum(a,b):
    max_num = max(a,b)
    min_num = min(a,b)
    total = 0
    for i in range(min_num, max_num + 1):
        total += i

    return total

#def get_sum(a,b):
#    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum(-1,1))

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False

print(validate_pin('a234'))

def delete_nth(order,max_e):
    new = []
    for x in order:
        if new.count(x) < max_e:
            new.append(x)
        else:
            continue
    return new

print(delete_nth([20, 37, 20, 21], 1))
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print(longest("aretheyhere", "yestheyarehere"))

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i])==sum(arr[i+1:]):
            return i
    return -1
    
print(find_even_index([1,2,3,4,3,2,1]))


from collections import Counter
def duplicate_count(text):
    text = text.lower()
    cnt = 0
    count = Counter(text)
    for value in count.values():
        if value>1:
            cnt += 1
    return cnt'''

def hashtag(s):
    lst = list((s.capitalize()).split( ))
    lst[0]='#'
    return ''.join(lst)

print(hashtag("code wars"))
    


