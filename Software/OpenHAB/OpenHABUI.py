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
                name = UIConfig().addlayout()
                if name != '': layout.floors.append(name)
                UIConfig().floors()
            elif mode == 1:
                name = UIConfig().addlayout()
                if name != '': layout.rooms.append((details[0],name))
                UIConfig().rooms(details[0])()
            elif mode == 2:
                name = UIConfig().addlayout()
                if name != '': layout.devices.append((details[0],details[1],name))
                UIConfig().devices(details[0],details[1])()
            MenuUI.back = 1
        def change(): UIConfig().selection(mode,details)
        make_button('+', 165, 30, 27, 30, 5, yellow, 24, add)
        make_button('Select', 205, 30, 27, 90, 5, blue, 24, change)
        #make_button('<>', 245, 30, 27, 50, 5, blue, 24, change)
      return func
    def addlayout(self):
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

    def selection(self,mode,details):
        counter = 1
        things = []
        if mode == 0:
                while counter <= len(layout.floors):
                  thing = layout.floors[counter-1]
                  thing = (thing,blue,20,UIConfig().select(0,counter,thing))
                  things.append(thing)
                  counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Select',yellow,things,passs)
                MenuUI.back = 0
                UIConfig().floors()
        elif mode == 1:
                while counter <= len(layout.rooms):
                  thing = layout.rooms[counter-1]
                  if thing[0] == details[0]:
                      thing = (thing[1],blue,20,UIConfig().select(1,counter,thing))
                      things.append(thing)
                  counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Select',yellow,things,passs)
                MenuUI.back = 0
                UIConfig().rooms(details[0])()
        elif mode == 2:
            while counter <= len(layout.devices):
              thing = layout.devices[counter-1]
              if (thing[0] == details[0]) and (thing[1] == details[1]):
                  thing = (thing[2],blue,20,UIConfig().select(2,counter,thing))
                  things.append(thing)
              counter = counter + 1
            MenuUI.menu.load(MenuUI.menu.slotconf,'Select',yellow,things,passs)
            MenuUI.back = 0
            UIConfig().devices(details[0],details[1])()
        MenuUI.back = 1
            
    def select(self,mode,position,details):
      def func():
        def interface(level,name,rename,remove,places,mover):
            clearall()
            make_label(level + ':', 40, 30, 60, cyan)
            def change():
                vkey = VirtualKeyboard(screen)
                newname = vkey.run(name)
                clearall()
                interface(level,newname,rename,remove,places,mover)
                check()
                rename(newname)
                MenuUI.back = 1
            def move():
                things = []
                counter = 1
                while counter <= places:
                    things.append((str(counter),blue,20,mover(counter)))
                    counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Move To',yellow,things,passs)
                MenuUI.back = 1
            make_button(name, 40, 85, 40, 240, 5, yellow, 40, change)
            make_button('Remove', 25, 139, 27, 130, 5, red, 25, remove)
            make_button('Move', 165, 139, 27, 130, 5, blue, 25, move)
            def exit(): MenuUI.back = 1
            MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
        def check():
            while 1: 
              touchdisch()
              if MenuUI.back == 1: break
        if mode == 0:
            def rename(renamed):
                layout.floors.pop(position-1)
                layout.floors.insert(position-1,renamed)
                UIConfig().rename(1,details,renamed)
            def remove():
                layout.floors.pop(position-1)
                UIConfig().remove(1,details)
                MenuUI.back = 1
            def move(place):
                def func():
                    layout.floors.pop(position-1)
                    layout.floors.insert(place-1,details)
                    MenuUI.back = 1
                return func
            interface('Floor',details,rename,remove,len(layout.floors),move)
            check()
        elif mode == 1:
            def rename(renamed):
                layout.rooms.pop(position-1)
                layout.rooms.insert(position-1,(details[0],renamed))
                UIConfig().rename(2,details,(details[0],renamed))
            def remove():
                layout.rooms.pop(position-1)
                UIConfig().remove(2,details)
                MenuUI.back = 1
            noplaces = 0
            things = []
            counter = 1
            while counter <= len(layout.rooms):
                thing = layout.rooms[counter-1]
                if thing[0] == details[0]:
                    noplaces = noplaces + 1
                    things.append(counter-1)
                counter = counter + 1
            def move(place):
                def func():
                    layout.rooms.pop(position-1)
                    layout.rooms.insert(things[place-1],details)
                    MenuUI.back = 1
                return func
            interface('Room',details[1],rename,remove,noplaces,move)
            check()
        elif mode == 2:
            def rename(renamed):
                layout.devices.pop(position-1)
                detail = list(details)
                detail.pop(2)
                detail.insert(2,renamed)
                layout.devices.insert(position-1,tuple(detail))
            def remove():
                layout.devices.pop(position-1)
                MenuUI.back = 1
            noplaces = 0
            things = []
            counter = 1
            while counter <= len(layout.devices):
                thing = layout.devices[counter-1]
                if (thing[0] == details[0]) and (thing[1] == details[1]):
                    noplaces = noplaces + 1
                    things.append(counter-1)
                counter = counter + 1
            def move(place):
                def func():
                    layout.devices.pop(position-1)
                    layout.devices.insert(place-1,details)
                    MenuUI.back = 1
                return func
            interface('Device',details[2],rename,remove,noplaces,move)
            check()
      return func

    def rename(self,mode,details,rename):
        counter = 1
        if mode == 1:
            oglist = tuple(layout.rooms)
            while counter <= len(oglist):
                thing = oglist[counter-1]
                if thing[0] == details:
                    layout.rooms.pop(counter-1)
                    renamed = list(thing)
                    renamed.pop(0)
                    renamed.insert(0,rename)
                    layout.rooms.insert(counter-1,tuple(renamed))
                    UIConfig().rename(2,thing,renamed)
                counter = counter + 1
        if mode == 2:
            oglist = tuple(layout.devices)
            while counter <= len(oglist):
              thing = oglist[counter-1]
              if (thing[0] == details[0]) and (thing[1] == details[1]):
                  layout.devices.pop(counter-1)
                  renamed = list(thing)
                  renamed.pop(0)
                  renamed.insert(0,rename[0])
                  renamed.pop(1)
                  renamed.insert(1,rename[1])
                  layout.devices.insert(counter-1,tuple(renamed))
              counter = counter + 1

    def remove(self,mode,details):
        counter = 1
        if mode == 1:
            oglist = tuple(layout.rooms)
            while counter <= len(oglist):
                thing = oglist[counter-1]
                if thing[0] == details:
                    layout.rooms.remove(thing)
                    UIConfig().remove(2,thing)
                counter = counter + 1
        if mode == 2:
            oglist = tuple(layout.devices)
            while counter <= len(oglist):
              thing = oglist[counter-1]
              if (thing[0] == details[0]) and (thing[1] == details[1]): layout.devices.remove(thing)
              counter = counter + 1
              
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
