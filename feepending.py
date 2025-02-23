import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mails(complete_data):
    for data in complete_data:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        username = "shashi2028j@gmail.com"
        password = "dkzl avng eona egdr"

        from_email = "shashi2028j@gmail.com"
        to_email = data[1]
        subject = "Reminder: Outstanding Fee Payment for PFS Course"
        body = f"Dear{data[0]},\nI hope this message finds you well.This is a gentle reminder regarding the pending fee payment for PFS course. As per our records, the outstanding amount should be cleared within two days.Kindly ensure the payment is made at the earliest to avoid any inconvenience.\nIf you have any questions or require assistance, please feel free to reach out.Thank you for your prompt attention to this matter.\n Best Regards \nCodegnan Destination!"

        msg = MIMEMultipart()
        msg['From'] = from_email    
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(username,password)
        server.send_message(msg)
        server.quit()
        print(f"Mail sent to {data[0]}")
    print("*******************************************")


