# Write a Python program to convert a list of characters into a string.

list1=[]
str1 = ""
status = True
while status:

    a=input("Enter Item :")
    check = input("Want to addd More Item (y/n): ").upper()
    list1.append(a)
    if check == "Y" :
        status = True
    else :
        status = False

print(list1)
print(type(list1))

for i in list1:
    str1 += i
print(str1)