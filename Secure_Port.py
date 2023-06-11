'''
x0c0x0c0x0c0x0c00xc0x0c0x0c0x00xc0xc0c0x0c
xc           In the name of god         cf
xc                                      xf
xc               Dev : Null             c0
xc                                      x0
xc   Github : github.com/rooting-4401   c0
x0c0xc0xx0c0xc00cx0xc0xc0c0x0c0xc0xc0c0x0c
'''
from socket import *
from colorama import Fore,init
from Banner import bnr
import os

# Def Init 
init()

def main():
	# Clear Time 
	linux = 'clear'
	windows = 'cls'
	
	os.system([linux,windows][os.name == 'nt'])
	
	#banner ....
	bnr.bn()

#Def Port Scanner
def Port():
	
	#Get ip
	ip = input(Fore.YELLOW+'\nEnter Your ip:')
	
	
	#list Port
	list_port = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,3380,443,138,139,179,110,137]
	
	
	# loop (for)
	for ports in list_port:
		try:
			
			sock = socket(AF_INET,SOCK_STREAM)
			req = sock.connect_ex((ip,ports))
			
			# if and else
			if req == False:
				try:
					serv = getservbyport(ports)
				except:
					continue
				
				print(Fore.GREEN+f'[-+-]Openned Ports {ip}:{ports}({serv})')
				o = open('open-port.txt','a')
				o.write(f'[-+-]Openned Ports {ip}:{ports}({serv})\n')
				o.close()
			else:
				print(Fore.RED+f'Clossed Port {ports}')
				o = open('close-port.txt','a')
				o.write(f'Clossed Port {ip}:{ports}\n')
				o.close()
		except Exception as xerr:
			print(Fore.RED+'Error msg : ' + xerr)

main()
Port()