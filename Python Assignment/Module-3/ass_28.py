# Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = (10,20,30,30,40,"",60,20,"",40,50,90,10,20,30)
print(len(tuple1))
tuple1 = filter("",tuple1)
print(tuple1)