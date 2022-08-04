#!/usr/bin/env python
# coding: utf-8

import csv
import time
import datetime

todate = datetime.date.today()
tmdate = datetime.date.today() + datetime.timedelta(days=1)


def congratulator(person,annive,dayf):
    """ Generate a congratulation message for each person
    """
    if dayf == True:
	todmorr = "tomorrow"
    else:
	todmorr = "today"
    if annive == True:
	congr = " %s has an anniversary %s!"% (person, todmorr)
    else:	
        congr = " %s has a birthday %s!"%  (person, todmorr)
    return congr
    #mailer(mess)
def formater():
    pass
    
def mailer(message):
    """ Send reminder msg for all
    """
    import smtplib
    from email.MIMEText import MIMEText

    sender = "informer@example.com"
    recip = ["mail1@example.com", "mail2@example.com"]
    text = message
    subj = "Birthday reminder"

    #SMTP-server
    server = "mail.example.com"
    port = 25
    user_name = "informer@example.com"

    #Formating message
    msg = MIMEText(text, 'plain', "utf-8")
    msg['Subject'] = subj
    msg['From'] = sender
    msg['To'] = ",".join(recip)

    #Send mail
    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.ehlo()
    s.sendmail(sender, recip, msg.as_string())
    s.quit()


table = []

#reading DOB.CSV and add in table rows
infile = open('DOB.csv', 'r')
for row in csv.reader(infile):
    table.append(row)
infile.close()


#Compare DOB with actual date
mess =""
for r in range(1,len(table)):
	dob1 = time.strptime(table[r][1], "%d.%m.%Y")
	dob = datetime.datetime.fromtimestamp(time.mktime(dob1))
	if (dob.day == todate.day and dob.month == todate.month) or (dob.day == tmdate.day and dob.month == tmdate.month):
	    if dob.day == todate.day:
		dayf = 0
	    else:
		dayf = 1 
		    # check for  anniversary
	    if (todate.year-dob.year)%5 == 0:
			annive =1
   	    else:
			annive = 0
	    mess += congratulator(table[r][0], annive, dayf) + "\n"

if mess != "" :
    mailer(mess)
