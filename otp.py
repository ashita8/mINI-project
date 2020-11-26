
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr='sendermail@gmail.com '
to_addr=['abc@gmail.com','efg.@gmail.com']
msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='just to check'

body='hello world'

msg.attach(MIMEText(body,'plain'))

email='sendermail.mypc@gmail.com ' #mail id from which you have to send mail please note that in this mail id you have to open access to other app(backdoor)
password='password' #password for this mail id

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)
mail.quit()