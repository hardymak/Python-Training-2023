# Write a Python program to count the number of characters (character frequency) in a string 

my_string = input("Enter a string: ")
count = {}

for letter in my_string:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print("Count Frequency is....")
for key, value in count.items():
    print(f"{key} occurs {value} times")        
            