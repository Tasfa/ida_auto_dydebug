#-*-encoding:utf-8-*-
#   
#   __Name__:       am-start
#   __Author__:     tasfa
#   __Info__:       www.tasfa.cn
#   __Version__:    1.0

import os


def banner():
    """
        Print the banner and Version Info
    """
    print "<--------------------------------------------------->"
    print """ 
     _____          __       
    |_   _|_ _ ___ / _| __ _ 
      | |/ _` / __| |_ / _` |
      | | (_| \__ \  _| (_| |
      |_|\__,_|___/_|  \__,_|
                             
    """
    print "[+]Welcome to use am-auto-start!"
    print "[+]For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->"


def check_name_path():
	"""
	Push the android_server to /data/local/tmp and then set the permission!
	"""

def exception_deal():
	pass

def check_device_alive():
	"""
	To check the device whether it can be found !
	"""

	Null_flag_lst = ['List of devices attached\n', '\n']
	cmd = 'adb devices'
	rel = os.popen(cmd)
	rel = rel.readlines()
	if rel == Null_flag_lst:
		print '[+]Please check your device !'
		print '[+]'+str(rel)
		return False
	return True
		


def close_an_ser_proc():
	"""
	To fix the bug that there was another android_server process leading to start failed
	"""
	
	cmd = 'adb shell su -c "ps | grep an_ser"'
	rel = os.popen(cmd)
	rel = rel.read()
	if rel == '':
		return ''
	print "[+]Killing android_server..."
	for x in xrange(len(rel)):
		if rel[x].isdigit():
			for i in xrange(x,len(rel)):
				if rel[i] == ' ':
					pid = rel[x:i]
					break
			break
	kill_cmd = "adb shell su -c 'kill "+pid+"'"

	
	rel = os.popen(kill_cmd)
	
	print "[+]android_server killed..."


def start_an_server():
	"""
	Start android_server
	"""
	error_flag = "Address already in use"
	file_not_found_error = "not found"
	try:
		print "[+]Running an_ser"
		rel = os.popen('adb shell su -c "./data/local/tmp/an_ser"')
		rel = rel.read() 
		
		if file_not_found_error in rel:
			print "Please check the android_server whether it has been move to your Phone!"
			check_name_path()
		elif error_flag in rel:
			close_an_ser_proc()
			start_an_server()	
	except Exception as e:
		exception_deal()



def main():
	banner()
	try:
		if check_device_alive():
			close_an_ser_proc()
			start_an_server()

	except KeyboardInterrupt:
		print "[+]Ctrl + C User exit!"
		close_an_ser_proc()
		print "[+]Closed android_server process !"
	

if __name__ == '__main__':
	main()