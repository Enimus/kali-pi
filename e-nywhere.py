
#!/usr/bin/python

import os
import sys, traceback

def main():
	try:

## 
##				print ('''
## 
##              ______                           __          __  _              _____         
##             |  ____|    \041[2;32m            \ \        / / | |            |  __ \        
##             | |__     ______   _ __    _   _   \ \  /\  / /  | |__     ___  | |__) |   ___ 
##             |  __|   |______| | '_ \  | | | |   \ \/  \/ /   | '_ \   / _ \ |  _  /   / _ \
##             | |____           | | | | | |_| |    \  /\  /    | | | | |  __/ | | \ \  |  __/
##             |______|          |_| |_|  \__, |     \/  \/     |_| |_|  \___| |_|  \_\  \___| \041[2;m
##                                         __/ |                                              
##                                         |___/                  
##                                         
## \041[2;32m+ ---+ ---+- +=[ Author: En1MuS \041[2;m
## \041[2;32m+ ---+ ---+- +=[ 331 Tools \041[2;m
##
##				print ('''
##

			
		''')
	  	def inicio1():
		    	  while True:
		        		    print ('''
  


1) Add Kali Keys and repos
2) Remove all kali linux repositories

			''')


				opcion0 = raw_input("\033[1;36mkat > \033[1;m")


				while opcion0 == "1":
					print ('''
          
          
          
1) Add kali linux repos
2) Remove kali linux repos

					''')
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali repo| \ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()




				def inicio():
					while opcion0 == "2":
						print ('''
\031[1;36m**************************** Choise The Package tipe *****************************\031[1;m


1) Top 10
2) Light
3) Medium
4) HaCk PaCk
5) Kali Menu
6) Classic Menu

			 ''')
       


			  			opcion1 = raw_input("\033[1;36mkat > \033[1;m")
		  				if opcion1 == "back":
		  					inicio1()
	  					elif opcion1 == "gohome":
	  						inicio1()
	  					elif opcion1 == "0":

		  				if opcion1 == "1":
                cmd = os.system("apt-get -f install -y kali-linux-top10 paros parsero proxystrike recon-ng skipfish sqlmap sqlninja  ua-tester uniscan vega w3af webscarab websploit tor  wpscan    dnschef   iaxflood inviteflood  mitmproxy  responder sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat powersploit u3-pwn 
	  					while opcion1 == "1":
  							print ('''

							elif opcion1 == "2":
	  					 	cmd = os.system("apt-get -f install -y paros parsero proxystrike recon-ng kali-linux-top10 skipfish sqlmap sqlninja  ua-tester uniscan vega w3af webscarab websploit  wpscan tor dnschef   iaxflood inviteflood  mitmproxy  responder sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat powersploit u3-pwn 
              
              
             	elif opcion1 == "3":  
  							cmd = os.system("apt-get -f install -y  dnsrecon exploitdb kali-linux-top10  ghost-phisher kali-linux-pwtools masscan nmap parsero recon-ng set wireshark ismtp intrace hping3 tor lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 aircrack-ng bluesnarfer fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl  kismet mdk3 wifite bbqsql davtest deblaze dirb dirbuster fimap funkload grabber tor joomscan jsql proxychains padbuster paros              

              elif opcion1 == "4":  
		  					cmd = os.system("apt-get -f install -y  dnsrecon exploitdb kali-linux-top10 kali-linux-web xrdp driftnet ghost-phisher masscan nmap parsero recon-ng set wireshark ismtp intrace hping3 tor ettercap-graphical lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 aircrack-ng bluesnarfer fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl  kismet mdk3 wifite bbqsql davtest deblaze dirb dirbuster fimap funkload grabber tor joomscan jsql proxychains padbuster paros parsero proxystrike recon-ng skipfish sqlmap sqlninja  ua-tester uniscan vega w3af webscarab websploit  wpscan    dnschef   iaxflood inviteflood  mitmproxy  responder sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat powersploit u3-pwn webshells dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory set shellnoob sqlmap dumpzilla iphone-backup-analyzer p0f pdf-parser pdgmail  funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest termineter thc-ssl-dos acccheck burpsuite cewl creddump crunch findmyhash hash-identifier john johnny maskprocessor  ncrack pack rainbowcrack  webscarab wordlists

              elif opcion1 == "5":  
		  					cmd = os.system("add-apt-repository ppa:diesch/testing && apt-get update")

              elif opcion1 == "5":  
		    				cmd = os.system("sudo apt-get install classicmenu-indicator")

              
