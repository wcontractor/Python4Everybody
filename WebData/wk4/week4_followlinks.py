from urllib.request import urlopen
from bs4 import *

#Get user inputs
url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position :'))



#Create an empty list to store the names in
links = []

# Retrieve all of the anchor tags
#tags = soup('a')
while count > 0:
    html = urlopen(url)
    soup = BeautifulSoup(html)
    
    tags = soup('a')
    
    for tag in tags:
    	links.append(tag.get('href', None))
    	count = count -1
print('Retreieving: ------------ ', links)
		