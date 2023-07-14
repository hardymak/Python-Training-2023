# Write a Python program to select an item randomly from a list.

import random

list1=[]
n= int(input("Enter How Many Items Want to add in List :"))

for i in range(0,n):
    list1.append(input("Enter Item Name :"))

print(list1) # print list which was created by taking user input.
print(type(list1)) # print class of variable. 

print(random.choice(list1)) # print an item randomly from a list.