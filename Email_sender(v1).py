import smtplib 
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "adel tafaghodi"
email['to'] = "destination Email"
email['subject'] = "you log in"

email.set_content('im programmer')

with smtplib.SMTP(host = 'smtp.gmail.com' , port = 587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login("main email address" , "password")#Email's adel(from)
    smtp.send_message(email)
    print("Done")
