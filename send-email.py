#create message formation

import email.message


msg=email.message.EmailMessage() # create msg object

msg["From"]= "aa098933967901@gmail.com"
msg["To"]= "aa098933967901@gmail.com"
msg["Subject"] = "you ware hacked" #main topic

#send text 
msg.set_content("meow")

#Could send more type 
# msg.add_alternative("<h1>Meow</h1>meowhecker",subtype="html")

#Connect to SMTP server and send the mail 

import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)

server.login("aa098933967901@gmail.com","ksoh cgmk ptwv lkfk")
server.send_message(msg)
server.close


