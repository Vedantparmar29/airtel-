import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime

people = [
    {
        "name": "vedant",
        "email": "vsbharat18@gmail.com",
        "birthday": "07-11",
        "anniversary": "08-15",
        "photo": "bday1.png"
    },
    {
        "name": "rajdeep",
        "email": "vs9156195@gmail.com",
        "birthday": "11-23",
        "anniversary": "07-11",
        "photo": "anniversary1.png"
    }
]
sender_email = "vs7351525@gmail.com"
password = "yjiy jhdy erps audg"




today = datetime.now().strftime("%m-%d")


for person in people:
    event = None
    if person["birthday"] == today:
        event = "Birthday"
    elif person["anniversary"] == today:
        event = "Anniversary"
    
    if event:
        try:
            
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = person['email']
            msg['Subject'] = f"Happy {event}, {person['name']}!"

            
            body = f"Dear {person['name']},\n\nWishing you a very happy {event}!\n\nBest regards,\nYour Team"
            msg.attach(MIMEText(body, 'plain'))

            
            with open(person["photo"], "rb") as img:
                image = MIMEImage(img.read())
                image.add_header('Content-Disposition', 'attachment', filename=person["photo"])
                msg.attach(image)

            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
                print(f"{event} email sent to {person['name']} at {person['email']}")

        except Exception as e:
            print(f"Failed to send email to {person['name']}: {e}")
