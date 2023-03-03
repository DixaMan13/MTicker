import smtplib
from Seats import seat
from email.message import EmailMessage
from datetime import datetime
import time
import random
import string

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tve21ec052@cet.ac.in', 'pythonpro1')
n=0
total=84
arr=[]
amt=0
bookedarr=[]
ch=0
mailmsg=''
charlist = list(string.ascii_letters) + list(string.digits)
bid = ''


def mailer():
    msg=EmailMessage()
    msg['Subject']='Cube Digital Movie Booking'
    msg['From']='tve21ec052@cet.ac.in'
    msg['To']=eml
    mailmsg='Tickets successfully booked!\nName of the Booker:'+name+'\nPhone number:'+str(ph)+'\nBooked tickets:'
    for i in arr:
        mailmsg=mailmsg+i+','
    mailmsg=mailmsg+'\nTotal amount to to be paid:'+str(amt)+'\nDate and Time of Booking:'+dt+'\nBooking ID:'+bid+'\n\nThank you for choosing our services.'
    msg.set_content(mailmsg)
    server.send_message(msg)

def printer():
    print("Total no.of seats left:",total,'\n')
    for a in range(2):
        for i in range(6):
            print("\t"*5,end="")
            for j in range(7):
                print(seat[a][i][j],"\t",end="")
            print()
        print()
    print('\t'*6,'________________\n','\t'*7,'(Screen)')

def updater(ch):
    for i in range(6):
        for j in range(7):
            if seat[ch][i][j] in arr:
                seat[ch][i][j]='X'


print("----------WELCOME TO CUBE DIGITAL MOVIE TICKET BOOKING----------")
name=input("Please enter your name:")
ph=int(input("Please enter your phone number:"))
eml=input("Please enter your email (Details will be mailed after the booking has been confirmed):")
opt='YES'
while opt=='YES':
    print("\n\t\tAvailable seats (X shows the already booked seats):")
    printer()
    flag = True
    while flag:
        ch = int(input(
            "Select the class: \n 0-Diamond class\t(Rows A-F)\t(180 Rs.) \n 1-Gold class\t(Rows G-L)\t(150 Rs.) :"))
        n = int(input("\nEnter the no.of seats you want to book:"))
        print("Enter the seats one by one:")
        for i in range(n):
            arr.append(input().upper())
            if arr[i] in bookedarr:
                print(
                    "Error in booking the chosen seats because one or more seats have already been taken. Please try again.")
                n = 0
                arr.clear()
                flag = True
                break
            else:
                flag = False
    for i in range(n):
        bookedarr.append(arr[i])
    updater(ch)
    total-=n
    time.sleep(2)
    for i in range(7):
        bid = bid + random.choice((charlist))
    print("Tickets Successfully booked!!")
    dt = (datetime.now()).strftime("%d/%m/%Y,%H:%M:%S")
    print("Tickets booked on", dt)
    printer()
    if ch==0:
        amt=n*180
    else:
        amt=n*150
    print("\nName:",name)
    print("Phone Number:", ph)
    print("Email ID:",eml)
    print("Booked seats:",arr)
    print("Booking ID:",bid)
    print("Total amount=Rs.", amt)
    mailer()
    print('\nMail sent successfully to',eml)
    if len(bookedarr)==84:
        print("Sorry! The Movie is Housefull!")
    opt=input("Do you wish to continue booking more tickets? (Enter yes or no):").upper()
    arr.clear()
    bid=''

print("\nThank you for choosing our services. We hope you enjoy your movie!")
