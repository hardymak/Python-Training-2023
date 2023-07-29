# Write a Python program to replace last value of tuples in a list.

tuple1= (10,20,30,40,50,60,90)
print(tuple1)
print(type(tuple1))

list1= list(tuple1)
list1.pop()

a=input("Enter New Item for Last Position of tuple : ")
list1.append(a)

tuple2= tuple(list1)
print(tuple2)
print(type(tuple2))