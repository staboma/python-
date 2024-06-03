import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # Gmail için güvenli bağlantı portu
sender_email = "kullanici_adiniz@gmail.com"
sender_password = "sifre_niz"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = "alici_email@gmail.com"
message["Subject"] = "Konu"

email_content = """
E-posta içeriğinizi buraya yazın.

Saygılarımla,

Gönderen Adı
"""

message_body = MIMEText(email_content, "plain")
message.attach(message_body)

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # TLS ile güvenli bağlantı kur
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, message["To"], message.as_string())