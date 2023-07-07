str='The lyrics is not that poor'
pos_not = str.find("not")
pos_poor = str.find("poor")

if pos_not < pos_poor:
    print(str[:pos_not]+"good")