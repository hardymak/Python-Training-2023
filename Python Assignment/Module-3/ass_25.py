# Write a Python program to reverse a tuple.

tuple1= (10,20,30,40,50,60,70,80,90)
print(tuple1)
list1 = list(tuple1)

list1.reverse()

list1=tuple(list1)
print(type(list1))
print(list1)