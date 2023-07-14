# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

list1=[]
for i in range (0,30):
    list1.append(i**2)
print(list1)
print(list1[0:5])
print(list1[-5:])