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
        subject = "Confirmation of Fee Payment for PFS Course"
        body = f"Dear {data[0]},\nI hope this message finds you well. We would like to confirm that we have received your payment for the PFS course. Thank you for completing the process promptly.\nIf you have any questions or require further assistance, please feel free to reach out. We appreciate your cooperation and look forward to supporting you throughout the course.Best regards,\nCodegnan Destination!"



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


