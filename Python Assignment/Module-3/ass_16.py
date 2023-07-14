# Write a Python program to check whether a list contains a sub list

main_list = ["a","b","c"]

sub_list = ["c"]

for i in main_list:
    for j in sub_list:
        if i == j :
            print("sub_list is in main_list")
            break

print("sub_list is not in main_list")

        