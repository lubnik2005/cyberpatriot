import os, sys, subprocess, pwd, grp
mainPrint='''
Welcome to the CyberPatriot Script

Please select on of the following:

1. Check for Users
2. Check for bad Programs

'''

def main():
	print(mainPrint)
	response = input('Selection: ')
	if response == str(1):
		mainUsers()
		main()
	if response == str(2):
		programs()
		main()
	
def mainUsers():
	usernameInput = ['root','bin','daemon','adm','lp','sync','shutdown','halt','mail','operator','games','ftp','nobody','systemd-coredump','systemd-timesync','systemd-network','systemd-resolve','dbus','tss','apache','mongodb','memcached','redis','mysql','sphinx',]
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
	for p in pwd.getpwall()
		computerUsers.append(p[0])
	
	#Get user input
	QuantityUsers = input('How many users do you have?')
	for x in range(0,QuantityUsers):
		usernameInputTemp = input('Username of User: '+ str(x+1))
		usernameInput.append(usernameInputTemp)
	
	#### FINDING MISSMATCHING USRES and putting them into usersMismatch ###
	usersMismatch = []
	list3 = computerUsers + usernameInput
	for i in range(0, len(list3)):
		if ((list3[i] not in computerUsers) or (list3[i] not in usernameInput)) and (list3[i] not in usersMismatch):
			usersMismatch[len(usersMismatch):] = [list3[i]]
			print('Mismatch: ' + str(list3[i]))
	return ("Mismatched Users: ")
	print(usersMismatch)
	
	#### FINDING Anauthorized USERS ########
	unauthUsers = []
	print('Searching for Unauthorized Users')
	for x in usersMismatch:
		if x not in usernameInput:
			print('Unauthorized User: ' + x)
			unauthUsers.append(x)
	print('The Following Users are Unauthorized: ')
	print(unauthUsers)
	for x in unauthUsers:
		response = input('Would you like to delete this users:'+x+'? [1/0] ')
		if str(response) = str(1):
			os.system('sudo deluser '+x)
	###FINDING Missing USRERS #####
	missingUsers = []
	print('Searching for Missing Users')
	for x in usersMismatch:
		if x not in computerUsers:
			print('Missing User: ' + x)
			missingUsers.append(x)
	print('The Following Users are Missing: ')
	print(missingUsers)
	for x in missingUsers:
		response = input('Would you like to Create these users?:? [1/0] ')
		if str(response) = str(1):
			for x in missingUsers:
				os.system('sudo adduser '+x)
		

def programs():
	badPrograms = ['apache2','nmap','samba','wireshark']
	print('This will check for bad programs:')
	input(badPrograms)
	i = 0
	for x in badPrograms:
		if os.system('dpkg -l |grep '+x):
			response = input(x+' is installed. Purge? [1/0]: ')
			i += 1
			if str(response) == str(1):
				os.system('sudo apt-get purge '+x)
	if i == 0:
		input('No bad programs installed')
	
main()