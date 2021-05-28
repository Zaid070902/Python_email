import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address = 'zaidflandorp4@gmail.com'
receiver_address = ['aaliyahjar13@gmail.com', 'gafrica851', 'dallascas0siem704@gmail.com', 'thapelo@lifechoices.co.za']
password = input("Enter password: ")
subject = "Hello world"
message = MIMEMultipart()
message['From'] = address
message['To'] = ','.join(receiver_address)
message['Subject'] = subject
body = "Sup?"
message.attach(MIMEText(body, 'plain'))
text = message.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(address, password)

s.sendmail(address, receiver_address, text)
s.quit()
