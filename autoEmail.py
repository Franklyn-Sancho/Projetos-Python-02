import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = '<HOST_URL>'
port = 587
user = '<USUARIO>'
password = '<SENHA>'

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(user, password)

message = "Olá, mundo!"
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = '<EMAIL_DE_DESTINO>'
email_msg['Subject'] = 'Assunto da mensagem'
email_msg.attach(MIMEText(message, 'plain'))

server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
