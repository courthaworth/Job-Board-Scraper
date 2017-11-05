# Job Board Scraper

This project is a web scraper that searches a number of job boards including YCombinator's Hacker News, icrunchdata.com, and Kaggle in order to find new job postings relevant to data science. The scraper will look for post titles that contain key words like Data, Machine Learning or ML. Once these postings are collected, the script will send an email to your email address containing hyperlinks to those postings. It would be easy to change the keywords that are being searched, just edit the list variable "keyword list" near the beginning of the file.


When running this script, you will need to input outgoing mail host(ex. smtpauth.earthlink.net) corresponding to the email you wish to use to send the email. You will also need to choose the port number (common port numbers are 25, 465, and 587). After inputting these, you will be asked to input the corresponding email address and password. By default this script will send the email from the address to itself. 

The functionality to use command line arguments has been implemented. Running this file in the command line, followed by your hostname, port, email address, password then you wont have to input them as the file is running. This is useful if you are always going to be using the same information when you run it, or you wish to automate the process using launchd, or similar functionality. There is an optional fifth emailaddress txt file list if you wish to send the email to multiple addresses. The desired format for such a file is just one email address per line:

example@gmail.com
example2@gmail.com


etc.

Most of these job boards do not update every day so there will be substantial repetition. I have set this up on my computer to run every 24 hours automatically but this can be configured however. On a mac, it is easy to set up this functionality using launchd, and launch control if you need help debugging. When I have time I will likely post a tutorial on this automation.
