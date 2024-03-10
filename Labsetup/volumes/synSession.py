#!/usr/bin/envpython3

from scapy.all import *

ip = IP(src="@@@@", dst="@@@@")
tcp = TCP(sport=@@@@, dport=@@@@, flags="A", seq=@@@@, ack=@@@@)
data = "@@@@"
pkt = ip / tcp / data
ls(pkt)
send(pkt, verbose=0)
