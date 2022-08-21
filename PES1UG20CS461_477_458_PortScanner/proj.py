import logging
from tabnanny import verbose
from telnetlib import IP
from urllib import response;
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
from scapy.all import *

if len(sys.argv) != 4:
    print("Invalid input format . \n Enter %s IP address starting_port_number ending_port_number \n"%(sys.argv[0]))
    sys.exit(0)
IP_addr = str(sys.argv[1])   
start_port = int(sys.argv[2])
ending_port  = int(sys.argv[3])
print('Scanning '+IP_addr+' for open TCP ports \n')

if start_port == ending_port:
     ending_port +=1

for x in range(start_port,ending_port):
    packet = IP(dst=IP_addr)/TCP(dport=x,flags='S')
    response = sr1(packet,timeout=1,verbose=0)
    if response and  response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
        print('Port '+str(x)+' is open .')
    else:
        print('Port '+str(x)+' is closed .')
    
print("The scan was succesful and is over .\n")