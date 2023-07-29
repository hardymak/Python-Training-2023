# Write a Python program to combine two dictionary adding values for common keys. Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
combine_dic = {}


for key in d2.keys() :
    if key in d1:
        combine_dic[key] = d1[key]+d2[key]
    else :
        combine_dic[key] = d2[key]

for key in d1.keys() :
    if key in d2:
        combine_dic[key] = d1[key]

print(combine_dic)