from PitftGraphicLib import *
import MenuUI
from virtualKeyboard import VirtualKeyboard
def passs(): pass
returner = 0
def backer():
    global returner
    if (returner == 1):
        if (MenuUI.page > 0):
           MenuUI.back = 1
        elif (MenuUI.page == 0):
           MenuUI.back = 1
           returner = 0

import info
def updateinfo():
    #####Set info#############################################################################
    directory = 'devicetypes/Stuff/'
    os.system('echo "#####General##########" > '+directory+'info.py')
    os.system('echo "wifinetwork = '+"'"+info.wifinetwork+"'"+'" >> '+directory+'info.py')
    os.system('echo "wifipassword = '+"'"+info.wifipassword+"'"+'" >> '+directory+'info.py')
    os.system('echo "mqttbrokerurl = '+"'"+info.mqttbrokerurl+"'"+'" >> '+directory+'info.py')
    os.system('echo "mqttport ='+"'"+info.mqttport+"'"+' " >> '+directory+'info.py')
    os.system('echo "######################" >> '+directory+'info.py')
    ##########################################################################################

def mainsetup():
    def wifisetup():
        def modnetwork():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.wifinetwork = vkey.run(info.wifinetwork)
            wifisetup()
            global returner
            returner = 1
        def modpassword():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.wifipassword = vkey.run(info.wifipassword)
            wifisetup()
            global returner
            returner = 1
        options = [('',black,0,passs),(info.wifinetwork,orange,20,modnetwork),('',black,0,passs),(info.wifipassword,orange,20,modpassword)]
        def loadup():
            backer()
            make_label('Wifi Network:', 25, 75, 25, orange)
            make_label('Password:', 25, 112, 25, orange)
        MenuUI.menu.load(MenuUI.menu.slotconf,'Wifi',green,options,loadup)
    def mqttsetup():
        def modbroker():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.mqttbrokerurl = vkey.run(info.mqttbrokerurl)
            mqttsetup()
            global returner
            returner = 1
        def modport():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.mqttport = vkey.run(info.mqttport)
            mqttsetup()
            global returner
            returner = 1
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),(info.mqttbrokerurl,orange,20,modbroker),('',black,0,passs),(info.mqttport,orange,20,modport)]
        def loadup():
            make_button('Own/Other Broker', 25, 75, 27, 270, 5, orange, 24, passs)
            backer()
            make_label('Broker URL:', 25, 112, 25, orange)
            make_label('Port:', 25, 149, 25, orange)
        MenuUI.menu.load(MenuUI.menu.slotconf,'MQTT',green,options,loadup)
    Settings = [('Wifi',yellow,24,wifisetup),('MQTT',yellow,20,mqttsetup)]
    def loadup():
        backer()
        make_label('Stuff Main Settings', 20, 20, 42, cyan)
    initdis()
    MenuUI.menu.load(MenuUI.menu.slotconf,'',black,Settings,loadup)
    updateinfo()
    disinitdis()

mode = False
def devicesetup():
    def typer(type):
        def func():
            global mode
            global returner
            mode = (type,0,0)
            returner = 1
        return func
    types = [('Electrical Outlet',blue,20,typer('Electrical Outlet'))]
    initdis()
    MenuUI.menu.load(MenuUI.menu.slotconf,'Type',yellow,types,backer)
    disinitdis()
    return mode

def deviceconnect(devinfo):
  def func():
    def wifispecific():
      if devinfo[1] == 0:
        options = []
        def loadup():
          backer()
          make_button('General Config', 25, 75, 27, 270, 5, orange, 24, passs)
      else:
        def modnetwork():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.wifinetwork = vkey.run(info.wifinetwork)
            wifispecific()
            global returner
            returner = 1
        def modpassword():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.wifipassword = vkey.run(info.wifipassword)
            wifispecific()
            global returner
            returner = 1
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),(info.wifinetwork,orange,20,modnetwork),('',black,0,passs),(info.wifipassword,orange,20,modpassword)]
        def loadup():
            backer()
            make_button('General Config', 25, 75, 27, 270, 5, orange, 24, passs)
            make_label('Wifi Network:', 25, 112, 25, orange)
            make_label('Password:', 25, 149, 25, orange)
      MenuUI.menu.load(MenuUI.menu.slotconf,'Wifi',green,options,loadup)
    def mqttspecific():
      if devinfo[1] == 0:
        options = []
        def loadup():
          backer()
      else:
        def modbroker():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.mqttbrokerurl = vkey.run(info.mqttbrokerurl)
            mqttspecific()
            global returner
            returner = 1
        def modport():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.mqttport = vkey.run(info.mqttport)
            mqttspecific()
            global returner
            returner = 1
        options = [('Specific/General',orange,24,passs),('Own/Other Broker',orange,24,passs),('',black,0,passs),(info.mqttbrokerurl,orange,20,modbroker),('',black,0,passs),(info.mqttport,orange,20,modport)]
        def loadup():
            backer()
            make_label('Broker URL:', 25, 112, 25, orange)
            make_label('Port:', 25, 149, 25, orange)
      MenuUI.menu.load(MenuUI.menu.slotconf,'MQTT',green,options,loadup)
    def connection(ip):
        def loadup():
            backer()
            make_label('IP Address: '+ip, 25, 70, 25, yellow)
        options = [('',black,0,passs),('',black,0,passs),('Wifi',orange,20,wifispecific),('MQTT',green,20,mqttspecific)]
        MenuUI.menu.load(MenuUI.menu.slotconf,'Device',cyan,options,loadup)
    connection('192.168.1.8')
  return func

moder = False
def devicemod(options):
    MenuUI.back = 0
    global moder
    initdis()
    def interface(config):
       def change():
           global moder
           disinitdis()
           crap = devicesetup()
           initdis()
           if crap != False:
               moder = crap
               interface(moder)
           else:
               interface(config)
       make_label('Type:', 40, 15, 60, cyan)
       make_button(config[0], 40, 70, 40, 240, 5, yellow, 40, change)
       make_button('Device Settings', 40, 130, 40, 240, 5, green, 40, deviceconnect(options))
       def exit(): MenuUI.back = 1
       MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
    def check():
        while 1:
            clearall()
            interface(options)
            touchdisch()
            if MenuUI.back == 1: break
    check()
    disinitdis()
    return moder

def devicewrite(device,devicename,room,options):
    return ('','')#(options+' item='+device+' icon"slider"',options+' '+device+' "'+devicename+'" ('+room+')')

config = ('Stuff',mainsetup,devicesetup,devicemod,devicewrite)
