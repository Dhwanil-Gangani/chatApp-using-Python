#for windows

import threading as th
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

width = os.get_terminal_size().columns                #get terminal size and center the content using this function.

receiverport = 1090                                          #port of the server were this app running
senderport = 1070                                             #port of your server were this app runnigg

print("Welcome to Groovy! Chat Application!".center(width))

senderip = input("\nEnter your IP : ")                      #ip address of this server

receiverip = input("\nEnter your Friends IP : ")              #ip address of receiver server

s.bind((senderip,senderport))

def sender():
       while True:
            sndmsg = input("\n")
            s.sendto(bytes(sndmsg.encode()),(receiverip,receiverport))
            if "bye" in sndmsg  or "see you soon" in sndmsg:
                 exit()

def receiver():
       while True:
            rcvmsg = s.recvfrom(1024)
            data = rcvmsg[0].decode()
            msg="Message From "+ rcvmsg[1][0]+ " : "+data
            print(msg.center(100))
            if "bye" in data or "see you soon" in data:
                 exit()

th.Thread(target=sender).start()
th.Thread(target=receiver).start()

