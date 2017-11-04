
#!/Users/courthaworth/anaconda3/bin/python
from bs4 import BeautifulSoup
import sys
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Keywords to look for
keywordlist = ["data", "machine learnning", " ml "]

#Websites to pull postings from
sitelist = ['https://news.ycombinator.com/jobs','https://icrunchdata.com/','https://jobs.dataelixir.com/','https://www.kaggle.com/jobs','https://stackoverflow.com/jobs']

urldict = {}

for url in sitelist:
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'lxml')
	#print(soup.prettify())
	for link in soup.find_all('a'):
		#print(link.find(text=True))
		body = str(link.find(text=True))
		if(any(substring in body.lower() for substring in keywordlist)):
			print(body)
			if(link.get("href").startswith("item")):
				urldict[body] = "https://news.ycombinator.com/{}".format(link.get("href"))
			else: 
				urldict[body] = link.get("href")



#print(urldict)

if(len(sys.argv)>2):
	hostaddress = sys.argv[1]
	portnumber = int(sys.argv[2])
	MY_ADDRESS = sys.argv[3]
	PASSWORD = sys.argv[4]
	emailtxt = sys.argv[5]

else:	
	hostaddress = input("Input Your Host address:")
	portnumber = int(input("Input your port:"))
	MY_ADDRESS = input("Input Email address that will send email:")
	PASSWORD = input("Input Password to said account: ")
	emailtxt = None

s = smtplib.SMTP(host=hostaddress, port=portnumber)
print("connected")
#s = smtplib.SMTP('localhost')
s.starttls()


s.login(MY_ADDRESS, PASSWORD)

emaillist = []
if(emailtxt is None):
	emaillist.append(MY_ADDRESS)
else:
	with open(emailtxt,"r") as file:
		for line in file:
			emaillist.append(line)

msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
msg['From']=MY_ADDRESS
msg['Subject']="Job Postings"

# add in the message body
for body, url in urldict.items():
	text = "\n{}:\n{}\n".format(body,url)
	msg.attach(MIMEText(text, 'plain'))

for address in emaillist:
	address = address.strip()
	print(address)
	msg['To']=address
	s.send_message(msg)
    
del msg