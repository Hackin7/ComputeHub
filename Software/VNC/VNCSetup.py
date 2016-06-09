#VNC Autolaunch service
import os

import sys
path = '/home/pi/git/ComputeHub/Software/VNC/' #path of VNC folder from root
sys.path.insert(0, path) 
import config

def setup():
 if config.VNC == 1:
  os.system('su pi -c "cd '+path+' && python Environment.py -s start"')
  os.system('pkill -f launch.sh') 
  os.system('/home/pi/noVNC/utils/launch.sh --vnc localhost:5901 &')
 elif config.VNC == 0:
  os.system('su pi -c "vncserver -kill :1"')
  os.system('pkill -f launch.sh') 

