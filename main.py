#!/usr/bin/env python3.5


import os, sys, subprocess, pwd, grp, apt

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
3. Exit

'''

def main():
	if not os.geteuid() == 0: # Check if user is running as root
		sys.exit('Script must be run as root')
	os.system('printf "\033c"')
	print(mainPrint)
	response = input('Selection: ')
	if str(response) == str(1):
		mainUsers()
		main()
	if str(response) == str(2):
		programs()
		main()
	if str(response) == str(3):
		os.system('printf "\033c"')
		print(bcolors.FAIL + 'Thanks for using this AWESOME SCRIPT!!' + bcolors)
		quit()
	


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
	
	#### FINDING Anauthorized USERS ########
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
	for x in unauthUsers:
		response = input('Would you like to delete this users: '+x+'? [1/0] ')
		if str(response) == str(1):
			os.system('sudo deluser '+x)
	###FINDING Missing USRERS #####
	missingUsers = []
	print('Searching for Missing Users')
	for x in usersMismatch:
		if x not in computerUsers:
			print(bcolors.FAIL + 'Missing User: ' + bcolors.ENDC + x)
			missingUsers.append(x)
	if len(missingUsers) == 0:
		print('No Missing Users')
	else:	
		print('The Following Users are Missing: ')
		print(missingUsers)
	for x in missingUsers:
		response = input('Would you like to create '+x+'?: [1/0] ')
		if str(response) == str(1):
				os.system('sudo adduser '+x)
		

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
main()
