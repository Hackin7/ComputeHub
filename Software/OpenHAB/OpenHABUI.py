import os
from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()
import MenuUI

def WebUI():
    disinitdis()
    os.system('FRAMEBUFFER=/dev/fb1 xinit ./WebUI.sh')
    initdis()

import layout
class UIConfig:
    def __init__(self): pass
    def addon(self,mode,*details):
      def func():  
        def add():
            if mode == 0:
                name = UIConfig().add()
                if name != '': layout.floors.append(name)
                UIConfig().floors()
            elif mode == 1:
                name = UIConfig().add()
                if name != '': layout.rooms.append((details[0],name))
                UIConfig().rooms(details[0])()
            MenuUI.back = 1
        def change(): pass
        make_button('+', 165, 30, 27, 30, 5, yellow, 24, add)
        make_button('-', 205, 30, 27, 30, 5, yellow, 24, add)
        make_button('<>', 245, 30, 27, 50, 5, blue, 24, change)
      return func
    def add(self):
        global name
        name = ''
        def change():
            vkey = VirtualKeyboard(screen)
            global name
            name = vkey.run(name)
            clearall()
            layout()
        def layout():
          global name
          clearall()
          make_label('Name:', 40, 40, 60, cyan)
          make_button(name, 40, 100, 40, 240, 5, yellow, 40, change)
          def exit():
            global name
            name = ''
            MenuUI.back = 1
          def ok():
              if name == '':
                  clearall()
                  make_label("Name Can't", 40, 60, 60, cyan)
                  make_label('be Blank', 40, 120, 60, cyan)
                  touchdisch()
                  time.sleep(1)
                  clearall()
                  layout()
                  return
              MenuUI.back = 1
          MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
          MenuUI.menu.slotconf(8, ('Add', white, 24, ok))
        layout()
        while 1: 
          touchdisch()
          if MenuUI.back == 1:
              MenuUI.back = 0
              return name
    def floors(self):
        counter = 1
        things = []
        while counter <= len(layout.floors):
          thing = layout.floors[counter-1]
          thing = (thing,orange,20,UIConfig().rooms(thing))
          things.append(thing)
          counter = counter + 1
        MenuUI.menu.load(MenuUI.menu.slotconf,'Floors',green,things,UIConfig().addon(0))
        UIConfig().filerewrite()
    def rooms(self,floor):
      def func():
        counter = 1
        things = []
        while counter <= len(layout.rooms):
          thing = layout.rooms[counter-1]
          if thing[0] == floor:
              thing = (thing[1],orange,20,UIConfig().devices(floor,thing[1]))
              things.append(thing)
          counter = counter + 1
        MenuUI.menu.load(MenuUI.menu.slotconf,'Rooms',green,things,UIConfig().addon(1,floor))
      return func
    def devices(self,floor,room):
      def func():
        counter = 1
        things = []
        while counter <= len(layout.devices):
          thing = layout.devices[counter-1]
          if (thing[0] == floor) and (thing[1] == room):
              thing = (thing[2],orange,20,passs)
              things.append(thing)
          counter = counter + 1
        MenuUI.menu.load(MenuUI.menu.slotconf,'Devices',green,things,UIConfig().addon(2,floor,room))
      return func
    def filerewrite(self):
        #####layout.py##########################################################################
        #####Floors#########################
        os.system('echo "floors = []" > layout.py')
        counter = 1
        while counter <= len(layout.floors):
          os.system('echo "floors.append('+"'"+layout.floors[counter-1]+"'"+')" >> layout.py')
          counter = counter + 1
        #####Rooms##########################
        os.system('echo "rooms = []" >> layout.py')
        counter = 1
        while counter <= len(layout.rooms):
          os.system('echo "rooms.append('+str(layout.rooms[counter-1])+')" >> layout.py')
          counter = counter + 1
        #####Devices###########################
        os.system('echo "devices = []" >> layout.py')
        counter = 1
        while counter <= len(layout.devices):
          os.system('echo "devices.append('+str(layout.devices[counter-1])+')" >> layout.py')
          counter = counter + 1
        #######################################################################################
        #####OpenHAB Config####################################################################
        #####Sitemaps#######################
        os.system('echo '+"'"+'sitemap home label="My Home"'+"'"+' > /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo "{" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo " Frame {" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        counter = 1
        while counter <= len(layout.floors):
          os.system('echo '+"'"+'Group item='+layout.floors[counter-1]+' label="'+layout.floors[counter-1]+'" icon="hue"'+"'"+' >> /etc/openhab/configurations/sitemaps/main.sitemap')
          counter = counter + 1
        os.system('echo " }" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo "}" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        #####Items##########################
        os.system('echo "" > /etc/openhab/configurations/items/main.items')
        counter = 1
        while counter <= len(layout.floors):
          os.system('echo "Group '+layout.floors[counter-1]+'" >> /etc/openhab/configurations/items/main.items')
          counter = counter + 1
        counter = 1
        while counter <= len(layout.rooms):
          os.system('echo '+"'"+'Group '+layout.rooms[counter-1][1]+' "'+layout.rooms[counter-1][1]+'" 	<video> ('+layout.rooms[counter-1][0]+')'+"'"+' >> /etc/openhab/configurations/items/main.items')
          counter = counter + 1
        #######################################################################################

def passs(): pass #Debugging
mainmenu = (('WebUI', yellow, 24, WebUI),('UI config', green, 24, UIConfig().floors)) #Debugging
MenuUI.menu.load(MenuUI.menu.slotconf,'OpenHAB',cyan,mainmenu,passs)
