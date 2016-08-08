from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_283039.html'
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")

span_tags = soup('span')

sum = 0
for span in span_tags:
	number = float(span.string)
	sum = number + sum
print(sum)
