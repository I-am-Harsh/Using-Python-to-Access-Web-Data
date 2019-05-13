import urllib.request, urllib.response, urllib.error
import xml.etree.ElementTree as ET


url = input("Enter the URL - ")
sum = 0

html = urllib.request.urlopen(url).read()

tree = ET.fromstring(html)

count_list = tree.findall("comments/comment/count")

for value in count_list:
    # count = value.find('count')
    sum = sum + int(value.text)
print(sum)
