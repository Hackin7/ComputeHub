#Environment Config
#Run in Main Software directory as user pi and not as root

import os
import time
import datetime
path = '/mnt/Making/RaspberryPi/SittingFox/Software/' #path of Main Software folder from root

port = '1'
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-p', '--port', dest='Port', help='Port of VNC server')
parser.add_option('-t', '--state', dest='State', help='State of VNC server, whether  at launcher or in X desktop environment(0/1)')
parser.add_option('-s', '--switch', dest='Switch', help='start or stop VNC')
options, arguments = parser.parse_args()
if options.Port: port = options.Port

from PitftGraphicLib import *
#from virtualKeyboard import VirtualKeyboard

#import config
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
   def passs(): pass
   make_label('Environment', 20, 20, 47, cyan)
   make_button('Raspbian Desktop', 25, 75, 27, 130, 5, yellow, 20, Mode().Raspbian)
   make_button('Mobile Landscape', 165, 75, 27, 130, 5, green, 20, Mode().Mobilel)
   make_button('Mobile Portrait', 25, 112, 27, 130, 5, orange, 20, Mode().Mobilep)
   if options.State == '1':
     make_button('Clear and Logout', 25, 186, 27, 130, 5, red, 20, Mode().Restart)
     def back():
       global back
       back = 1
     make_button('Apps', 165, 186, 27, 130, 5, blue, 20, back)
    
 def check(self):
  while 1:
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break


class Mode:
  def __init__(self): pass

  def layout(self):
    clearall()
    make_label('Relogin!', 40, 60, 60, cyan)
    touchdisch()
    time.sleep(1)
    #clearall()
    #Menu().layout()

  def Restart(self):
    os.system('echo "#!/bin/sh" > ~/.vnc/xstartup')
    os.system('echo "cd '+path+'" >> ~/.vnc/xstartup')
    os.system('echo "python CloudComputing/Environment.py -t 0" >> ~/.vnc/xstartup')
    os.system('echo "#matchbox-window-manager" >> ~/.vnc/xstartup')
    os.system('vncserver -kill :'+port)
    os.system('vncserver  :'+port+' -geometry 320x240')
    exit()
    
  def Raspbian(self):
    Mode().layout()
    ###Rewriting file############################################################
    os.system('echo "#!/bin/sh" > ~/.vnc/xstartup')
    os.system('echo "#Raspbian Desktop Environment" >> ~/.vnc/xstartup')
    os.system('echo "xrdb $HOME/.Xresources" >> ~/.vnc/xstartup')
    os.system('echo "xsetroot -solid grey" >> ~/.vnc/xstartup')
    os.system('echo "python CloudComputing/Environment.py -t 1 &" >> ~/.vnc/xstartup')
    os.system('echo "#x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &" >> ~/.vnc/xstartup')
    os.system('echo "#x-window-manager &" >> ~/.vnc/xstartup')
    os.system('echo "# Fix to make GNOME work" >> ~/.vnc/xstartup')
    os.system('echo "export XKL_XMODMAP_DISABLE=1" >> ~/.vnc/xstartup')
    os.system('echo "/etc/X11/Xsession" >> ~/.vnc/xstartup')
    ##############################################################################
    os.system('vncserver -kill :'+port)
    os.system('vncserver :'+port)
    exit()

  def Mobilel(self):
    Mode().layout()
    ###Rewriting file############################################################
    os.system('echo "#!/bin/sh" > ~/.vnc/xstartup')
    os.system('echo "#Matchbox Mobile Environment 640x360" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-panel &" >> ~/.vnc/xstartup')
    os.system('echo "python CloudComputing/Environment.py -t 1 &" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-desktop &" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-window-manager" >> ~/.vnc/xstartup')
    ##############################################################################
    os.system('vncserver -kill :'+port)
    os.system('vncserver :'+port+' -geometry 640x360')
    exit()
  def Mobilep(self):
    Mode().layout()
    ###Rewriting file############################################################
    os.system('echo "#!/bin/sh" > ~/.vnc/xstartup')
    os.system('echo "#Matchbox Mobile Environment 640x360" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-desktop &" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-panel &" >> ~/.vnc/xstartup')
    os.system('echo "python CloudComputing/Environment.py -t 1 &" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-window-manager" >> ~/.vnc/xstartup')
    ##############################################################################
    os.system('vncserver -kill :'+port)
    os.system('vncserver :'+port+' -geometry 360x640')
    exit()  

import sys
sys.path.insert(0, path) 
import App
class ProgramsMenu():
 def __init__(self): pass
 
 # Slot Configuration
 def slotconf(self,slot, app):
    def setup(): app[3]()
    # 1st Row, 1st Column
    if slot == 1:
        make_button(app[0], 30, 30, 55, 95, 10, app[1], app[2], setup)
    # 1st Row, 2nd Column
    if slot == 2:
        make_button(app[0], 135, 30, 55, 95, 10, app[1], app[2], setup)
    # 2nd Row, 1st Column
    if slot == 3:
        make_button(app[0], 30, 100, 55, 95, 10, app[1], app[2], setup)
    if slot == 4:
        make_button(app[0], 135, 100, 55, 95, 10, app[1], app[2], setup)
    if slot == 5:
        make_button(app[0], 30, 170, 55, 95, 10, app[1], app[2], setup)
    if slot == 6:
        make_button(app[0], 135, 170, 55, 95, 10, app[1], app[2], setup)
 
 def layout(self):
  def exit(): 
    global back
    back = 1 
  def nextpage():
    clearall()
    global page
    page = page + 1
    ProgramsMenu().layout()
    global back
    while 1:
      touchdisch()
      if back == 1: break
    back = 0
    page = page - 1
    clearall()
    ProgramsMenu().layout()

  counter = 1
  while counter <= 6: #Maximun no. of slots
    if page*6+counter-1 >= len(App.programs): break #Stop at no. of programs
    ProgramsMenu().slotconf(counter, App.programs[page*6+counter-1])
    counter = counter + 1
  make_button('Back', 240, 30, 55, 70, 10, white, 24, exit)
  make_button('More', 240, 100, 55, 70, 10, white, 24, nextpage)
 
 def load(self):
   global page
   page = 0
   clearall()
   ProgramsMenu().layout()
   global back
   while 1:
     touchdisch()
     if back == 1: break
   back = 0

if options.Switch == 'start': 
  Mode().Restart()
elif options.Switch == 'stop':
  os.system('vncserver -kill :'+port)
  #os.system('pkill -f launch.sh')
  exit()

if options.State: 
  menu = Menu()
  screen = pygame.display.set_mode(size)
  initdis()
  while True:
    menu.layout()
    menu.check()
    ProgramsMenu().load()
    clearall()
