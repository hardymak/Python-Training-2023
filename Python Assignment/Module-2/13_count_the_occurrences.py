def count (str):
    
    dict = {}
    w = str.split()
    
    for i in w:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
para = input("enter a paragraph:")

print(count(para))
            