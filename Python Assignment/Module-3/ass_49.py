# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial():
    factorial = 1

    if num > 0:
        for i in range ( 1, num + 1):
            factorial = factorial * i
        print(factorial)
    elif num < 0:
        print("factorial does not for negative numbers")
    else:
        print("The factorial of 0 is 1")


num = int(input("Enter Number You Wnat to Find Factorial : "))

factorial()