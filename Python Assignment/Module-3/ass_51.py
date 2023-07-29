# Write a Python function to check whether a number is perfect or not.

def perfect():
    global sum
    if num1 > 0 :
        for i in range(1,num1):
            if num1 % i == 0:
                sum += i
    return sum    
    # if sum == num1 :
    #     print("Entered Number is Perfect Number.")
    # else:
    #     print("Entered Number is not Perfect Number.")

sum = 0
num1 = int(input("Enter Number : "))
perfect()
if sum == num1 :
    print("Entered Number is Perfect Number.")
else:
    print("Entered Number is not Perfect Number.")