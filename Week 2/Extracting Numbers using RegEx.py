import re

#Create the file numbers.txt or anything you like and replace it
#The file is already included in the repo
#However your file may be different 

file = open("numbers.txt")

text = file.read()

number_final = re.findall('[0-9]+',text)

total = 0
for i in number_final:
    i = int(i)
    total = total + i;

print(total)

file.close()
