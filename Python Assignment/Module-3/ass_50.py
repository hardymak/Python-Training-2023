# Write a Python function to check whether a number is in a given range
def checkinrange():
    if num1 in range(1,100):
        print("Enter Number is in Range.")
    else:
        print("Enter Number is not in Range.")


num1 = int(input("Enter Number : "))
checkinrange()