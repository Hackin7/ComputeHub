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
    os.system('echo "mqtttopic ='+"'"+info.mqtttopic+"'"+' " >> '+directory+'info.py')
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
        def modtopic():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            info.mqtttopic = vkey.run(info.mqtttopic)
            mqttsetup()
            global returner
            returner = 1
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),(info.mqttbrokerurl,orange,20,modbroker),('',black,0,passs),(info.mqttport,orange,20,modport),('',black,0,passs),('',black,0,passs),('',black,0,passs),(info.mqtttopic,orange,20,modtopic)]
        def loadup():
            make_button('Own/Other Broker', 25, 75, 27, 270, 5, orange, 24, passs)
            backer()
            if MenuUI.page == 0:
                make_label('Broker URL:', 25, 112, 25, orange)
                make_label('Port:', 25, 149, 25, orange)
            if MenuUI.page == 1:
                make_label('Main Topic:', 25, 112, 25, orange)
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
            mode = (type,0,0,'Undefined')
            returner = 1
        return func
    types = [('Electrical Outlet',blue,20,typer('Electrical Outlet'))]
    initdis()
    MenuUI.menu.load(MenuUI.menu.slotconf,'Type',yellow,types,backer)
    disinitdis()
    return mode

alldevinfo = 0
moder = False
def deviceconnect():
    def wifispecific():
      global alldevinfo
      if alldevinfo[1] == 0:
        options = []
        def changeconfigmode():
            global alldevinfo
            dev = list(alldevinfo)
            dev.pop(1)
            dev.insert(1,(info.wifinetwork,info.wifipassword))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            wifispecific()
            global returner
            returner = 1
        def loadup():
          backer()
          make_button('General Config', 25, 75, 27, 270, 5, orange, 24, changeconfigmode)
      else:
        def modnetwork():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            global alldevinfo
            network = alldevinfo[1][0]
            dev = list(alldevinfo)
            wifi = list(dev[1])
            wifi.pop(0)
            wifi.insert(0,vkey.run(network))
            dev.pop(1)
            dev.insert(1,tuple(wifi))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            wifispecific()
            global returner
            returner = 1
        def modpassword():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            global alldevinfo
            password = alldevinfo[1][1]
            dev = list(alldevinfo)
            wifi = list(dev[1])
            wifi.pop(1)
            wifi.insert(1,vkey.run(password))
            dev.pop(1)
            dev.insert(1,tuple(wifi))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            wifispecific()
            global returner
            returner = 1
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),(alldevinfo[1][0],orange,20,modnetwork),('',black,0,passs),(alldevinfo[1][1],orange,20,modpassword)]
        def changeconfigmode():
            global alldevinfo
            dev = list(alldevinfo)
            dev.pop(1)
            dev.insert(1,0)
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            wifispecific()
            global returner
            returner = 1
        def loadup():
            backer()
            if MenuUI.page == 0:
                make_button('Specific Config', 25, 75, 27, 270, 5, orange, 24, changeconfigmode)
                make_label('Wifi Network:', 25, 112, 25, orange)
                make_label('Password:', 25, 149, 25, orange)
      MenuUI.menu.load(MenuUI.menu.slotconf,'Wifi',green,options,loadup)
    def mqttspecific():
      global alldevinfo
      if alldevinfo[2] == 0:
        options = []
        def changeconfigmode():
            global alldevinfo
            dev = list(alldevinfo)
            dev.pop(2)
            dev.insert(2,(info.mqttbrokerurl,info.mqttport,info.mqtttopic))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            mqttspecific()
            global returner
            returner = 1
        def loadup():
          backer()
          make_button('General Config', 25, 75, 27, 270, 5, orange, 24, changeconfigmode)
      else:
        def modbroker():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            global alldevinfo
            brokerurl = alldevinfo[2][0]
            dev = list(alldevinfo)
            mqtt = list(dev[2])
            mqtt.pop(0)
            mqtt.insert(0,vkey.run(brokerurl))
            dev.pop(2)
            dev.insert(2,tuple(mqtt))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            mqttspecific()
            global returner
            returner = 1
        def modport():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            global alldevinfo
            port = alldevinfo[2][1]
            dev = list(alldevinfo)
            mqtt = list(dev[2])
            mqtt.pop(1)
            mqtt.insert(1,vkey.run(port))
            dev.pop(2)
            dev.insert(2,tuple(mqtt))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            mqttspecific()
            global returner
            returner = 1
        def modtopic():
            screen = pygame.display.set_mode(size)
            vkey = VirtualKeyboard(screen)
            global alldevinfo
            port = alldevinfo[2][2]
            dev = list(alldevinfo)
            mqtt = list(dev[2])
            mqtt.pop(2)
            mqtt.insert(2,vkey.run(port))
            dev.pop(2)
            dev.insert(2,tuple(mqtt))
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            mqttspecific()
            global returner
            returner = 1
        def changeconfigmode():
            global alldevinfo
            dev = list(alldevinfo)
            dev.pop(2)
            dev.insert(2,0)
            global moder
            moder = tuple(dev)
            alldevinfo = tuple(dev)
            mqttspecific()
            global returner
            returner = 1
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),(alldevinfo[2][0],orange,20,modbroker),('',black,0,passs),(alldevinfo[2][1],orange,20,modport),('',black,0,passs),('',black,0,passs),('',black,0,passs),(alldevinfo[2][2],orange,20,modtopic)]
        def loadup():
            backer()
            make_button('Specific Config', 25, 75, 27, 270, 5, orange, 24, changeconfigmode)
            if MenuUI.page == 0:
                make_label('Broker URL:', 25, 112, 25, orange)
                make_label('Port:', 25, 149, 25, orange)
            if MenuUI.page == 1:
                make_label('Main Topic:', 25, 112, 25, orange)
      MenuUI.menu.load(MenuUI.menu.slotconf,'MQTT',green,options,loadup)
    def connection(ip):
        def loadup():
            backer()
            make_label('IP Address: '+ip, 25, 70, 25, yellow)
        options = [('',black,0,passs),('',black,0,passs),('Wifi',orange,20,wifispecific),('MQTT',green,20,mqttspecific)]
        MenuUI.menu.load(MenuUI.menu.slotconf,'Device',cyan,options,loadup)
    connection('192.168.1.8')

def devicemod(options):
    MenuUI.back = 0
    global moder
    global alldevinfo
    alldevinfo = options
    initdis()
    def interface():
       global alldevinfo
       def change():
           global moder
           global alldevinfo
           disinitdis()
           crap = devicesetup()
           initdis()
           if crap != False:
               moder = crap
               alldevinfo = moder
       make_label('Type:', 40, 15, 60, cyan)
       make_button(alldevinfo[0], 40, 70, 40, 240, 5, yellow, 40, change)
       make_button('Device Settings', 40, 130, 40, 240, 5, green, 40, deviceconnect)
       def exit(): MenuUI.back = 1
       MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
    def check():
        while 1:
            backer()
            clearall()
            interface()
            touchdisch()
            if MenuUI.back == 1: break
    check()
    disinitdis()
    return moder

def devicewrite(device,devicename,room,options):
    if options[0] == 'Electrical Outlet':
        return ('Switch item='+device+' icon"slider"','Switch '+device+' "'+devicename+'" ('+room+') {mqtt="<[broker:/'+info.mqtttopic+'/d:command:ON]"}')#>[broker:/'+info.mqtttopic+'/d:command:ON:ON],>[broker:/'+info.mqtttopic+'/d:command:OFF:OFF]"}')
    else:
        print 'No Config!'
        return ('','')

config = ('Stuff',mainsetup,devicesetup,devicemod,devicewrite)
