#-*-encoding:utf-8-*-
#   
#   __Name__:       android_server_listen
#   __Author__:     tasfa
#   __Info__:       www.tasfa.cn
#   __Version__:    2.0

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
    print "[+]Welcome to use android_server_listen!"
    print "[+]For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->"


def execCmd(cmd):
  """
    execute command
  """
  rel = os.popen(cmd)
  rel = rel.read()
  return rel

def push_an_ser():
	"""
	Push the android_server to /data/local/tmp and then set the permission!
	"""
	push_cmd = 'adb push android_server /data/local/tmp/an_ser'
	permission_cmd = """adb shell "su -c 'chmod 777 /data/local/tmp/an_ser'" """
	if check_device_alive():
		print "[+]Pushing the android server..."
		print "[+]Please Wait a minute.."
		execCmd(push_cmd)
		execCmd(permission_cmd)
		print "[+]Push successfully..."
		return True
	else:
		return False


	

def check_an_ser():
	"""
	check whether there is a android server
	"""
	cmd = 'adb shell  "ls -l /data/local/tmp | grep an_ser "'
	rel = execCmd(cmd)
	if rel: 
		return True # not null
	else:
		return push_an_ser()


def exception_deal():
	"""
	V2 is a bug feedback alert!
	"""
	print "*****************************************"
	print "[+]I am so sorry!"
	print "[+]There is something wrong..." 
	print "[+]Plesse push the bug to me and emali me the detail Thankyou!..."
	print "Email : root#tasfa.cn"
	print "*****************************************"

def check_device_alive():
	"""
	To check the device whether it can be found !
	"""

	Null_flag_lst = ['List of devices attached\n', '\n']
	cmd = 'adb devices'
	rel = os.popen(cmd)
	rel = rel.readlines() #note here	
	if rel == Null_flag_lst:
		print '[+]Please check your device !'
		print '[+]'+str(rel)
		return False
	return True
		


def close_an_ser_proc():
	"""
	To fix the bug that there was another android_server process leading to start failed
	"""
	
	cmd = """adb shell "su -c 'ps | grep an_ser'"""
	rel = execCmd(cmd)
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

	kill_cmd = "adb shell \"su -c 'kill -9 " + pid + "'\""
	rel = execCmd(kill_cmd)
	print "[+]android_server killed..."


def start_an_server():
	"""
	Start android_server
	"""
	error_flag = "Address already in use"
	file_not_found_error = "not found"
	try:
		print "[+]Running an_ser "
		print "[+]Listening on port #23333..."
		cmd = """adb shell "su -c './data/local/tmp/an_ser -p23333'" """
		rel = execCmd(cmd)  #here will block the cmd

		if file_not_found_error in rel:
			print "Please check the android_server whether it has been move to your Phone!"
			check_an_ser()
		elif error_flag in rel:
			close_an_ser_proc()
			start_an_server()

	except Exception as e:
		exception_deal()


def main():
	#banner()
	try:
		if check_device_alive() & check_an_ser():
			close_an_ser_proc()
			start_an_server()

	except KeyboardInterrupt:
		print "[+]Ctrl + C User exit!"
		close_an_ser_proc()
		print "[+]Closed android_server process !"
	

if __name__ == '__main__':
	main()
