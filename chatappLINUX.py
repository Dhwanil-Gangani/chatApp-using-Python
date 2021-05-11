#chat app for linux os

import threading as th
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

width = os.get_terminal_size().columns #get terminal size and center the content using this function.

receiverport = 1070  #port of the server were this app running
senderport = 1090     #port of your server were this app runnigg
os.system("tput setaf 6")
print("Welcome to Groovy! Chat Application!".center(width))

os.system("tput setaf 2")

senderip = input("\nEnter your IP : ") #ip address of this server

os.system("tput setaf 3")
receiverip = input("\nEnter your Friends IP : ") #ip address of receiver server

s.bind((senderip,senderport))

def receiver():
    while True:
        rcvmsg = s.recvfrom(1024)
        data = rcvmsg[0].decode()
        os.system("tput setaf 3")
        msg="Msg from"+ rcvmsg[1][0]+ " : "+data
        print(msg.center(100))
        if "bye" in data or "see you soon" in data:
            exit()

def sender():
    while True:
        sndmsg = input("\n")
        os.system("tput setaf 2")
        s.sendto(bytes(sndmsg.encode()),(receiverip,receiverport))
        if "bye" in sndmsg or "see you soon" in sndmsg:
            exit()

th.Thread(target=receiver).start()
th.Thread(target=sender).start()
