#-*-encoding:utf-8-*-
#   
#   __Name__:       dydebug
#   __Author__:     tasfa
#   __Info__:       www.tasfa.cn
#   __Version__:    2.0

import os
import time



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
    print "[+]Welcome to use dydebug!"
    print "[+]For more infomation --> www.tasfa.cn!!"
    print "<--------------------------------------------------->"

def execCmd(cmd):
  """
    execute command
  """
  platfrom_cmd ="start cmd /k " #window cmd!

  cmd = platfrom_cmd + cmd
  rel = os.system(cmd)
  

def start_ser_init():
  start_cmd = "python android_server_listen.py"
  execCmd(start_cmd)

def adb_forward():
  forward_cmd = "adb_forward_dbg.bat"
  execCmd(forward_cmd)

def main():
  start_ser_init()
  time.sleep(2)
  adb_forward()
  adb_forward()
  

if __name__ == '__main__':
  main()

# start listern
# 自动转发端口

# 询问是要attach（可以了解下 ida的命令行） 还是 dydebug 

# 询问是要全自动 还是 手动

# 若手动 询问是否要打开ida 是否要打开ddms 是否要打开jeb connect  

