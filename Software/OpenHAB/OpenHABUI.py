import os
from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()
import MenuUI
import devicetypes

def WebUI():
    disinitdis()
    os.system('FRAMEBUFFER=/dev/fb1 xinit ./WebUI.sh')
    initdis()

import layout
returner = 0
def backer():
    global returner
    if (returner == 1):
        if (MenuUI.page > 0):
           MenuUI.back = 1
        elif (MenuUI.page == 0):
           MenuUI.back = 1
           returner = 0
           
class UIConfig:
    def __init__(self): pass
    def mainmenu(self):
        MenuUI.menu.load(MenuUI.menu.slotconf,'Config',green,[('Structure',orange,20,UIConfig().home),('Device Types',orange,20,UIConfig().devtypesconfig)],backer)
    def addon(self,mode,*details):
      def func():
        backer()  
        def add():
            sett = UIConfig().addlayout()
            if sett[1] != '':
                if sett[0] == 0: #Group
                    counter = 1
                    highno = 0
                    while counter <= len(layout.groups):
                        print counter,highno,layout.groups[counter-1][1]
                        if layout.groups[counter-1][1] > highno: highno = layout.groups[counter-1][1]
                        counter = counter + 1
                    layout.groups.append((details[0],highno+1,sett[1])) 
                if sett[0] == 1: layout.devices.append((details[0],sett[1],'None','Empty')) #Device
            if mode == 0: UIConfig().home()
            elif mode == 1: UIConfig().groups(details[0],details[1])()
            global returner
            returner = 1
        def change(): UIConfig().selection(mode,details)
        make_button('+', 165, 30, 27, 30, 5, yellow, 24, add)
        make_button('Select', 205, 30, 27, 90, 5, blue, 24, change)
      return func
    def addlayout(self):
        global name
        name = ''
        global typeset
        typeset = 0
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
          def ok(type):
            def func():
              if name == '':
                  clearall()
                  make_label("Name Can't", 40, 60, 60, cyan)
                  make_label('be Blank', 40, 120, 60, cyan)
                  touchdisch()
                  time.sleep(1)
                  clearall()
                  layout()
                  return
              global typeset
              typeset = type
              MenuUI.back = 1
            return func
          MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
          make_button('Add Group', 165, 149, 27, 130, 5, white, 24, ok(0))
          MenuUI.menu.slotconf(8, ('Add Device', white, 24, ok(1)))
        layout()
        while 1: 
          touchdisch()
          if MenuUI.back == 1:
              MenuUI.back = 0
              return (typeset,name)

    def selection(self,mode,details):
        global returner
        counter = 1
        things = []
        if mode == 0:
                while counter <= len(layout.groups):
                  thing = layout.groups[counter-1]
                  if thing[0] == 0:
                      thing = (thing[2],blue,20,passs)#UIConfig().select(0,counter,thing))
                      things.append(thing)
                  counter = counter + 1
                counter = 1
                while counter <= len(layout.devices):
                  thing = layout.devices[counter-1]
                  if thing[0] == 0:
                      thing = (thing[1],blue,20,passs)#UIConfig().select(1,counter,thing))
                      things.append(thing)
                  counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Select',yellow,things,backer)
                MenuUI.back = 0
                returner = 0
                UIConfig().home()
        elif mode == 1:
                groupno = details[0]
                while counter <= len(layout.groups):
                  thing = layout.groups[counter-1]
                  if thing[0] == groupno:
                      thing = (thing[2],blue,20,passs)#UIConfig().select(0,counter,thing))
                      things.append(thing)
                  counter = counter + 1
                counter = 1
                while counter <= len(layout.devices):
                  thing = layout.devices[counter-1]
                  if thing[0] == groupno:
                      thing = (thing[1],blue,20,passs)#UIConfig().select(1,counter,thing))
                      things.append(thing)
                  counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Select',yellow,things,backer)
                MenuUI.back = 0
                returner = 0
                UIConfig().groups(details[0],details[1])()
        returner = 1
            
    def select(self,mode,position,details):
      def func():
        global returner
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
                MenuUI.menu.load(MenuUI.menu.slotconf,'Move To',yellow,things,backer)
                MenuUI.back = 1
            make_button(name, 40, 85, 40, 240, 5, yellow, 40, change)
            make_button('Remove', 25, 139, 27, 130, 5, red, 25, remove)
            #make_button('Move', 165, 139, 27, 130, 5, blue, 25, move)
            def exit():
                MenuUI.back = 1
            MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
        def check():
            while 1: 
              touchdisch()
              if MenuUI.back == 1: break
        if mode == 0:
            def rename(renamed):
                layout.floors.pop(position-1)
                layout.floors.insert(position-1,renamed)
            def remove():
                layout.floors.pop(position-1)
                UIConfig().remove(1,position)
                MenuUI.back = 1
            def move(place):
                def func():
                    layout.floors.pop(position-1)
                    layout.floors.insert(place-1,details)
                    returner = 1
                    MenuUI.back = 1
                return func
            interface('Group',details,rename,remove,len(layout.floors),move)
            check()
        elif mode == 1:
            def rename(renamed):
                layout.rooms.pop(position-1)
                layout.rooms.insert(position-1,(details[0],renamed))
            def remove():
                layout.rooms.pop(position-1)
                UIConfig().remove(2,(details[0],position))
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
                    returner = 1
                    MenuUI.back = 1
                return func
            interface('Room',details[1],rename,remove,noplaces,move)
            check()
        elif mode == 2:
            def rename(renamed):
                layout.devices.pop(position-1)
                detail = list(details)
                detail.pop(1)
                detail.insert(1,renamed)
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
                    returner = 1
                    MenuUI.back = 1
                return func
            interface('Device',details[2],rename,remove,noplaces,move)
            check()
        returner = 1
      return func

    def remove(self,mode,details):
        counter = 1
        if mode == 1:
            oglist = tuple(layout.rooms)
            while counter <= len(oglist):
                thing = oglist[counter-1]
                if thing[0] == details:
                    layout.rooms.remove(thing)
                    UIConfig().remove(2,(thing[0],counter))
                counter = counter + 1
        if mode == 2:
            oglist = tuple(layout.devices)
            while counter <= len(oglist):
              thing = oglist[counter-1]
              if (thing[0] == details[0]) and (thing[1] == details[1]): layout.devices.remove(thing)
              counter = counter + 1
              
    def home(self):
        counter = 1
        things = []
        while counter <= len(layout.groups):
          thing = layout.groups[counter-1]
          if thing[0] == 0:
              thing = (thing[2],orange,20,UIConfig().groups(thing[1],thing[2]))
              things.append(thing)
          counter = counter + 1
        counter = 1
        while counter <= len(layout.devices):
          thing = layout.devices[counter-1]
          if thing[0] == 0:
              thing = (thing[1],orange,20,UIConfig().devicemenu(0,counter,thing))
              things.append(thing)
          counter = counter + 1
        MenuUI.menu.load(MenuUI.menu.slotconf,'Home',green,things,UIConfig().addon(0,0))
        UIConfig().filerewrite()
    def groups(self,groupno,name):
      def func():
        counter = 1
        things = []
        while counter <= len(layout.groups):
          thing = layout.groups[counter-1]
          if thing[0] == groupno:
              thing = (thing[2],orange,20,UIConfig().groups(thing[1],thing[2]))
              things.append(thing)
          counter = counter + 1
        counter = 1
        while counter <= len(layout.devices):
          thing = layout.devices[counter-1]
          if thing[0] == groupno:
              thing = (thing[1],orange,20,UIConfig().devicemenu((groupno,name),counter,thing))
              things.append(thing)
          counter = counter + 1
        MenuUI.menu.load(MenuUI.menu.slotconf,name,green,things,UIConfig().addon(1,groupno,name))
      return func

    def devicemenu(self,group,position,device):
      def func():  
        def interface(name,type):
            clearall()
            make_label('Device:', 40, 30, 60, cyan)
            def rename(renamed):
                layout.devices.pop(position-1)
                detail = list(device)
                detail.pop(1)
                detail.insert(1,renamed)
                layout.devices.insert(position-1,tuple(detail))
            def change():
                vkey = VirtualKeyboard(screen)
                newname = vkey.run(device[1])
                rename(newname)
                clearall()
                interface(newname,type)
                check()
                MenuUI.back = 1
            def mode():
                def typer(mode):
                    def func():
                       layout.devices.pop(position-1)
                       detail = list(device)
                       detail.pop(2)
                       detail.insert(2,mode[0])
                       disinitdis()
                       options = mode[2]()
                       initdis()
                       if options != False:
                           detail.pop(3)
                           detail.insert(3,options)
                       layout.devices.insert(position-1,tuple(detail))
                       clearall()
                       interface(name,mode[0])
                       check()
                       global returner
                       returner = 1
                    return func
                counter = 1
                things = []
                while counter <= len(devicetypes.types):
                    thing = devicetypes.types[counter-1]
                    things.append((thing[0],blue,20,typer(thing)))
                    counter = counter + 1
                MenuUI.menu.load(MenuUI.menu.slotconf,'Type',yellow,things,backer)
                MenuUI.back = 1
            def op():
                counter = 1
                while counter <= len(devicetypes.types):
                    if devicetypes.types[counter-1][0] == type:
                        disinitdis()
                        options = devicetypes.types[counter-1][3](device[3])
                        if options != False:
                            layout.devices.pop(position-1)
                            detail = list(device)
                            detail.pop(3)
                            detail.insert(3,options)
                            layout.devices.insert(position-1,tuple(detail))
                        initdis()
                        interface(name,type)
                        check()
                        MenuUI.back = 1
                    counter = counter + 1
            make_button(name, 40, 85, 40, 240, 5, yellow, 40, change)
            make_button('Type: '+type, 25, 139, 27, 130, 5, red, 20, mode)
            make_button('Options', 165, 139, 27, 130, 5, red, 25, op)
            def exit(): MenuUI.back = 1
            MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
        def check():
            while 1: 
              touchdisch()
              if MenuUI.back == 1: break
        interface(device[1],device[2])
        check()
        MenuUI.back = 0
        if group == 0:
            UIConfig().home()
        else:
            UIConfig().groups(group[0],group[1])()
        global returner
        returner = 1
      return func

        
    def filerewrite(self):
        #####layout.py##########################################################################
        #####Groups#########################
        os.system('echo "groups = []" > layout.py')
        counter = 1
        while counter <= len(layout.groups):
          os.system('echo "groups.append('+str(layout.groups[counter-1])+')" >> layout.py')
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
        os.system('echo '+"'"+'sitemap home label="Home"'+"'"+' > /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo "{" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo " Frame {" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        counter = 1
        while counter <= len(layout.groups):
            if layout.groups[counter-1][0] == 0:
                os.system('echo '+"'"+'Group item='+'g'+str(layout.groups[counter-1][1])+' label="'+layout.groups[counter-1][2]+'" icon="hue"'+"'"+' >> /etc/openhab/configurations/sitemaps/main.sitemap')
            counter = counter + 1
        counter = 1
        while counter <= len(layout.devices):
             device = layout.devices[counter-1]
             devtypecounter = 1
             while devtypecounter <= len(devicetypes.types):
                 if (devicetypes.types[devtypecounter-1][0] == device[2]) & (device[0] == 0):
                     deviceadd = devicetypes.types[devtypecounter-1][4]('d'+str(counter-1),device[1],'g'+str(device[0]),device[3])
                     os.system('echo '+"'"+deviceadd[0]+"'"+' >> /etc/openhab/configurations/sitemaps/main.sitemap')
                 devtypecounter = devtypecounter + 1
             counter = counter + 1
        os.system('echo " }" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        os.system('echo "}" >> /etc/openhab/configurations/sitemaps/main.sitemap')
        #####Items##########################
        os.system('echo "" > /etc/openhab/configurations/items/main.items')
        counter = 1
        #####Group#####
        counter = 1
        while counter <= len(layout.groups):
          if layout.groups[counter-1][0] == 0:
              os.system('echo "Group '+'g'+str(layout.groups[counter-1][1])+'" >> /etc/openhab/configurations/items/main.items')
          else:
              os.system('echo '+"'"+'Group '+'g'+str(layout.groups[counter-1][1])+' "'+layout.groups[counter-1][2]+'" <video> ('+'g'+str(layout.groups[counter-1][0])+')'+"'"+' >> /etc/openhab/configurations/items/main.items')
          counter = counter + 1
        #####Devices####
        counter = 1
        while counter <= len(layout.devices):
             device = layout.devices[counter-1]
             devtypecounter = 1
             while devtypecounter <= len(devicetypes.types):
                 if devicetypes.types[devtypecounter-1][0] == device[2]:
                     deviceadd = devicetypes.types[devtypecounter-1][4]('d'+str(counter-1),device[1],'g'+str(device[0]),device[3])
                     os.system('echo '+"'"+deviceadd[1]+"'"+' >> /etc/openhab/configurations/items/main.items')
                 devtypecounter = devtypecounter + 1
             counter = counter + 1
        ################
        #while counter <= len(layout.rooms):
        #  os.system('echo '+"'"+'Group '+layout.rooms[counter-1][1]+' "'+layout.rooms[counter-1][1]+'" 	<video> ('+layout.rooms[counter-1][0]+')'+"'"+' >> /etc/openhab/configurations/items/main.items')
        #  counter = counter + 1
        #while counter <= len(layout.devices):
        #  os.system('echo '+"'"+layout.devices[counter-1][3]+' '+layout.devices[counter-1][2]+' "'+layout.devices[counter-1][2]+'" ('+layout.devices[counter-1][1]+')'+"'"+' >> /etc/openhab/configurations/items/main.items')
        #  counter = counter + 1
        #######################################################################################

    def devtypesconfig(self):
            def launch(thing):
              def func():
                disinitdis()
                thing[1]()
                initdis()
              return func
            counter = 1
            things = []
            while counter <= len(devicetypes.types):
                thing = devicetypes.types[counter-1]
                things.append((thing[0],orange,20,launch(thing)))
                counter = counter + 1
            MenuUI.menu.load(MenuUI.menu.slotconf,'Type',green,things,backer)

def passs(): pass #Debugging
mainmenu = (('WebUI', yellow, 24, WebUI),('Config', green, 24, UIConfig().mainmenu)) #Debugging
MenuUI.menu.load(MenuUI.menu.slotconf,'OpenHAB',cyan,mainmenu,backer)
