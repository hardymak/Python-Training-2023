# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
str1 = ["abc","xyz","aba","121","hello","aba"]
count=0
for i in str1:

    if len(i) >= 2 and  i[0] == i[-1] :
        count+=1
print ("No. of String : ",count)