import smtplib
import ssl
port = 465  # For SSL
password = "cloyfszstdncrerk"

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = "yu.attend@gmail.com"
rec="awosradaideh@gmail.com"




message = """
     Subject: You Have been recorded 


     You have been recorded as absent from the course:  """
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    # TODO: login and send email

    server.login(sender_email, password)
    server.sendmail(sender_email, rec, message)
