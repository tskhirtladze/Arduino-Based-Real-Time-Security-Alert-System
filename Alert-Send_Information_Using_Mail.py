import time
import serial
import smtplib
import ssl
from email.message import EmailMessage

subject = "Security Alert!!!!!"
body = "თქვენს სახლში შემოჭრა დაფიქსირდა!!!"
sender_email = "tskhi2020@agruni.edu.ge"
receiver_email = "tskhi2020@agruni.edu.ge"
password = input("შეივანეთ ელ. ფოსტის პაროლი: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"თქვენს სახლში შემოჭრა დაფიქსირდა!!!"

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")


arduino_data = serial.Serial('com5', 9600)
time.sleep(1)

while True:
    while arduino_data.inWaiting() == 0:
        pass
    data_packet = arduino_data.readline()
    data_packet = str(data_packet, 'utf-8')
    data_packet = data_packet.strip('\r\n')
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Success")
    print(data_packet)