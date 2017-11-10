#!/usr/bin/env python3.5


import os, sys, subprocess, pwd, grp, apt, glob
from helpInfo import helpInfo

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

mainPrint='''
Welcome to the CyberPatriot Script

Please select on of the following:

1. Check for Users
2. Check for bad Programs
3. Check for Unauth Media Files (This takes forever...)
4. Ports
5. Firewall
6. Programs and Updates
9. Help
=======
10. Exit


'''

def main():
	if not os.geteuid() == 0: # Check if user is running as root
		sys.exit('Script must be run as root')
	os.system('printf "\033c"')
	print(mainPrint)
	response = input('Selection: ')
	if str(response) == str(1):
		os.system('printf "\033c"')
		mainUsers()
		main()
	if str(response) == str(2):
		os.system('printf "\033c"')
		programs()
		main()
	if str(response) == str(3):
		os.system('printf "\033c"')
		mediaFiles()
		main()
	if str(response) == str(4):
		os.system('printf "\033c"')
		mainPort()
		main()
	if str(response) == str(5):
		os.system('printf "\033c"')
		firewall()
		main()
	if str(response) == str(6):
		os.system('printf "\033c"')
		installPrograms()
	if str(response) == str(9):
		os.system('printf "\033c"')
		helpInfo()
		main()
	if str(response) == str(10):
		os.system('printf "\033c"')
		print(bcolors.FAIL + 'Thanks for using this AWESOME SCRIPT!!' + bcolors.ENDC)
		quit()
	
	main()

def mainUsers():
	usernameInput = ['root', 'daemon', 'bin', 'sys', 'sync', 'games', 'man', 'lp', 'mail', 'news', 'uucp', 'proxy', 'www-data', 'backup', 'list', 'irc', 'gnats', 'nobody', 'systemd-timesync', 'systemd-network', 'systemd-resolve', 'systemd-bus-proxy', 'syslog', '_apt', 'messagebus', 'uuidd', 'lightdm', 'whoopsie', 'avahi-autoipd', 'avahi', 'dnsmasq', 'colord', 'speech-dispatcher', 'hplip', 'kernoops', 'pulse', 'rtkit', 'saned', 'usbmux',]

	print('Users Inputed:')
	if len(usernameInput) == 0:
		print('No Users Inputed')
	else:
		print(usernameInput)
	#Get all user data
	# Refer to https://docs.python.org/2/library/pwd.html
	all_user_data = pwd.getpwall()
	
	#Put the Current users on the computer into list computerUsers
	computerUsers = []
	for p in pwd.getpwall():
		computerUsers.append(p[0])
	print('Users On Computer')	
	print(computerUsers)
	#Get user input
	QuantityUsers = int(input('How many users do you have?: '))
	for x in range(0,QuantityUsers):
		usernameInputTemp = str(input('Username of User '+ str(x+1)+': '))
		usernameInput.append(usernameInputTemp)
	
	#### FINDING MISSMATCHING USRES and putting them into usersMismatch ###
	usersMismatch = []
	list3 = computerUsers + usernameInput
	for i in range(0, len(list3)):
		if ((list3[i] not in computerUsers) or (list3[i] not in usernameInput)) and (list3[i] not in usersMismatch):
			usersMismatch[len(usersMismatch):] = [list3[i]]
			print(bcolors.FAIL + 'Mismatch: ' + bcolors.ENDC + str(list3[i]))
	print("Mismatched Users: ")
	print(usersMismatch)
	
	#### FINDING Unauthorized USERS ########
	unauthUsers = []
	input('Searching for Unauthorized Users')
	for x in usersMismatch:
		if x not in usernameInput:
			print(bcolors.FAIL + 'Unauthorized User: '  + bcolors.ENDC + x)
			unauthUsers.append(x)
	if len(unauthUsers) == 0:
		print('No Unauthorized Usrers')
	else:	
		print('The Following Users are Unauthorized: ')
		print(unauthUsers)
	response = input('Do you want the script to do this automatically?[1/0] ')
	if str(response) == str(1):
		for x in unauthUsers:
			os.system('sudo mv /home/' + x +' ./store/home/unAuth')
			os.system('sudo deluser ' + x)
	else:	
		for x in unauthUsers:
			response = input('Would you like to delete this users: '+x+'? [1/0] ')
			if str(response) == str(1):
				os.system('sudo deluser ' + x)
	###FINDING Missing USRERS #####
	missingUsers = []
	input('Searching for Missing Users')
	for x in usersMismatch:
		if x not in computerUsers:
			print(bcolors.FAIL + 'Missing User: ' + bcolors.ENDC + x)
			missingUsers.append(x)
	if len(missingUsers) == 0:
		print('No Missing Users')
	else:	
		print('The Following Users are Missing: ')
		print(missingUsers)
	response = input('Want the script to create all of the users at once?[1/0] ')
	if str(response) == str(1):
		response = input('What password should they all have?: ')
		for x in missingUsers:
			os.system('sudo useradd '+ x)
			os.system('echo -e "' + response + '" | sudo passwd -q ' + x)
	else:
		for x in missingUsers:
			response = input('Would you like to create '+x+'?: [1/0] ')
			if str(response) == str(1):
				os.system('sudo adduser '+x)
	input('Great! All finished with Users')
		

def programs():
	badPrograms = ['apache2','nmap','samba','wireshark','wireshark-common','hydra']
	print('This will check for the following programs:')
	print(badPrograms)
	print('Searching...')
	cache = apt.Cache()
	cache.open()
	i = 0
	for x in badPrograms:
		if cache[x].is_installed:
			response = input(x+' is installed. Purge? [1/0]: ')
			i += 1
			if str(response) == str(1):
				os.system('sudo apt-get purge '+x)
	if i == 0:
		input('No bad programs installed')
	cache.close()
	
def mediaFiles():
		typesOfMedia = ['jpg','png','mp3','jpeg','mov','mp4','avi','mpg','mpeg','flac','m4a','flv','ogg','gif']
		defaultMedia = []
		allMedia = []
		unAuthMedia = []
		response = None
		response = input('Where do you want to search (home is default)?: ')
		if response != None:
			input("Well that's too bad, it hasn't been implemented yet, will search from home!")
		#Searching for All Media
		#Refer to: https://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
		print('Searching for Media with the following extentions:')
		print(typesOfMedia)
		for ext in typesOfMedia:
			for filename in glob.iglob('/home/**/*.'+ext, recursive=True):
				print(bcolors.FAIL + 'Media File: ' +bcolors.ENDC +filename)
				allMedia.append(filename)
		
		#Searching for UnauthMedia
		list3 = allMedia + defaultMedia
		for i in range(0, len(list3)):
			if ((list3[i] not in allMedia) or (list3[i] not in defaultMedia)) and (list3[i] not in unAuthMedia):
				unAuthMedia[len(unAuthMedia):] = [list3[i]]
				print(bcolors.FAIL + 'Unauthorized File: ' + bcolors.ENDC + str(list3[i]))
				os.system('sudo mv '+str(list3[i])+' ./store/media')
		if len(unAuthMedia) != 0:
			input('Finished searching for UnauthFiles, and copied all files to ./store/media')
			response = input('Delete all Unauth Files?[1/0] ')
			if str(response) == str(1):
				for file in unAuthMedia:
					print('Deleting: '+file)
					os.system('sudo rm -f '+file)
		else:
			print('No Unauthorized files found!')
		input('Finished with the file section!')
def mainPort():
	ports = ['23','2049','6000:6000','7100','515','111']
	for port in ports:
		dropa = 'iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport ' + port+ ' -j DROP'
		dropb = 'iptables -A INPUT -p udp -s 0/0 -d 0/0 --dport ' + port+ ' -j DROP'
		os.system(dropa)
		os.system(dropb)
		print(dropa + '\n' + dropb)
	os.system('iptables -A INPUT -p all -s localhost -i eth0 -j DROP')
	input('Finished Ports')

def firewall():
	denyStuffs = ['23','2049','515','111']
	os.system('ufw enable')
	for denyStuff in denyStuffs:
		os.system('ufw deny ' + denyStuff)
	os.system('lsof  -i -n -P; netstat -tulpn')
	input('Finished Firewall')

def installPrograms():
	os.system('sudo apt-get --assume-yes upgrade ')
	os.system('sudo apt-get --assume-yes upgrade')
	os.system('sudo apt-get -V -y --assume-yes install --reinstall coreutils')
	os.system('sudo apt-get apt-get -V -y --assume-yes install firefox hardinfo chkrootkit iptables portsentry lynis ufw gufw sysv-rc-conf nessus clamav')

	programs = ['synaptic','hardinfo','chkrootkit','lynis','freshclam','clamscan']
	input('Finished Programs')
main()

