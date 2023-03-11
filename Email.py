import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(html_file_path, recipient_email):
    # Öffnen Sie die HTML-Datei und lesen Sie ihren Inhalt
    sender_email = "dkspider21@gmail.com"
    sender_password ="#Knospe2020$"
    smtp_server ="smtp.gmail.com"
    smtp_port ="465"
    with open(html_file_path, "r") as f:
        html_content = f.read()

    # Erstellen Sie die E-Mail-Nachricht
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = 'HTML-Datei als E-Mail-Anhang'

    # Fügen Sie den HTML-Inhalt als MIME-Typ "text/html" hinzu
    message.attach(MIMEText(html_content, 'html'))

    # Fügen Sie die HTML-Datei als Anhang hinzu
    with open(html_file_path, 'rb') as f:
        attach = MIMEApplication(f.read(),_subtype="html")
        attach.add_header('Content-Disposition','attachment',filename=str(html_file_path))
        message.attach(attach)

    # Verbinden Sie sich mit dem E-Mail-Server und senden Sie die E-Mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
send_email("Vanessa_Export.html", "dkspider@t-online.de")