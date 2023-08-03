# Write a Python program to append text to a file and display the text.

file = open("NewFile.txt","a")

for i in range(0,5):
    name = input("\nEnter Name : ").upper()
    score = int(input("\nEnter Marks : "))
    file.write("\nName : "+name+"\t")
    file.write("Score : "+str(score))
file.close()

file = open("NewFile.txt","r")
print(file.read())
file.close()