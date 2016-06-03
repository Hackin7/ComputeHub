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
print os.getcwd()
import info
prevmqtturl = info.mqttbrokerurl + ':' + info.mqttport
def updateinfo():
    #####Infofile#############################################################################
    directory = 'devicetypes/Stuff/'
    os.system('echo "#####General##########" > '+directory+'info.py')
    os.system('echo "wifinetwork = '+"'"+info.wifinetwork+"'"+'" >> '+directory+'info.py')
    os.system('echo "wifipassword = '+"'"+info.wifipassword+"'"+'" >> '+directory+'info.py')
    os.system('echo "mqttlocalext = '+str(info.mqttlocalext)+'" >> '+directory+'info.py')
    os.system('echo "mqttbrokerurl = '+"'"+info.mqttbrokerurl+"'"+'" >> '+directory+'info.py')
    os.system('echo "mqttport ='+"'"+info.mqttport+"'"+' " >> '+directory+'info.py')
    os.system('echo "mqtttopic ='+"'"+info.mqtttopic+"'"+' " >> '+directory+'info.py')
    os.system('echo "devhighestcounter = '+str(info.devhighestcounter)+'" >> '+directory+'info.py')
    os.system('echo "######################" >> '+directory+'info.py')
    ##########################################################################################
    global prevmqtturl
    print prevmqtturl
    os.system('cat /etc/openhab/configurations/openhab_default.cfg > /etc/openhab/configurations/openhab_default.cfg.bak')
    os.system('sed s#mqtt:broker.url=tcp://'+prevmqtturl+'#mqtt:broker.url=tcp://'+info.mqttbrokerurl+':'+info.mqttport+'#g /etc/openhab/configurations/openhab_default.cfg.bak > /etc/openhab/configurations/openhab_default.cfg')

def mainsetup():
    global prevmqtturl
    prevmqtturl = info.mqttbrokerurl + ':' + info.mqttport
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
          if info.mqttlocalext == 0: pass
          else:
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
            if info.mqttlocalext == 0:
                def change(): info.mqttlocalext = 1
                make_button('Local Broker', 25, 75, 27, 270, 5, orange, 24, change)
            if info.mqttlocalext == 1:
                def change():
                    info.mqttlocalext = 0
                    info.mqttbrokerurl = 'localhost'
                    mqttsetup()
                    global returner
                    returner = 1
                make_button('External Broker', 25, 75, 27, 270, 5, orange, 24, change)
            backer()
            if MenuUI.page == 0:
                make_label('Broker URL:', 25, 112, 25, orange)
                make_label('Port:', 25, 149, 25, orange)
            if MenuUI.page == 1:
                make_label('Main Topic:', 25, 112, 25, orange)
        MenuUI.menu.load(MenuUI.menu.slotconf,'MQTT',green,options,loadup)
    Settings = [('MQTT',yellow,20,mqttsetup)]#('Wifi',yellow,24,wifisetup),
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
            info.devhighestcounter = info.devhighestcounter+1
            updateinfo()
            global mode
            global returner
            mode = (type,info.devhighestcounter)
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
    def connection():
        def loadup():
            backer()
            global alldevinfo
            make_label('Device No: '+str(alldevinfo[1]), 25, 70, 25, yellow)
        options = []
        MenuUI.menu.load(MenuUI.menu.slotconf,'Device',cyan,options,loadup)
    connection()

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
       make_button('Device No:'+str(alldevinfo[1]), 40, 130, 40, 240, 5, green, 40, passs)#deviceconnect)
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
        return ('Switch item='+device+' icon"slider"','Switch '+device+' "'+devicename+'" ('+room+') {mqtt="<[broker:/'+info.mqtttopic+'/d'+str(options[1])+':command:EXEC(python '+os.getcwd()+'/devicetypes/Stuff/Commands.py -d 0 -c %s)],>[broker:/'+info.mqtttopic+'/d'+str(options[1])+':command:ON:output.on],>[broker:/'+info.mqtttopic+'/d'+str(options[1])+':command:OFF:output.off]"}')
    else:
        print 'No Config!'
        return ('','')

config = ('Stuff',mainsetup,devicesetup,devicemod,devicewrite)
