def helpInfo():

	info = [['Users','''
1. Users
		1. Run Users
		2. First Section will show default users on Ubuntu
		3. Second Section is showing all users on computer
		4. You will be asked how many users you want to enter. This value is supposed to come from your README. Thus, the amount of usrers on your readme should be entered.
		5. You will now be asked to enter the usrers. Simply look at your README, and enter it one by one.
		6. The program will now check for mismatches in what you entered, and the computer users
		7. The progam will stop
		8. Press ENTER to continue
		7. The program will now look for unauthorized users.
		8. Delete if Neccissary - 1 is yes - 0 is no
		9. Now the progam will look for missing users 
		10. If missing users exist, it will ask if you want to make one.
	'''],['Bad Programs','''
	1. The program will first show the packages that it is looking for
	2. The progam will now search for those packages
	3. The program will ask you if you want to delete the package
	''']]
	
	
	print('This is the help Desk, you should get answers here.')
	for item in range(0,len(info)):
		print(str(item) + ' : ' + str(info[item][0]))
	response = input('Please select one of the following: ')
	input(info[int(response)][1])
