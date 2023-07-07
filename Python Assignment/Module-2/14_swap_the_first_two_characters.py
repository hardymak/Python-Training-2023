v2, v1 = "abcd", "rstu"

temp = v2
v2=v1[0:2] + v2[2:]
v1= temp [0:2] + v1[2:]
print(v2+' '+v1)