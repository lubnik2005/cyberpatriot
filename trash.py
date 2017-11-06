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
	