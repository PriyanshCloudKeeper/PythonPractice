# Create a app password in gmail, Account - Security - 2 Factor - App Password

# Email Formating Library and Connection Library

# SMTP module

import smtplib
from email.message import EmailMessage
msg = EmailMessage()

# Connection Estalish

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("priyansh.choudhary@cloudkeeper.com", "wief lzcs tpya odss")

# msg object set

msg['From'] = "priyansh.choudhary@cloudkeeper.com"
msg["To"] = "priyanshjproff@gmail.com"
msg["Subject"] = "Automated Email By Yours Truly"

body = "Hello, This is a test email"
msg.set_content(body)

# send the created message with SMTP server
server.send_message(msg)
server.quit()

# delete passwd




