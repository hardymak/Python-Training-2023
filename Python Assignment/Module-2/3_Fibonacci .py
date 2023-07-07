# Write a Python program to get the Fibonacci series of given range. 
a = 0
b = 1
num = int(input("Enter a number to obtain fibbonacci sequence:-"))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range (2,num ):
        c = a+b
        a = b
        b = c
        print(c)    

