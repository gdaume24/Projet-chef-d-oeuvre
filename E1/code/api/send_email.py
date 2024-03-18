import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    # Création de l'e-mail
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Corps du message
    message.attach(MIMEText(body, 'plain'))

    # Connexion au serveur SMTP et envoi de l'e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    # Configurations SMTP
    smtp_server = 'smtp.example.com'  # Adresse du serveur SMTP
    smtp_port = 587  # Port SMTP
    smtp_username = 'your_smtp_username'  # Nom d'utilisateur SMTP
    smtp_password = 'your_smtp_password'  # Mot de passe SMTP

    # Informations de l'e-mail
    sender_email = 'geoffroy.daumer@outlook.com'  # Adresse e-mail de l'expéditeur
    receiver_email = 'kirbycath61'  # Adresse e-mail du destinataire
    subject = 'Sujet de l\'e-mail'  # Sujet de l'e-mail
    body = 'Contenu du message.'  # Corps de l'e-mail

    # Envoi de l'e-mail
    send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)