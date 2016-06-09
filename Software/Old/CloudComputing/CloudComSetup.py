#CloudComputing Autolaunch service
import os

import sys
path = '/mnt/Making/RaspberryPi/SittingFox/Software/CloudComputing/' #path of CloudComputing folder from root
sys.path.insert(0, path) 
import config

def setup():
 if config.CloudCom == 1:
  os.system('su pi -c "python '+path+'Environment.py -s start"')
  os.system('pkill -f launch.sh') 
  os.system('/home/pi/noVNC/utils/launch.sh --vnc localhost:5901 &')
 elif config.CloudCom == 0:
  os.system('su pi -c "vncserver -kill :1"')
  os.system('pkill -f launch.sh') 

