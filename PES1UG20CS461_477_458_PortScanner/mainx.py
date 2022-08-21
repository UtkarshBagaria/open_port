from scapy.all import *
from scapy.all import IP
from scapy.all import TCP
import sys

if len(sys.argv) != 3:
    print("Usage: %s target port" % (sys.argv[0]))
    sys.exit(0)

target = str(sys.argv[1])
port = int(sys.argv[2])

print('Scanning '+ target +' for open TCP ports\n')

packet = IP(dst=target)/TCP(dport=port, flags='S')
response = sr1(packet, timeout=1, verbose=1)

if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
    print('\nPort '+str(port)+' is open!')

final_packet = IP(dst=target)/TCP(dport=response.sport, flags='R')
sr(final_packet, timeout=1, verbose=0)

print('Scan is complete!\n') 