#scrape
#look for data, MAchine learning, " ML "
#Send email

from bs4 import BeautifulSoup
import requests


url = 'https://news.ycombinator.com/jobs'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
urllist = []
keywordlist = ["data", "machine learnning", " ml "]
for link in soup.find_all('a'):
	#print(link.find(text=True))
	body = str(link.find(text=True))
	if(any(substring in body.lower() for substring in keywordlist)):
		print(body)
		urllist.append("https://news.ycombinator.com/{}".format(link.get("href")))


print(urllist)