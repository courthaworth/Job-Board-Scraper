#scrape
#look for data, MAchine learning, " ML "
#Send email

from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


keywordlist = ["data", "machine learnning", " ml "]

url = 'https://news.ycombinator.com/jobs'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
urldict = {}



for link in soup.find_all('a'):
	#print(link.find(text=True))
	body = str(link.find(text=True))
	if(any(substring in body.lower() for substring in keywordlist)):
		print(body)
		if(link.get("href").startswith("item")):
			urldict[body] = "https://news.ycombinator.com/{}".format(link.get("href"))
		else: 
			urldict[body] = link.get("href")


print(urldict)

hostaddress = input("Input Your Host address:")
portnumber = int(input("Input your port:"))

s = smtplib.SMTP(host=hostaddress, port=portnumber)
#s = smtplib.SMTP('localhost')
s.starttls()
MY_ADDRESS = input("Input Email address that will send email:")
PASSWORD = input("Input Password to said account: ")

s.login(MY_ADDRESS, PASSWORD)

msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
msg['From']=MY_ADDRESS
msg['To']=MY_ADDRESS
msg['Subject']="Job Postings"

# add in the message body
for body, url in urldict.items():
	text = "\n{}:\n{}".format(body,url)
	msg.attach(MIMEText(text, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)
    
del msg