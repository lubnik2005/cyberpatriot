import os
import sys
import subprocess
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
	usersInputted = []
	usersComputer = subprocess.Popen(["cut -d: -f1 /etc/passwd"], shell=True, stdout=subprocess.PIPE).stdout
	usersComputer = usersComputer.read().splitlines()
	#Though bitwise is better for comparing, we will use utf-8 instead
	for x in usersComputer:
		x = x.decode()
	for x in usersComputer:
		pass
		#x.remove(2)
	print(usersComputer)
	print('Welcome to the user section! Please input all users')
	response = input('Please select the amount of users you have: ')
	for x in range(0,int(response)):
		user = input('Username of User: ')
		usersInputted.append(user)
	print(usersInputted)
	
	for x in usersInputted:
		for y in usersComputer:
			if x == y:
				print 
	
def programs():
	badPrograms = ['apache2','nmap','samba','wireshark']
	print('This will check for bad programs:')
	input(badPrograms)
	i = 0
	for x in badPrograms:
		if os.system('dpkg -l |grep '+x):
			response = input(x+' is installed. Purge? [1/0]: ')
			i += 1
			if response == 1:
				os.system('sudo apt-get purge '+x)
	if i == 0:
		input('No bad programs installed')
	
main()