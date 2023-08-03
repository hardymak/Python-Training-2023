# Write a Python program to read first n lines of a file.

Line= int(input("Enter Number of line want to read : "))
file = open("Newfile.txt","r")
for i in range(Line):
    print(file.readline())
    
file.close()