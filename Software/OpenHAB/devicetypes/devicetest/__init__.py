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


def mainsetup(): print 'No Config Required!'

mode = False
def devicesetup():
    def typer(type):
        def func():
            global mode
            global returner
            mode = type
            returner = 1
        return func
    types = [('Call',blue,20,typer('Call')),
             ('Color',blue,20,typer('Color')),
             ('Contact',blue,20,typer('Contact')),
             ('DateTime',blue,20,typer('DateTime')),
             ('Dimmer',blue,20,typer('Dimmer')),
             ('Group',blue,20,typer('Group')),
             ('Location',blue,20,typer('Location')),
             ('Number',blue,20,typer('Number')),
             ('Rollershutter',blue,20,typer('Rollershutter')),
             ('String',blue,20,typer('String')),
             ('Switch',blue,20,typer('Switch'))]
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
       make_label('Type:', 40, 30, 60, cyan)
       make_button(config, 40, 85, 40, 240, 5, yellow, 40, change)
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
    return options+' '+device+' "'+devicename+'" ('+room+')'

config = ('DeviceTest',mainsetup,devicesetup,devicemod,devicewrite)
