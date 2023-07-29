# Write a Python program to find the repeated items of a tuple.

tuple1 = (10,20,30,30,40,50,60,20,80,40,50,90,10,20,30)
list1 = []
for i in tuple1 :
    # tuple1.count(i)
    if tuple1.count(i) > 1 :
        list1.append(i)
    set1 = set(list1)
print("Repeted Items in Tuple : ",set1)