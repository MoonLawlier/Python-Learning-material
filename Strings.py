#Ways to write a string:
'''str1 = "This is a string.\n \t hi there!"
str2 = 'This is a string'
str3 = """This is a string"""
print(str1)'''
#Escape sequence characters: characters used to format in python
#basic operations:
#Concatination: adding two strings
'''str1 = "Hi There!"
print(len(str1))
str2 = "I'm Manaswi!"
c = str1 + " "  + str2
print(c)'''
#Indexing: numbering of characters in strings
'''str1 = "Holla!"
print(str1[0])
#slicing: accessing parts of a string'''
#syntax: str[ starting_index : ending_index]
'''str1 = "Manaswi"
print(str1[0:len(str1)])
print(str1[0:])
print(str1[0:5])
print(str1[-5: -1])'''

#String functions:
''' str.endswith(" any_alphabets")
    str.strip()
    str.capitalize()
    str.upper()
    str.lower()
    str.replace( old , new)
    str.find(word)
    str.count(" ")
    str.split()
    '''
#string methods:
'''# Method	    Description
ord()           #Returns the integer representing the ascii value of that character
capitalize()	#Converts the first character to upper case
casefold()	    #Converts string into lower case
center()	    #Returns a centered string
count()	        #Returns the number of times a specified value occurs in a string
encode()	    #Returns an encoded version of the string
endswith()	    #Returns true if the string ends with the specified value
expandtabs()	#Sets the tab size of the string
find()	        #Searches the string for a specified value and returns the position of where it was found
format()	    #Formats specified values in a string
format_map()	#Formats specified values in a string
index()  	    #Searches the string for a specified value and returns the position of where it was found
isalnum()	    #Returns True if all characters in the string are alphanumeric
isalpha()	    #Returns True if all characters in the string are in the alphabet
isascii()	    #Returns True if all characters in the string are ascii characters
isdecimal()	    #Returns True if all characters in the string are decimals
isdigit()	    #Returns True if all characters in the string are digits
isidentifier()	#Returns True if the string is an identifier
islower()	    #Returns True if all characters in the string are lower case
isnumeric()	    #Returns True if all characters in the string are numeric
isprintable()	#Returns True if all characters in the string are printable
isspace()	    #Returns True if all characters in the string are whitespaces
istitle()	    #Returns True if the string follows the rules of a title
isupper()	    #Returns True if all characters in the string are upper case
join()	        #Joins the elements of an iterable to the end of the string
ljust()	        #Returns a left justified version of the string
lower()	        #Converts a string into lower case
lstrip()	    #Returns a left trim version of the string
maketrans()	    #Returns a translation table to be used in translations
partition()	    #Returns a tuple where the string is parted into three parts
replace()	    #Returns a string where a specified value is replaced with a specified value
rfind()	        #Searches the string for a specified value and returns the last position of where it was found
rindex()	    #Searches the string for a specified value and returns the last position of where it was found
rjust()	        #Returns a right justified version of the string
rpartition()	#Returns a tuple where the string is parted into three parts
rsplit()	    #Splits the string at the specified separator, and returns a list
rstrip()	    #Returns a right trim version of the string
split()	        #Splits the string at the specified separator, and returns a list
splitlines()	#Splits the string at line breaks and returns a list
startswith()	#Returns true if the string starts with the specified value
strip()	        #Returns a trimmed version of the string
swapcase()	    #Swaps cases, lower case becomes upper case and vice versa
title()	        #Converts the first character of each word to upper case
translate()	    #Returns a translated string
upper()     	#Converts a string into upper case
zfill()     	#Fills the string with a specified number of 0 values at the beginning
'''

'''str = "i am here!"
print("here" in str) #checks wether the word is present in the string or not and returns boolean value.
print("hello" not in str) #checks wether the word is absent in the string or not and returns boolean value.
print(str.endswith("ere!")) #checks wether the string ends with the letters written inside the double quotes in paranthesis.
print(str.capitalize()) #capitalizes the first letter of the string
print(str.upper()) #converts the whole string to uppercase
print(str.lower()) #converts the whole string to lowercase
print(str.replace("e" , "a")) #replaces the old word to new 
print(str.find("here")) #provides the index no. of the word's first occurence
print(str.count("e")) #count letter or words in the string
print(str.strip()) #removes extra spaces from starting and ending of the string
print(str.split()) #splits the string into list of words wherever there is a space'''


'''def largestOddNumber(num):
        """
        :type num: str
        :rtype: str
        """
        nums = list(num)
        new = []
        if int(num)%2 != 0:
             return num
        else:

            for val in nums:
                if int(val)%2 != 0:
                    new.append(val)
                else:
                    continue
                return max(new)
            return ""
print(largestOddNumber("10133890"))'''

#Slicing : returns a part of the string
'''string = "Moon is Back!"
print(string[3:9]) 
print(string[:5]) #from starting index to 4th index
print(string[5:]) #from 5th index to end
print(string[-5:-2]) '''

#Escape characters: sometimes we need things that aren't technically legal in a string world. So it works like a little cheatsheet.
'''txt = "We are the so-called "Vikings" from the north."-------> this will give error because of the double quotes inside the string.
txt = "We are the so-called \"Vikings\" from the north." #-----> this will work because we have used single quotes to define the string.
print(txt)'''

#Escape Characters
#Other escape characters used in Python:

#Code	Result	
#\'	    Single Quote	-----> txt = 'It\'s alright.'  -----> It's alright.
#\\	    Backslash		-----> txt = "This will insert one \\ (backslash)."-----> This will insert one \ (backslash).
#\n	    New Line		----->txt = "Hello\nWorld!"----->Hello
#                                                         World!
#\r	    Carriage Return	----->txt = "Hello\rWorld!"----->World!
#\t	    Tab	      	    ----->txt = "Hello\tWorld!" -----> Hello	World!
#\b	    Backspace		----->txt = "Hello \bWorld!"-----> HelloWorld!
#\f	    Form Feed		----->

#\ooo	Octal value		----->#A backslash followed by three integers will result in a octal value:
#txt = "\110\145\154\154\157"-----> Hello

#\xhh	Hex value    	----->A backslash followed by an 'x' and a hex number represents a hex value:
#txt = "\x48\x65\x6c\x6c\x6f" ----->Hello

#Boolean values with strings:
'''x = "Hello"
y = 15

print(bool(x))
print(bool(y))'''
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
'''#The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) 

#The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

#Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #Returns False because the __len__ function returns 0

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

#Example
#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))



#ex 1: remove parathesis 
def remove_outer_parentheses(s):
    result = []
    depth = 0

    for ch in s:
        if ch == '(':
            if depth > 0:
                result.append(ch)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(ch)

    return ''.join(result)'''

#Greatest English Letter in Upper and Lower Case

from collections import Counter


def find(s):
    c = Counter(s)
  
    big = max(ord(c.keys())) 
    for ch in c: 
        if big.isupper() and big.lower() in c:
            return chr(big)
        c.pop(max(c.item()))
        return(find(s))
    return ""

res = find("nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM")
print(res)

        
        
       