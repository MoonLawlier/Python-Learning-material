#Lists = arrays --------> similar as string
#Syntax: variable_name = [val1, val2, val3 ...]
student = ["Karan", 17 , 65 , "Delhi"]
print(student[0])
student[0] = "Arjun"
print(student[0])
#Slicing:
#Syntax: list_name[starting_index : ending_index]
print(student[1:3])
print(student[-1 : ])

#List Methods:
''' 1) list.append( element )
    2) list.sort()
    3) list.reverse()
    4) list.insert(index , element )
    5) list.remove()
    6) list.pop(index)

    * set(your_list) ----> a built in function to have all the unique values from your_list!    '''

'''list = [2,1,3]
print(list.append(0))
print(list.sort(reverse = True)) #sort is used to sort list in ascending order and if we pass "reverse = True" then decending order.
print(list)'''

list =["Apple", "Blueberry","Banana"]
#print(list.sort(reverse = True)) #sort is used to sort list in ascending order and if we pass "reverse = True" then decending order.
#print(list)
'''list.reverse()
print(list)'''
#list.insert(index, element)
list.insert(0 , "Litchi")
print(list)#append is used to add ana element only at the end of the list while insert can insert an element at any particular index.
'''list.remove("Banana")
print(list)
list.pop(2)
print(list)'''
''' lst = split(lst1)----> splitting the items of the list as individual elements'''

#Mapping:
'''Syntax: 
lst = [expression for item in iterable]'''
nums = eval(input())  # Don't change this line
new_nums = [x**3+2*(x**2)+5 for x in nums]

#Filtering:
'''Syntax:
lst = [expression for item in iterable if condition else condition]'''
words = ['pony', 'confine', 'utter', 'decrease', 'entertain']
filteres_words = [word for word in words if 'a' in word]

print(filteres_words)  # ['decrease', 'entertain']

#special:
#result = [expression for x in lst1 for y in lst2]