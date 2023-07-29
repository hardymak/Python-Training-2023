# Write a Python program to split a list into different variables.


my_list = ["a", "b", "c"]

for i in my_list :
    for j in range(len(my_list)) :
        print(f"var", j , " = " , i ) 
