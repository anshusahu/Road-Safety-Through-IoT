import smtplib

content = 'Sent from python'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login(sender_email,Password)

mail.sendmail(sender_email,receiver_email,content)

mail.close()

