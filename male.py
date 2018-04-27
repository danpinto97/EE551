# import time
# import datetime
# print(time.time(), time.clock())
# time.sleep(1)
# print(time.time(), time.clock())
#
# now = datetime.datetime.now()
#
# print "Current day: " , now.day
import smtplib
import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'lov3rboi77@gmail.com'
password = 'purpleandred'
sender = 'jmeiskin@stevens.edu'
targets = ['dpinto@stevens.edu']
#msg = MIMEText('bicth pleas money me') #this is the body
msg = MIMEMultipart()
msg.attach(MIMEText(file("Unofficial Transcript.pdf").read()))
msg['Subject'] = 'Here\'s a PDF!'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
