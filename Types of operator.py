#Types of operator
''' Arithmetic operators { +,-,*,/,%,**}
    Relational / Comparison Operator { ==, != , >,<, >=, <=}
    Assignment Operators { =, +=, -=, *=, /=, %= , **=}
    Logical Operators {not, and, or}'''

#Arithmetic operators
'''a = 3
b = 4
sum = a+b
diff = a-b
pro = a*b
div = a/b
mod = b%a
pow = a**b
print(sum)
print(diff)
print(pro)
print(div) #div always show answer as a  floating value. 
print(pow) # a^b
print(mod) #mod gives remainder'''

#Relational / Comparison operators
'''a = 50
b = 60
print(a != b)
print(a == b)
print(a >= b)
print(a <= b)'''

#Assignment operator
'''num = int(input("num : "))
num += 10
print(num)
num -= 10
print(num)
num *= 10
print(num)
num /= 10
print(num)
num **= 10
print(num)'''

#logical operator
a = 50
b = 60
val1 = True
val2 = False
print(not(a > b))
print(" answer :", val1 and val2)
print( a == b and a >= b)
print( a == b or a >= b)