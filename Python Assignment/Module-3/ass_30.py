# Write a Python program to convert a list of tuples into a dictionary.

tuple1= (("a",1),("b",2),("c",3),("d",4),("e",5),("f",6),("g",7),("h",8),("i",9),)
dic1 = {}

for i in tuple1:
    key = i[0]
    value = i[1]
    dic1[key] = value

print(dic1)