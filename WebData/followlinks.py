from urllib.request import urlopen
import ssl
from bs4 import *

url = input('Enter URL : ')
position = input('Enter position : ')
count = input('Enter count : ')

page = urlopen(url)
data = page.read()
soup = BeautifulSoup(data)

# Retrieve all of the anchor tags
tags = soup('a')

#Create an empty list
links = list()

for tag in tags:
    links.append(tag.get('href', None))

print('Retrieving: ', links[0])
print('Retrieving: ', links[int(position)-1])

link = links[int(position)-1]
counter = 1
while counter < int(count):
    page = urlopen(link)
    data = page.read()
    soup = BeautifulSoup(data)

    # Retrieve all of the anchor tags
    tags = soup('a')

    links = list()

    for tag in tags:
        links.append(tag.get('href', None))
    print('Retrieving: ', links[int(position)-1])
    link = links[int(position)-1]
    counter = counter + 1