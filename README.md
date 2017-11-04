# Job Board Scraper

This project will be a web scraper that searches a number of job boards including YCombinator's Hacker News in order to find new job postings relevant to data science. The scraper will look for post titles that contain key words like Data, Machine Learning or ML. Once these postings are collected, the script will send an email to your email address containing hyperlinks to those postings.


You will need to input outgoing mail host(ex. smtpauth.earthlink.net) corresponding to the email you wish to use to send the email. You will also need to choose the port number (common port numbers are 25, 465, and 587). After inputting these, you will be asked to input the corresponding email address and password. I am planning on adding the functionality to enter all four of these things as command line arguments so that this script can be automated to run every 24 hours or in a similar manner.
