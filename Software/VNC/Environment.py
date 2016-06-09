#Environment Config
#Run in Main Software directory as user pi and not as root
def passs(): pass
import os
import time
import datetime
path = os.getcwd()

port = '1'
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-p', '--port', dest='Port', help='Port of VNC server')
parser.add_option('-t', '--state', dest='State', help='State of VNC server, whether  at launcher or in X desktop environment(0/1)')
parser.add_option('-s', '--switch', dest='Switch', help='start or stop VNC')
options, arguments = parser.parse_args()
if options.Port: port = options.Port

from PitftGraphicLib import *
def Menu():
 initdis()
 import MenuUI
 mainmenu = (('Clear and Restart', red, 20, Mode().Restart),
             ('Raspbian Desktop', yellow, 20, Mode().Raspbian),
             ('Mobile Landscape', green, 20, Mode().Mobilel),
             ('Mobile Portrait', orange, 20, Mode().Mobilep),)
 MenuUI.menu.load(MenuUI.menu.slotconf,'Environment',cyan,mainmenu,passs)

class Mode:
  def __init__(self): pass
  
  def layout(self):
    clearall()
    make_label('Relogin!', 40, 60, 60, cyan)
    touchdisch()
    time.sleep(1)
    
  def Restart(self):
    print('Restart')
    os.system('echo "#!/bin/sh" > ~/.vnc/xstartup')
    os.system('echo "cd '+path+'" >> ~/.vnc/xstartup')
    os.system('echo "python Environment.py -t 0" >> ~/.vnc/xstartup')
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
    os.system('echo "python Environment.py -t 1 &" >> ~/.vnc/xstartup')
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
    os.system('echo "python Environment.py -t 1 &" >> ~/.vnc/xstartup')
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
    os.system('echo "python Environment.py -t 1 &" >> ~/.vnc/xstartup')
    os.system('echo "matchbox-window-manager" >> ~/.vnc/xstartup')
    ##############################################################################
    os.system('vncserver -kill :'+port)
    os.system('vncserver :'+port+' -geometry 360x640')
    exit()  

if options.Switch == 'start': Mode().Restart()
elif options.Switch == 'stop':os.system('vncserver -kill :'+port)
else:
    while True: Menu()
