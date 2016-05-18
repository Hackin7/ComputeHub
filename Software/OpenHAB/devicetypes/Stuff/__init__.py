from PitftGraphicLib import *
import MenuUI
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

def mainsetup():
    def mqttsetup():
        print('lol it doesnt work as if')
        def passs():pass
        options = [('',black,0,passs),('',black,0,passs),('',black,0,passs),('URL',yellow,20,passs),('',black,0,passs),('Port',yellow,20,passs)]
        def loadup():
            backer()
        MenuUI.menu.load(MenuUI.menu.slotconf,'MQTT',yellow,options,loadup)
    Settings = [('MQTT',blue,20,mqttsetup)]
    initdis()
    MenuUI.menu.load(MenuUI.menu.slotconf,'Stuff',yellow,Settings,backer)
    disinitdis()

mode = False
def devicesetup():
    def typer(type):
        def func():
            global mode
            global returner
            mode = type
            returner = 1
        return func
    types = [('Electrical Outlet',blue,20,typer('Electrical Outlet'))]
    initdis()
    MenuUI.menu.load(MenuUI.menu.slotconf,'Type',yellow,types,backer)
    disinitdis()
    return mode

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
       make_button(config, 40, 70, 40, 240, 5, yellow, 40, change)
       make_button('Device Settings', 40, 130, 40, 240, 5, orange, 40, change)
       def exit(): MenuUI.back = 1
       MenuUI.menu.slotconf(7, ('Back', white, 24, exit))
    interface(options)
    def check():
        while 1:
            touchdisch()
            if MenuUI.back == 1: break
    check()
    disinitdis()
    return moder

def devicewrite(device,devicename,room,options):
    return (options+' item='+device+' icon"slider"',options+' '+device+' "'+devicename+'" ('+room+')')

config = ('Stuff',mainsetup,devicesetup,devicemod,devicewrite)
