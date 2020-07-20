import smtplib
import os
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASSWORD'))
message = "Message_you_need_to_send"
s.sendmail(os.environ.get('EMAIL_USER'),os.environ.get('EMAIL_USER'), message)
s.quit()
