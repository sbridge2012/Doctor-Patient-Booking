import sys
import datetime

import GUI as G


def send_appts(email_address, appointments):

    email = 'sbridge11@googlemail.com'
    password = 'hfpgbhljxumexiqd'
    smpt_object = smtplib.SMTP('smtp.gmail.com', 587)
    smpt_object.ehlo()
    smpt_object.starttls()
    smpt_object.login(email, password)
    from_address = email
    patient_email = 'sbridge11@googlemail.com'

    subject = "Your appointments"
    msg =  " Dear Patient, please find your appointments listed " + appointments
    email_message = 'Subject: {}\n\n{}'.format(subject, msg)

    smpt_object.sendmail(from_address, email_address, email_message)
    time = True
    print("email test1")




