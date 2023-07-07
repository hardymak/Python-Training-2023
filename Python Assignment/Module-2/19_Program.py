# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string ength is less than 2, return instead of the empty string. 

def strings_from_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
print(strings_from_ends("Elephant"))
print(strings_from_ends("or"))
print(strings_from_ends("E"))