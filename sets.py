#SET is a collection of unordered items. just like in maths, each element lies here only once and no repetion is allowed!(it will exclude repeated values!)
#lists and dictionaries cannot be stored in sets cause they are mutable (changable)
#Syntax: variable_name = {value}
#Sets are mutable but it's elements are immutable
Collection = {"JJK", "BSD", "Assasination classroom"}
print(Collection)
#To create an empty set:
Empty = set()
print(type(Empty))
''' Methods in sets: 
    set_name.add( value to add ) ---> It could be anything tupples, strings, etc.
    set_name.remove( value to remove ) 
    set_name.clear( value ) ---> empties the set 
    set_name.pop() -----> Pick a random value from the set
    set.union(set2)
    set.intersection(set2)'''
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

Class = { "Python","Java","C++","Python","Javascipt","Java","Python","Java","C++","C"}
print(len(Class))