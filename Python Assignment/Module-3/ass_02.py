"""

# How will you remove last object from a list? 
    
    -> using pop we can remove last element of the list and we can pop(index) specific index value

# what is list1 [-1]?

    ->  here list1[-1] indicate last position element of list
    
    ->  list1 =[ 2, 33, 222, 14, 25 ]
        print(list1[-1])
            o/p = 25
    
"""
l1= [10,20,30,40,50]
l2= ["python", "java", "php","android"]
 
l1.pop()    # remove last element(50) from the list 
print(l1)

l2.pop()    # remove last element(android) from the list = "android"
print(l2)

list1 =[ 2, 33, 222, 14, 25 ]
print(list1[-1])    # last element(25) of list
