import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from email.utils import make_msgid


def send_mail(recipients, body, msg_subject):
    load_dotenv()
    smtp_server = os.getenv('SMTP_SERVER')
    email_pass = os.getenv('EMAIL_PASS')
    sender_mail = os.getenv('SENDER_MAIL')
    ##---------------------------Message------------------------------##

    for recipient_email, recipient_name in recipients:
        msg = EmailMessage()
        msg['Subject'] = msg_subject
        msg['From'] = sender_mail
        msg['To'] = recipient_email
        msg.set_content('This is plain text')

        logo_cid = make_msgid()
        msg.add_alternative(f"""
                <html>
                        <body>            
                        <p>Laba diena, <strong>{recipient_name}</strong>!</p>

                        <p>{body}</p>

                        <p>Pagarbiai,</p>
                        <p>NAME SURENAME</p>
                        <p>Telefonas: +37000000000</p>
                        <p>El. paštas: info@example.com</p> 
                        <img style="width: 200px" src="cid:{logo_cid}"/>           
                    </body>
                </html>
                """, subtype='html')

        with open("Logo.jpg", "rb") as img:
            msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                             cid=logo_cid)

        ##--------------------------------Attachment photo----------------------##
        # files = ['tomas.jpg', 'kitas.jpeg']
        # for file in files:
        #     with open(file, 'rb') as f:
        #         file_data = f.read()
        #         file_type = imghdr.what(f.name)
        #         file_name = f.name
        #     msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

        ##----------------------Sending mail----------------------------##
        with smtplib.SMTP_SSL(smtp_server, 465) as connection:
            connection.login(user=sender_mail, password=email_pass)
            connection.send_message(msg=msg)
