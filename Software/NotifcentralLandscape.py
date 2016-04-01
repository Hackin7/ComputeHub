#Notifcentral Landscape for SittingFox

# setup       Launch command &, kill command,
enviroment = ('sleep 1')#'kodi --standalone &','pkill kodi')

import os
#Time Date check
import time
import datetime
#Button Setup
import RPi.GPIO as gpio
button = 23 #GPIO pin for button
gpio.setmode(gpio.BCM)
gpio.setup(button,gpio.IN,pull_up_down=gpio.PUD_UP)
#Buzzer Setup (disable I2C pins)
gpio.setup(17,gpio.OUT)

from PitftGraphicLib import *
initdis()


import App
import Services
Services.setup()
prev = len(Services.notif)

back = 0 
page = 0
class Menu:
 def __init__(self): pass
      
 # Slot Configuration
 def slotconf(self,slot, app):
    def rm(): 
      disinitdis()
      app[3]()
      Services.notif.remove(app)
      initdis()
    if slot == 1:
        make_button(app[0], 25, 75, 27, 270, 5, app[1], app[2], rm)
    if slot == 2:
        make_button(app[0], 25, 112, 27, 270, 5, app[1], app[2], rm)
    if slot == 3:
        make_button(app[0], 25, 149, 27, 270, 5, app[1], app[2], rm)
    #if slot == 2:
    #    make_button(app[0], 165, 75, 27, 130, 5, app[1], app[2], rm)
    #if slot == 4:
    #    make_button(app[0], 165, 112, 27, 130, 5, app[1], app[2], rm)
    #if slot == 6:
    #    make_button(app[0], 165, 149, 27, 130, 5, app[1], app[2], rm)
    
 def layout(self): 
   #Time and date 
   #global time
   time = datetime.datetime.now().time()
   make_label(str(time)[0:8], 20, 20, 47, cyan) #'10:30 am'
   date = datetime.date.today()
   make_label(date, 160, 30, 32, green) #'16/5/2015'
   
   def exit(): 
     global back
     back = 1 
     #if page == 0: back = 0
   def nextpage():
     clearall()
     global page
     page = page + 1
     Menu().layout()
     #global back
     Menu().check()
     #back = 0
     page = page - 1
     clearall()
     Menu().layout()
   counter = 1  
   while counter <= 3: #Maximun no. of slots
     if page*3+counter-1 >= len(Services.notif): break #Stop at no. of programs
     Menu().slotconf(counter, Services.notif[page*3+counter-1])
     counter = counter + 1

   make_button('Back', 25, 186, 27, 82, 5, white, 24, exit)
   make_button('Programs', 117, 186, 27, 82, 5, white, 23, ProgramsMenu().load)
   make_button('Next', 209, 186, 27, 85, 5, white, 24, nextpage)
   #Menu().slotconf(7, ('Back', white, 24, exit))
   #Menu().slotconf(8, ('Next', white, 24, nextpage))

 def check(self):
  while 1:
    touchdisch()
    #Notification/Service check
    Menu().service(disinitdis,initdis,Menu().layout)
    #Timedate check and notif update check
    if str(time)[0:8] != str(datetime.datetime.now().time())[0:8]: 
      clearall()  
      Menu().layout()
    global back
    if back == 1: 
      back = 0
      break
    
 def service(self,setup,unsetup,layout):
   Services.check()
   #Service check
   if len(Services.service) != 0:
    setup()
    Services.service[0]()
    Services.service.remove(Services.service[0]) 
    unsetup()
    layout()
   global prev
   if prev < len(Services.notif): 
     gpio.output(17,1)
     time.sleep(1)
     gpio.output(17,0)
   prev = len(Services.notif)
  
class ProgramsMenu():
 def __init__(self): pass
 
 # Slot Configuration
 def slotconf(self,slot, app):
    def setup():
      disinitdis()
      app[3]()
      def passs(): pass
      while True:
       Menu().service(app[4],app[3],passs)
       #Menu().service(killprogram,app[3],passs)
       if not gpio.input(button):
         app[4]()
         break 
      initdis()
      ProgramsMenu().layout()
    # 1st Row, 1st Column
    if slot == 1:
        make_button(app[0], 30, 30, 55, 95, 10, app[1], app[2], setup)
    # 1st Row, 2nd Column
    if slot == 2:
        make_button(app[0], 135, 30, 55, 95, 10, app[1], app[2], setup)
    # 2nd Row, 1st Column
    if slot == 3:
        make_button(app[0], 30, 100, 55, 95, 10, app[1], app[2], setup)
    if slot == 4:
        make_button(app[0], 135, 100, 55, 95, 10, app[1], app[2], setup)
    if slot == 5:
        make_button(app[0], 30, 170, 55, 95, 10, app[1], app[2], setup)
    if slot == 6:
        make_button(app[0], 135, 170, 55, 95, 10, app[1], app[2], setup)
 
 def layout(self):
  def exit(): 
    global back
    back = 1 
  def nextpage():
    clearall()
    global page
    page = page + 1
    ProgramsMenu().layout()
    global back
    while 1:
      Menu().service(disinitdis,initdis,ProgramsMenu().layout)
      touchdisch()
      if back == 1: break
    back = 0
    page = page - 1
    clearall()
    ProgramsMenu().layout()

  counter = 1
  while counter <= 6: #Maximun no. of slots
    if page*6+counter-1 >= len(App.programs): break #Stop at no. of programs
    ProgramsMenu().slotconf(counter, App.programs[page*6+counter-1])
    counter = counter + 1
  make_button('Back', 240, 30, 55, 70, 10, white, 24, exit)
  make_button('More', 240, 100, 55, 70, 10, white, 24, nextpage)
 
 def load(self):
   global page
   page = 0
   clearall()
   ProgramsMenu().layout()
   global back
   while 1:
     touchdisch()
     Menu().service(disinitdis,initdis,ProgramsMenu().layout)
     if back == 1: break
   back = 0
   clearall()
   Menu().layout()


code = '6969'
class Clock:
 def __init__(self): pass
 def layout(self): 
   #Time and date 
   #global time
   time = datetime.datetime.now().time()
   make_label(str(time)[0:8], 40, 60, 90, cyan) #'10:30 am'
   date = datetime.date.today()
   make_label(date, 160, 30, 32, green) #'16/5/2015'
 def check(self):
  while 1:
    touchdisch()
    ##Notification/Service check
    Menu().service(disinitdis,initdis,Menu().layout)
    #Timedate check and notif update check
    if str(time)[0:8] != str(datetime.datetime.now().time())[0:8]: 
      clearall()  
      Clock().layout()
    if not gpio.input(button):
         os.system(enviroment[1])
         #clearall()
         #Menu().layout()
         #Menu().check()
         Clock().pininput()
         os.system(enviroment[0])
         Clock().layout()

 def pininput(self):
  global code
  global pin
  pin = ''
  def layout():
    clearall()
    def input(insert): 
      global pin
      pin = pin+insert
      clearall()
      layout()
    def de():
      global pin
      pin = pin[:len(pin)-1]
      clearall()
      layout()
    def one(): input('1')
    def two(): input('2')
    def three(): input('3')
    def four(): input('4')
    def five(): input('5')
    def six(): input('6')
    def seven(): input('7')
    def eight(): input('8')
    def nine(): input('9')
    def zero(): input('0')

    time = datetime.datetime.now().time()
    make_label(str(time)[0:8], 20, 30, 50, cyan)
    make_label(datetime.date.today(), 20, 75, 32, green) #'16/5/2015'
     
    def change():pass
    make_button(pin, 175, 35, 35, 95, 5, yellow, 40, change)
    make_button('Del', 270, 35, 35, 35, 5, red, 25, de)
    make_button('1', 175, 83, 35, 35, 5, green, 40, one)
    make_button('2', 223, 83, 35, 35, 5, green, 40, two)
    make_button('3', 270, 83, 35, 35, 5, green, 40, three)
    make_button('4', 175, 131, 35, 35, 5, green, 40, four)
    make_button('5', 223, 131, 35, 35, 5, green, 40, five)
    make_button('6', 270, 131, 35, 35, 5, green, 40, six)
    make_button('7', 175, 178, 35, 35, 5, green, 40, seven)
    make_button('8', 223, 178, 35, 35, 5, green, 40, eight)
    make_button('9', 270, 178, 35, 35, 5, green, 40, nine)
    make_button('0', 128, 178, 35, 35, 5, green, 40, zero)

    def exit():
      global back
      back = 1
    make_button('Back', 25, 186, 27, 90, 5, white, 24, exit)
 
  layout()
  while 1: 
    touchdisch()
    global back
    ##Notification/Service check
    Menu().service(disinitdis,initdis,Menu().layout)
    #Timedate check and notif update check
    if str(time)[0:8] != str(datetime.datetime.now().time())[0:8]: 
      clearall()  
      layout()
    if pin == code:
       clearall()
       Menu().layout()
       Menu().check()
       break
    if back == 1: 
      back = 0
      break
  clearall()

os.system(enviroment[0])
clock = Clock() #Menu()
clock.layout()
clock.check()
