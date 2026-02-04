'''Syntax for open:
    #open: f =open("file_name","mode")
    # data = f.read() ---> reads entire file
    # data = f.readline()--> reads one line at a time

    #write: f = open("file_name","mode")
            f.write("anything here!")

    
    #'r' = open for reading(default) 
    #'w' = open for writing, truncating the file first
    #'x' = create a new file and open it for writing
    #'a' = open for writing, appending to the end of the file if it exists 
    #'b' = binary mode
    #'t' = text mode(default)
    #'+' = open a disk file for updating(reading and writing)
    
    #'r+' = read and append (no truncate)
    #'w+' = read and write (but the whole data will first vanish and then the new data will be written!)-->truncate
    #'a+' = read + append (no truncate)
    
    if you don't have any file of that name and you open it in write or append mode then python will automatically create that file for you!'''
#f = open("demo.txt","w+")
#data = f.read()
#f.write("Here I Go!!")
#print(data)
#f.close()

#when with syntax is used in python it will automatically close the file
'''with open("demo.txt","r") as f:
    data = f.read()
    print(data)
with open("demo.txt","w") as f:
    f.write("Don't be afraid!")'''#----> will read the old file but truncates it and write our data

'''import os #--->module in python for deleting 
os.remove()'''
#count the total no. of even numbers in my file.
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    num = data.split(",")
    for val in num:
        if (int(val)%2==0):
            count += 1
        
print(count)
f.close()

   