from scapy.all import *
from pwn import *


packets = rdpcap('DartS.pcap')
i = 0

dic = {}

for packet in packets:
    port = packet.dport
    dic[port] = packet[UDP].payload

for a in dic:
  print a
  res = list(map(ord,str(dic[a])))
  print str(res)[1:-1]
