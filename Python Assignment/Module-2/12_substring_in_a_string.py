# Write a Python program to count occurrences of a substring in a string    

my_string = input("Enter a string :")
my_substring = input("Enter a Substring :")

my_count = my_string.count(my_substring)

print("Substring occurs %d times " % my_count)