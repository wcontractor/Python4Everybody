import urllib
import json
import requests

url = raw_input("Enter location:")
file = requests.get(url)


data = file.json()
comments = data["comments"]


sum = 0
for item in comments:
	sum = sum + int(item['count'])
print sum


