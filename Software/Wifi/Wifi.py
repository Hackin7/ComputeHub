#Wifi Config
#Run in directory and as root

import os
import time

from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()

import config
back = 0 
page = 0
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
   make_label('Wifi', 20, 20, 47, cyan)
   make_button('Connect mode', 25, 75, 27, 130, 5, yellow, 24, Mode().function1)
   make_button('Access Point mode', 165, 75, 27, 130, 5, green, 20, Mode().function2)
   make_button('Connection', 25, 112, 27, 130, 5, orange, 24, Connection)
   make_button('AP Settings', 165, 112, 27, 130, 5, blue, 24, APsettings().function)
    
   #Menu().slotconf(7, ('Back', white, 24, exit))
   #Menu().slotconf(8, ('Next', white, 24, nextpage))

 def check(self):
  while 1:
    touchdisch()

class Mode:
  def __init__(self): pass

  def layout(self,say,other):
    clearall()
    make_label(say, 40, 60, 60, cyan)
    make_label(other, 40, 120, 60, cyan)
    touchdisch()
    time.sleep(1)
    clearall()
    Menu().layout()

  def function1(self):
    os.system('sh ./Client.sh') #command
    ###Rewriting file############################################################
    os.system('echo "hostname = '+ "'" + config.hostname + "'" + '" > config.py')
    os.system('echo "password = '+ "'" + config.password + "'" + '" >> config.py')
    ##############################################################################
    Mode().layout('In Connect','Mode')

  def function2(self):
    os.system('sudo sh ./AP.sh ' + config.hostname + ' ' + config.password ) #command
    ###Rewriting file############################################################
    os.system('echo "hostname = '+ "'" + config.hostname + "'" + '" > config.py')
    os.system('echo "password = '+ "'" + config.password + "'" + '" >> config.py')
    ##############################################################################
    Mode().layout('In AP Mode!','')

def Connection():
  disinitdis()
  os.system('tap ./connection')
  os.system('echo "wpa_gui" >> ./connection')
  os.system('echo "(wpa_gui && pkill xinit) & " >> ./connection')
  os.system('echo "matchbox-window-manager" >> ./connection')
  os.system('FRAMEBUFFER=/dev/fb1 xinit ./connection')
  os.system('rm -rf ./connection')
  initdis()
  Menu().layout()  
  
class APsettings:
  def __init__(self): pass

  def layout(self):
    make_label('AP Settings', 20, 20, 47, cyan)
    make_label('Hostname:', 25, 75, 24, yellow)
    make_label('Password:', 165, 75, 24, green)
    make_button(config.hostname, 25, 112, 27, 130, 5, yellow, 24, APsettings().hostname)
    make_button(config.password, 165, 112, 27, 130, 5, green, 24, APsettings().password)
    make_label('Must be input correctly for AP to function', 25, 149, 20, white)
    def exit(): 
      global back
      back = 1 
    make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
  
  def function(self):
    clearall()
    APsettings().layout()
    global back
    while True:
      touchdisch()
      if back == 1: 
        back = 0
        break
    ###Rewriting file############################################################
    os.system('echo "hostname = '+ "'" + config.hostname + "'" + '" > config.py')
    os.system('echo "password = '+ "'" + config.password + "'" + '" >> config.py')
    ##############################################################################
    clearall()
    Menu().layout()
  def hostname(self):
    vkey = VirtualKeyboard(screen)
    config.hostname = vkey.run(config.hostname)
    clearall()
    APsettings().layout()
  def password(self):
    vkey = VirtualKeyboard(screen)
    config.password = vkey.run(config.password)
    clearall()
    APsettings().layout()

menu = Menu()
menu.layout()
menu.check()
