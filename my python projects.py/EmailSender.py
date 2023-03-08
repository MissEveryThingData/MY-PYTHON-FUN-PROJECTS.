from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'relebogile08lebogang@gmail.com'
email_password = 'dvowlvyoomtqtfpm'

email_receiver = 'pomabo4619@crtsec.com'

subject = "do nt forget to subscribe"
body = """please subcribe ,while you enjoy the video"""

em = EmailMessage()
em['from']= email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
  smtp .login(email_sender,email_password)
  smtp.sendmail(email_sender,email_receiver,em.as_string())


