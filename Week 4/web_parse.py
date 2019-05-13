from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

#Insert the URL when prompted in terminal window

#This code will serve as the answer for both the programming assignment.

url = input("Enter URL - ")

############################################### Comment this for first question ##############################
pos = int(input("Enter the position - ")) - 1
count = int(input("Enter the count - "))
count1 = 0
while(count1 < count):

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[pos].get('href')
    name = tags[pos].contents[0]
    count1 = count1 + 1

print(name)

##################################################################






################################################ Comment this for second question ############################################### 

tags = soup('span')
sum = 0
for value in tags:
    temp = int(value.contents[0])
    sum = sum + temp
print(sum)

##############################################################################################