# Write a Python function that takes a list and returns a new list with unique elements of the first list.
 
def unique_list(numbers):
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
    return unique

print(unique_list([1, 2, 3, 1, 2]))
