# Syntax:  "key" : "value"
#it is mutable and no we cannot have two keys with same name
#Unordered
'''dict = {
       "name" : "Manaswi",
       "cgpa" : 9.6,
       "marks": [98, 97, 95] ,
       "topics": ("dict", "set"),
       9.8 : 4.9
       }
print(dict)
info = {
    "key": "value",
    "name": "Me",
    "learning": "Coding",
#we cannot add another set or dictionary inside a dictionary
}
print(type(info))
print(info["name"]) #to access the value of the key written in the dictonary
print(info)
info["name"] = "Manaswi" #changing a value of a key 
info["surname"] = "Sorde" #Adding a new key : value pair
print(info["name"])
print(info)
#We can create a null dict : null_dict {}'''

#Nested dictionaries
Anime = {
    "No. of Anime watched" : 100,
    "Shippings" : {

        "Sherlock" : "William",
        "Gojo" : "Geto",
        "Sukuna" : "Megumi",
        "Ash" : "Misty"
    }
}
#print(Anime)
#print(Anime["Shippings"]["Sherlock"]) #value extracted from nested dictionaries 
#dictionary methods:
'''dictname.keys()
    dictname.values()
    dictname.items()
    dictname.get()
    dictname.update()

print(Anime.keys()) #dictnname.keys() = gives/returns me all the keys of my dictionary
print(list(Anime.keys())) #Typecasting dict ----> list
print(Anime.values()) #dictname.values() gives me  all the values of my dictonary
print(Anime.items()) #it returns values into key-value pair in a form of tupples 
print(Anime.get("Shippings")) #returns the key- if not correct returns 'None' ----> methodical way
Country = { "Country" : "Japan" }
Anime.update(Country) #When adding a new key-value pair: format =  ({"Country" : "Japan"}) make sure to add curly braces while updating a new dictionary in the old one do not use curly braces!'''
'''print(Anime)

Word_meanings = {
    "Table" : "A piece of furniture , list of facts and figures",
    
    "Cat" : "A small animal"
}
print(Word_meanings)

# The dictionary of words and their meanings
word_meanings = {
    "apple": "a fruit",
    "book": "a written or printed work",
    "car": "a motor vehicle with four wheels",
    "dog": "a domesticated mammal"
}

# Your code here
def find_meaning(word):
    if word in word_meanings.keys():
        return True
    else:
        return False
# Don't change below this line
print("Does 'book' exist in the dictionary?", find_meaning("book"))
print("Does 'cat' exist in the dictionary?", find_meaning("cat"))
print("Does 'dog' exist in the dictionary?", find_meaning("dog"))

def add_book(catalog, title, author, year):
    new1 = add_book["catalog" : f"{catalog}"]
    new2 = add_book["title" : f"{title}"]
    new3 = add_book["author" : f"{author}"]
    new4 = add_book["year" : f"{year}"]
    add_book.update(new1)
    add_book.update(new2)
    add_book.update(new3)
    add_book.update(new4)
    if title in add_book:
        return True
    
var = add_book(catalog={},  author="George Orwell", title = 1984, year = 1949 )'''

''' #It is also possible to use the dict() constructor to make a dictionary.

#Example
#Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)'''


# find the operator:
def equation(a,b,c):
    ops = {
        "+": a+b,
        "-": a-b,
        "*": a*b,
        "/": int(a/b) if b!=0 else None
    }
    for op, value in ops.items():
        if value == c:
            return f"{a}{op}{b}={c}" 
        
print(equation(10,5,15))