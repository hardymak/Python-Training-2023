# Write python program that swap two number with temp variable and without temp variable. 
# Without using third variable

a = 12
b = 13

a,b = b,a

print("the value of a is",a)
print("the value of b is",b)



# with using temp variable

a = 13
b = 12

temp = a

a = b
print("The value of x is",a)

b = temp
print("The value of y is ",b)