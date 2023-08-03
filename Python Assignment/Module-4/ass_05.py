# Write a Python program to read Last n lines of a file.

import linecache
fname = "NewFile.txt"
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)


n = int(input("Enter Last n lines TO Read : "))
for i in range(num_lines,num_lines-n,-1):
	print(linecache.getline("NewFile.txt",i),end="")