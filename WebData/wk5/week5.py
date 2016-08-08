from urllib.request import urlopen
import xml.etree.ElementTree as ET

#sample url = 'http://python-data.dr-chuck.net/comments_42.xml'


address = input('Enter location: ')
url = urlopen(address)
data = url.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')

sum = 0

print("Retrieving", url)

for item in counts:
	#print('Count', item.get('count'))
	sum = sum + int(item.text)
	#print(item.get(item.text))

print(sum)








