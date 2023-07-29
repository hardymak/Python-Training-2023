# Write a Python program to get unique values from a list

list1=[]
n= int(input("Enter How Many Items Want to add in List :"))

for i in range(0,n):
    list1.append(input("Enter Item Name :"))

print(list1) # print list which was created by taking user input.

set1= set(list1)
print("unique values from a list : ",set1)