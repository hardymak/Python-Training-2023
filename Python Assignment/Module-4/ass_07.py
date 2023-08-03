# Write a Python program to read a file line by line store it into a variable.

with open ("NewFile.txt","r") as f :
        lines = f.readlines()
        print(lines)
        print(type(lines))