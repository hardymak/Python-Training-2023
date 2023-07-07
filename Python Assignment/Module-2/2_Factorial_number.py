# Write a Python program to get the Factorial number of given number. 
num = int(input("enter a number here:"))
 
fact = 1
  
if num > 0:
    for i in range (1, num+1):
        fact = fact * i
print("the factorial of the given number is", fact)              
 