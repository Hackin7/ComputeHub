#CloudCom Config
#Run in directory and as root

import os
import time

from PitftGraphicLib import *
#from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()

import config
back = 0 
page = 0
######Storage#################################################################
class Menu:
 def __init__(self): pass
      
 # Slot Configuration
 def slotconf(self,slot, app):
    if slot == 1:
        make_button(app[0], 25, 75, 27, 130, 5, app[1], app[2], app[3])
    if slot == 2:
        make_button(app[0], 165, 75, 27, 130, 5, app[1], app[2], app[3])
    if slot == 3:
        make_button(app[0], 25, 112, 27, 130, 5, app[1], app[2], app[3])
    if slot == 4:
        make_button(app[0], 165, 112, 27, 130, 5, app[1], app[2], app[3])
    if slot == 5:
        make_button(app[0], 25, 149, 27, 130, 5, app[1], app[2], app[3])
    if slot == 6:
        make_button(app[0], 165, 149, 27, 130, 5, app[1], app[2], app[3])
    if slot == 7:
        make_button(app[0], 25, 186, 27, 130, 5, app[1], app[2], app[3])
    if slot == 8:
        make_button(app[0], 165, 186, 27, 130, 5, app[1], app[2], app[3])

 def layout(self): 
   make_label('Owncloud', 20, 20, 47, cyan)
   ####Toggle switch#########################################################
   def switch():
     if config.Switch == 0: 
       config.Switch = 1
       os.system("sudo systemctl enable apache2")
       os.system("sudo service apache2 start")
     else:
       config.Switch = 0
       os.system("sudo systemctl disable apache2")
       os.system("sudo service apache2 stop")
     ###Rewriting file############################################################
     os.system('echo "Switch = ' + str(config.Switch) + '" > config.py')
     ##############################################################################
     clearall()
     Menu().layout()
   def state():
       if config.Switch == 0: return "Turn On"
       else: return "Turn Off"
   make_button(state(), 25, 75, 27, 130, 5, yellow, 24, switch)
   ##########################################################################
   #make_button('Allow Area Access', 165, 75, 27, 130, 5, yellow, 20, Areamod().load)
 
 def load(self):
   clearall()
   Menu().layout()
   #global back
   while 1:
      #if back == 1: break
      touchdisch() 
   #back = 0
   clearall()

menu = Menu()
menu.load()
