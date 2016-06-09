#CloudCom Config
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
   make_label('Cloud Computing', 20, 20, 47, cyan)
   make_button('VNC Computing', 25, 75, 27, 130, 5, yellow, 23, Com().load)
   #make_button('Storage', 165, 75, 27, 130, 5, green, 24, Storage().load)
    
   #Menu().slotconf(7, ('Back', white, 24, exit))
   #Menu().slotconf(8, ('Next', white, 24, nextpage))

 def check(self):
  while 1:
    touchdisch()

class Com:
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
   make_label('VNC Computing', 20, 20, 47, cyan)
   ####Toggle switch#########################################################
   def switch():
     if config.CloudCom == 0: config.CloudCom = 1
     else: config.CloudCom = 0
     ###Rewriting file############################################################
     os.system('echo "CloudCom = ' + str(config.CloudCom) + '" > config.py')
     os.system('echo "Storage = ' + str(config.Storage) + '" >> config.py')
     os.system('echo "Mntpoint = '+ str(config.Mntpoint) + '" >> config.py')
     ##############################################################################
     clearall()
     Com().layout()

   if config.CloudCom == 0: 
     state = "Turn On"
     os.system('su pi -c "vncserver -kill :1"')
     os.system('pkill -f launch.sh') 
   else: 
     state = "Turn Off"
     os.system('su pi -c "python Environment.py -s start"')
     os.system('pkill -f launch.sh')
     os.system('/home/pi/noVNC/utils/launch.sh --vnc localhost:5901 &')
   make_button(state, 25, 75, 27, 130, 5, yellow, 24, switch)
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
     Com().layout()  

   make_button('Change Password', 165, 75, 27, 130, 5, orange, 20, vncpass)
   
   def backer():
     global back
     back = 1
   make_button('Back', 25, 186, 27, 130, 5, white, 24, backer)
   
 def check(self):
  global back
  while 1:
    if back == 1: break
    touchdisch() 
  back = 0
 
 def load(self):
   clearall()
   Com().layout()
   Com().check()
   clearall()
   Menu().layout()

######Storage#################################################################
class Storage:
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
   make_label('Owncloud Storage', 20, 20, 47, cyan)
   ####Toggle switch#########################################################
   def switch():
     if config.Storage == 0: config.Storage = 1
     else: config.Storage = 0
     ###Rewriting file############################################################
     os.system('echo "CloudCom = ' + str(config.CloudCom) + '" > config.py')
     os.system('echo "Storage = ' + str(config.Storage) + '" >> config.py')
     os.system('echo "Mntpoint = '+ str(config.Mntpoint) + '" >> config.py')
     ##############################################################################
     clearall()
     Storage().layout()

   if config.Storage == 0: 
     state = "Turn On"
     os.system("sudo update-rc.d apache2 disable")
     os.system("sudo service apache2 stop")
   else:
     state = "Turn Off"
     os.system("sudo update-rc.d apache2 enable")
     os.system("sudo service apache2 start")
   make_button(state, 25, 75, 27, 130, 5, yellow, 24, switch)
   ##########################################################################
   #make_button('Allow Area Access', 165, 75, 27, 130, 5, yellow, 20, Areamod().load)

   def backer():
     global back
     back = 1
   make_button('Back', 25, 186, 27, 130, 5, white, 24, backer)
 
 def load(self):
   clearall()
   Storage().layout()
   global back
   while 1:
      if back == 1: break
      touchdisch() 
   back = 0
   clearall()
   Menu().layout()

###############################################################################
class Areamod:
   def __init__(self): pass
   
   def layout(self):
     make_label('Allow Area Access', 20, 20, 47, cyan)
     
     global user
     global area
     global disk
     
     def userch():
        global user
        vkey = VirtualKeyboard(screen)
        user = vkey.run(user)
        clearall()
        Areamod().layout()
     def areach():
        global area
        vkey = VirtualKeyboard(screen)
        area = vkey.run(area)
        clearall()
        Areamod().layout()
     def diskch():
        global disk
        vkey = VirtualKeyboard(screen)
        disk = vkey.run(disk)
        clearall()
        Areamod().layout()  

     make_label('User: ', 25, 75, 24, orange)
     make_button('', 25, 75,  27, 130, 5, black, 1, showusers().load)
     make_button(user, 165, 75, 27, 130, 5, orange, 24, userch)
      
     make_label('Area: ', 25, 112, 24, green)
     make_button(area, 165, 112, 27, 130, 5, green, 24, areach)
     
     make_label('Disk (if mounted): ', 25, 149, 20, blue)
     make_button(disk, 165, 149, 27, 130, 5, blue, 24, diskch)
     
     def backer():
       global back
       back = 1
     make_button('Back', 25, 186, 27, 130, 5, white, 24, backer)
     def give():
       def Alert(say,other):
         clearall()
         make_label(say, 40, 60, 60, cyan)
         make_label(other, 40, 120, 30, cyan)
         touchdisch()
         time.sleep(1)
         clearall()
         Areamod().layout() 

       global user
       global area
       global disk
   
       if user == '': Alert('No User','Given')
       elif area == '': Alert('No Area','Given')
       elif area[0] != '/': Alert('No Area','Given')
       else : 
         os.system('sudo ln -s '+ area + ' /Storage/Cloud/' + user + '/files/')#Symbolic Link
         Alert('Done!','Modify Link in Owncloud')

       if disk == '': Alert('No Disk','to be mounted') 
       elif disk[0] != '/': Alert('No Disk','to be mounted')
       else: pass 
     make_button('Give Access To', 165, 186, 27, 130, 5, yellow, 20, give)
        
   def load(self):
     clearall()
     #####Setup##############################################################
     global user
     global area
     global disk
     user = ''
     area = ''
     disk = ''
     ########################################################################
     Areamod().layout()
     global back
     while 1:
        if back == 1: break
        touchdisch() 
     back = 0
     clearall()
     Storage().layout()
 
class showusers:
  def __init__(self): pass
  
  def lineconf(self,slot,label):
      colour = yellow
      if slot == 1:
        make_label(label, 25, 75, 24, colour)
      if slot == 2:
        make_label(label, 25, 112, 24, colour)
      if slot == 3:
        make_label(label, 25, 149, 24, colour)
  
  def layout(self):
      make_label('Users', 20, 20, 47, cyan)
      #showusers().lineconf(1,'123456789012345678901234567890') #Each line takes exactly 30 characters # For Debugging
      #text = '123456789012345678901234567890a23456789012345678901234567890'+'123456789012345678901234567890a23456789012345678901234567890'
      #####List of users##########
      import subprocess
      userlist = subprocess.Popen(["ls","/Storage/Cloud"],stdout=subprocess.PIPE)
      text = userlist.stdout.read().decode()
      ############################
      line = 1
      while line <= 3: #Amount of lines in one page
        showusers().lineconf(line,text[0+(line*30-30)+(page*30*3):30+(line*30-30)+(page*30*3)])
        if 30+(line*30-30)+(page*30*3) > len(text): break
        line = line + 1
      
      def back():
        global back
        back = 1
      make_button('Back', 25, 186, 27, 130, 5, white, 24, back)
      def nxtpage():
        global page 
        page = page + 1
        clearall()
        showusers().layout() 
        global back
        while 1:
           if back == 1: break
           touchdisch() 
        back = 0
        page = page - 1
        clearall()
        showusers().layout()
      make_button('Next', 165, 186, 27, 130, 5, white, 24, nxtpage)

  def load(self):
    global page
    temp = page
    page = 0
    clearall()
    showusers().layout() 
    global back
    while 1:
       if back == 1: break
       touchdisch() 
    back = 0
    page = temp
    clearall()
    Areamod().layout()
##########################################################################################################

menu = Menu()
menu.layout()
menu.check()
