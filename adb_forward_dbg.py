#-*-encoding:utf-8-*-
#   
#   __Name__:       adb_forward
#   __Author__:     tasfa
#   __Info__:       www.tasfa.cn
#   __Version__:    2.0

import os

def execCmd(cmd):
  """
    execute command
  """
  rel = os.popen(cmd)
  rel = rel.read()
  return rel

def adb_forward():
	cmd = "adb forward tcp:23333 tcp:23333 & exit"
	execCmd(cmd)
	print "[+]adb forward successfully.."

def main():
	adb_forward()

if __name__ == '__main__':
	main()