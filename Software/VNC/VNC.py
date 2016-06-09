#VNC Config
#Run in directory and as root

import os
import time

from PitftGraphicLib import *
#from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()

import MenuUI
returner = 0
def backer():
    global returner
    if (returner == 1):
        if (MenuUI.page > 0):
           MenuUI.back = 1
        elif (MenuUI.page == 0):
           MenuUI.back = 1
           returner = 0

def passs():pass

import config
def filerewrite():
     ###Rewriting file############################################################
     os.system('echo "VNC = ' + str(config.VNC) + '" > config.py')
     ##############################################################################

def Menu(): 
   ####Toggle switch#########################################################
   def switch():
     if config.VNC == 1:
         config.VNC = 0
         os.system('su pi -c "vncserver -kill :1"')
         os.system('pkill -f launch.sh')
     else:
         config.VNC = 1
         os.system('su pi -c "python Environment.py -s start"')
         os.system('pkill -f launch.sh')
         os.system('/home/pi/noVNC/utils/launch.sh --vnc localhost:5901 &')
     filerewrite()
   def state():
       if config.VNC == 0:return "Switch On"
       else:return "Switch Off"
   ##########################################################################
   def vncpass(): 
     disinitdis()
     os.system('tap ./connection')
     os.system('echo "(lxterminal -e vncpasswd && pkill xinit) & " >> ./connection')
     os.system('echo "matchbox-keyboard & " >> ./connection')
     os.system('echo "matchbox-window-manager" >> ./connection')
     os.system('FRAMEBUFFER=/dev/fb1 xinit ./connection')
     os.system('rm -rf ./connection')
     initdis()

   def loadup():
       backer()
       make_button(state(), 25, 75, 27, 130, 5, yellow, 24, switch)
   mainmenu = (('', black, 0, passs),('Change Password', orange, 20, vncpass)) #Debugging
   MenuUI.menu.load(MenuUI.menu.slotconf,'VNC Computing',cyan,mainmenu,loadup)

Menu()
