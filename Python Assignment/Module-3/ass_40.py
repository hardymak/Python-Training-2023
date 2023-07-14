# Write a Python program to map two lists into a dictionary 

items = ['pen', 'paper', 'pencil']
quantities = [5, 20, 15]
items_dict = {key:value for key, value in zip(items, quantities)}

print(items_dict)