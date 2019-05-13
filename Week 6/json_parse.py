import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter the URL - ")

data = urllib.request.urlopen(url).read()

json_data = json.loads(data)


sum = 0
for user in json_data['comments']:
    sum = sum + int(user['count'])
print(sum)