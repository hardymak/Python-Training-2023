# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

a = int(input("Enter first value :"))
b = int(input("Enter second value :"))
c = int(input("Enter third value :"))

if a == b or b == c or c == a:
    print("sum is :", 0)
else:
    print("Sum is :",a+b+c)    