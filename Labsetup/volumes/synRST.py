#!/usr/bin/envpython3

from scapy.all import *

ip = IP(src="@@@@", dst="@@@@")
tcp = TCP(sport=@@@@, dport=@@@@, flags="R", seq=@@@@)
pkt = ip / tcp
ls(pkt)
send(pkt, verbose=0)