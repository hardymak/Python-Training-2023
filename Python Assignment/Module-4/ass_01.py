"""
#  What is File function in python?

=> A file function allows us to use, access and manipulate all the user accessible files. One can read and write any such files.

#  What is keywords to create and write file.

=> f = open("demofile.txt", "a")

=> A file can be opened with a built-in function called open(). 
   This function takes two parameters; filename and mode
"""
f = open("NewFile.txt","w")
para = [10,20,30,40,50,60]
a= str(para)

f.write(a)
f.close()