from ai import aiProcess

def retry():
    print("sure, I can write a email for you")
    remail= input("Enter Receiver's email: ")
    print("What's the subject of your email ?")
    subject= input()
    print("Would you like to write the email yourself or let ai handle it for you")
    try:
        ch= input()
        if "myself" in ch:
            print("ok, what's the message then ?")
            message= input()
            content= message
            welcome(remail,subject,content)

        elif "ai" in ch.lower():
            print("ok, then can you give a short brief of your email")
            prompt= input()
            message= aiProcess(f"write an email for me, I am just giving a short brief of it, (don't add subject and no lead in sentence) : {prompt}")
            print("would you like to add the following content in your email:")
            print(message)
            respo = input("send it (yes/no): ")
            if respo.lower() == "yes":
                content= message
                welcome(remail,subject,content)
            else:
                retry()
        else:
            print("try again")
            retry()
    except Exception as e:
        print(e)
        retry()



import smtplib
import os
from dotenv import load_dotenv
load_dotenv
smtp_server= "smtp.gmail.com"
port = 587
sender_email= "<Your-Email-Address>"
password= "<Your-Password>"

def welcome(receiver_email,subject,content):
    message= f"Subject: {subject}\n\n{content}"
    try:
        server= smtplib.SMTP(smtp_server,port)
        server.starttls()
        server.login(sender_email,password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        server.quit()
