import smtplib

smtp_smtp = "smtp.googlemail.com"
port = 587  # For starttls
sender_email = "db.backup911@gmail.com"
password = "uepkckkrrjwyxlob"

with smtplib.SMTP(smtp_smtp,port) as smtp:
    smtp.ehlo()
    smtp.starttls() # Secure the connection
    smtp.ehlo()

    smtp.login(sender_email, password)

    subject = 'Sample Subject'
    body = 'Sample Body'

    msg = 'Subject: {}\n\n{}'.format(subject, body)

    smtp.sendmail(sender_email, "pavanbaddi911@gmail.com", msg)
    

