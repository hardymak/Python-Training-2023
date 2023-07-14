# Write a Python script to concatenate following dictionaries to create a new one.

dic = {}

dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}

dic.update(dic1)
dic.update(dic2)

print(dic)