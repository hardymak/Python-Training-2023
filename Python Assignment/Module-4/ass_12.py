# Write a Python program to copy the contents of a file to another file.

with open("NewFile.txt","r") as file1:
    a=file1.read()

with open("NewFile2.txt","a") as file2:
    file2.write(a)