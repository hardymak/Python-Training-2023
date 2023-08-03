# Write a Python program to write a list to a file.

sub = ['Python', 'Java', 'React Js', 'Node Js', 'Andriod', 'Html']
with open("NewFile.txt", "a") as myfile:
        for i in sub:
                myfile.write("\n"+i)

content = open("NewFile.txt")
print(content.read())