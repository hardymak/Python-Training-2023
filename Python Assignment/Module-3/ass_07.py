# Write a Python program to remove duplicates from a list.

#  remove duplicate values from list or find unique value from list using set
    
l1 = [10,20,30,40,20,50,30,60]
s= set(l1)  # convert in to set
print(s)

# remove duplicate values from list or find unique value from list without using set

unique_list = []
l1 = [10,20,30,40,20,50,30,60]
for i in l1:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)