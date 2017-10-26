import sys
from subprocess import Popen, PIPE

def unix():
	p1 = Popen(["ifconfig"], stdout=PIPE) 
	p2 = Popen(["uname", "-a"], stdout=PIPE) 
	p3 = Popen(["cat","/etc/resolv.conf"], stdout=PIPE) 
	#p1 = Popen(["systeminfo"], stdout=PIPE) #for win
	output = p1.communicate()[0] + "--- uname -a ---\n " + p2.communicate()[0] + "\n--- cat /etc/resolv.conf ---\n" + p3.communicate()[0]
	print ("Output:\n{}".format(output))

def win():
	print("This is Windows platform! I'm dead.\nX_X")
	p1 = Popen(["systeminfo"], stdout=PIPE) #for win
	output = p1.communicate()[0]
	print ("Systeminfo:\n{}".format(output))

#print("platform:" + sys.platform)
if sys.platform == "linux2" or sys.platform == "linux": #only linux
	unix()
elif sys.platform == "win32" or sys.platform == "win64": # Depends on version of compiler (did not check win64)
	win()
else: 
	print("ERROR: NOT DEFINED PLATFORM: {}".format(sys.platform))


try: # pause and exit
	input("Press any key to exit...")
	exit(0)
except:
	exit(0)