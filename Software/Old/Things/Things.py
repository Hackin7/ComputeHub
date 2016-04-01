#Things Menu
#Install the BlockComPi software in /home/pi first

import os
import sys
import subprocess
#Time Date check
import time
import datetime
from PitftGraphicLib import *
from virtualKeyboard import VirtualKeyboard
screen = pygame.display.set_mode(size)
initdis()

import Config

back = 0 
page = 0

class Menu:
 def __init__(self): pass
      
 # Slot Configuration
 def slotconf(self,slot, app, item):
    if item == 1:
      colour = yellow
      font = app[1]
      def run(): Control().load(app)
    else:
      colour = app[1]
      font = app[2]
      run = app[3]
    if slot == 1:
        make_button(app[0], 25, 75, 27, 130, 5, colour, font, run)
    if slot == 2:
        make_button(app[0], 165, 75, 27, 130, 5, colour, font, run)
    if slot == 3:
        make_button(app[0], 25, 112, 27, 130, 5, colour,  font, run)
    if slot == 4:
        make_button(app[0], 165, 112, 27, 130, 5, colour, font, run)
    if slot == 5:
        make_button(app[0], 25, 149, 27, 130, 5, colour, font, run)
    if slot == 6:
        make_button(app[0], 165, 149, 27, 130, 5, colour, font, run)
    if slot == 7:
        make_button(app[0], 25, 186, 27, 130, 5, colour, font, run)
    if slot == 8:
        make_button(app[0], 165, 186, 27, 130, 5, colour, font, run)

 def layout(self): 
   make_label("Things", 20, 20, 47, cyan)
   def exit(): 
     global back
     back = 1 
     if page == 0: back = 0
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
   def passs(): pass
   if page == 0:
     Menu().slotconf(1, ('Rooms', green, 24, Rooms().load),0)
     #Menu().slotconf(2, ('IOT', orange, 24, IOT().load),0)
     Menu().slotconf(2, ('IFTTT', orange, 24, IOT().IFTTTload),0)
     Menu().slotconf(3, ('Monitoring', yellow, 24, Monitoring().loader(Monitoring().layout,Menu().layout)),0)
     Menu().slotconf(4, ('Settings', red, 24, Settings().load),0)
     make_label('All Things On Next page', 25, 149, 24, yellow)
   roomcheck = 0
   things = []
   counter = 1 
   while True:
     if counter-1+3 >= len(Config.things[roomcheck]): 
         roomcheck = roomcheck + 1
         counter = 1 #reset output
     if roomcheck > len(Config.things)-1: break
     #########Room info######################################
     name = Config.things[roomcheck][0]
     colour = Config.things[roomcheck][1]
     thing = list(Config.things[roomcheck][counter-1+3])
     thing.extend([name,colour])
     #########Add Thing#####################################
     things.append(thing)#Config.things[roomcheck][counter-1+3])
     ####Debugging##########################################
     #print roomcheck
     #print counter-1+3 
     #print Config.things[roomcheck][counter-1+3]
     #######################################################
     counter = counter + 1
   #print len(things) #Debugging
   counter = 1 
   while counter <= 6: #Maximun no. of slots
     if page == 0: break
     if page*6+counter-1-6 >= len(things): break #Stop at no. of programs
     Menu().slotconf(counter, things[page*6+counter-1-6],1)
     counter = counter + 1

   Menu().slotconf(7, ('Back', white, 24, exit),0)
   Menu().slotconf(8, ('Next', white, 24, nextpage),0)

 def check(self):
  while 1:
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break

class Control:
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
 
 def labelconf(self,slot, app):
    if slot == 1:
        make_label(app[0], 25, 75, app[1], app[2])
    if slot == 2:
        make_label(app[0], 165, 75, app[1], app[2])
    if slot == 3:
        make_label(app[0], 25, 112, app[1], app[2])
    if slot == 4:
        make_label(app[0], 165, 112, app[1], app[2])
    if slot == 5:
        make_label(app[0], 25, 149, app[1], app[2])
    if slot == 6:
        make_label(app[0], 165, 149, app[1], app[2])
    if slot == 7:
        make_label(app[0], 25, 186, app[1], app[2])
    if slot == 8:
        make_label(app[0], 165, 186, app[1], app[2])
 
 def modeconf(self, slot, room, info, app): #Pending More Modification for input
   time = str(datetime.datetime.now().time())[0:8]
   date = str(datetime.date.today())
   if app[0] == 0: #Set Output mode
      if app[1] == 0: #Function (input/output,mode,label,colour,font,function)
        def function():
          os.system('echo "1" > /tmp/Things/'+room[0]+'/'+info[0]+'/'+app[2])
          Monitoring().fileinsert(0,app[2]+' happened',info[0],room[0],date+' '+time)
          app[5]()
        Control().slotconf(slot,(app[2],app[3],app[4],function))
      if app[1] == 1: #Toggle Mode
        ####Toggle switch#########################################################
        def switch():
          #len(app)-6 #No of toggle modes
          app[2] = app[2]+1
          if app[2] > len(app)-6-1: app[2] = 0 
          app[6+app[2]][3]()
          os.system('echo "'+str(app[2])+'" > /tmp/Things/'+room[0]+'/'+info[0]+'/'+app[3])
          Monitoring().fileinsert(0,'Switched to '+app[6+app[2]][0],info[0],room[0],date+' '+time)
          #clearall()
          #Control().layout(info,room)

        label = app[6+app[2]][0]
        colour = app[6+app[2]][1]
        font = app[6+app[2]][2]
        #func = app[6+app[2]][3]

        Control().slotconf(slot,(label,colour,font,switch))
        ##########################################################################
   else: #Show Input Mode
      if app[1] == 0: #Show
        input = app[3]()
        text = subprocess.Popen(["cat","/tmp/Things/"+room[0]+"/"+info[0]+"/"+app[2]],stdout=subprocess.PIPE).stdout.read().decode()
        if (text[:len(text)-1] != input):
            os.system('echo "'+input+'" > /tmp/Things/'+room[0]+"/"+info[0]+"/"+app[2])
            Monitoring().fileinsert(0,app[2]+': '+input,info[0],room[0],date+' '+time)
        Control().labelconf(slot,(app[2]+': '+input,app[5],app[4]))
   
   pass #

 def layout(self,info,room):
   #print info #Debugging
   make_label(info[0], 20, 20, 47, cyan)
   make_label(info[2]+room[0], 160, 20, 24, room[1])
   make_label(info[2]+info[3], 160, 40, 24, green)
   
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     #print info #Debugging
     Control().check(info,room)
     #global back
     #back = 0
     page = page - 1
     clearall()
     Control().layout(info,room)
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(info[5]): break #Stop at no. of programs
     Control().modeconf(counter, room, info, info[5][page*6+counter-1])
     counter = counter + 1

   def ifttt(): IFTTTconf().load(info,room)
   make_button('Back', 25, 186, 27, 82, 5, white, 24, exit)
   make_button('IFTTT', 117, 186, 27, 82, 5, yellow, 23, ifttt)
   make_button('Next', 209, 186, 27, 85, 5, white, 24, nextpage)
   
 def check(self,info,room):
  while 1:
   clearall()
   Control().layout(info,room)
   touchdisch()
   if len(info[5]) != 0:
     if info[4]() != 0: 
       clearall()
       make_label('Lost', 40, 60, 60, cyan)
       make_label('Connection', 40, 120, 60, cyan)
       touchdisch()
       time.sleep(1)
       clearall()
       break
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self,info):
  os.system('pkill -f IOTLink.py') #Allow Access to Device
  global page
  temp = page
  page = 0
  clearall()
  make_label('Loading', 40, 60, 60, cyan)
  touchdisch()
  Control().check(info[4](),(info[5],info[6]))
  clearall()
  page = temp
  Menu().layout()
  os.system('sudo python IOTLink.py &') #Resume IOT Access to Device

class IFTTTconf:
 def __init__(self): pass
      
 # Slot Configuration
 def modeconf(self, slot,room, info, app): #Pending More Modification for input
   if app[0] == 0: #Set Output mode
      if app[1] == 0: #Function (input/output,mode,label,colour,font,function)
         def config(): 
           IFTTTconf().showtype(([1,'When '+app[2]],[1,'When '+app[2]]))#,[0,'Do '+app[2]]))#,[0,'Do "'+app[2]+'"'],[1,'When "'+app[2]+'"'],[1,'When "'+app[2]+'"'],[0,'Do "'+app[2]+'"'],[0,'Do "'+app[2]+'"'],[0,'Do "'+app[2]+'"'],[1,'When "'+app[2]+'"'],[0,'Do "'+app[2]+'"'],[0,'Do "'+app[2]+'"'])) #Debugging
           global condition
           if condition == 0: return #exit
           elif len(Config.IOT.ifttt) == 6:
             make_label('Limit ', 40, 60, 60, cyan)
             make_label('Reached', 40, 120, 60, cyan)
             touchdisch()
             time.sleep(1)
             clearall()
             return #exit
           elif condition[0] == 0: IOTinfo = [''] #Action
           elif condition[0] == 1: #Trigger
             IFTTTconf().eventname()
             global name
             if name != '':  IOTinfo = [name]
             else: return
           IOTinfo.extend(condition)
           IFTTTconf().fileinsert(room,info,app,IOTinfo)
         Control().slotconf(slot,(app[2],app[3],app[4],config))
      if app[1] == 1: #Toggle Mode
        def config():
           nostates = 0
           modeavaliable = []
           while nostates <= len(app)-6-1: 
             #modeavaliable.append((0,'Do '+app[6+nostates][0], nostates))
             modeavaliable.append((1,'When '+app[6+nostates][0], nostates))
             nostates = nostates + 1
           print modeavaliable
           IFTTTconf().showtype(modeavaliable)
           global condition
           if condition == 0: return #exit
           elif len(Config.IOT.ifttt) == 6:
             make_label('Limit ', 40, 60, 60, cyan)
             make_label('Reached', 40, 120, 60, cyan)
             touchdisch()
             time.sleep(1)
             clearall()
             return #exit
           elif condition[0] == 0: IOTinfo = [''] #Action
           elif condition[0] == 1:
             IFTTTconf().eventname()
             global name
             if name != '': IOTinfo = [name]
             else: return
           IOTinfo.extend(condition)
           IFTTTconf().fileinsert(room,info,app,IOTinfo)
         
        Control().slotconf(slot,(app[3],app[4],app[5],config))
   else: #Show Input Mode
      if app[1] == 0: #Show
        def config():
          IFTTTconf().showtype(((1,app[2]+' == string'),(1,app[2]+' != string')))
          global condition
          if condition == 0: return #exit
          elif len(Config.IOT.ifttt) == 6:
             make_label('Limit ', 40, 60, 60, cyan)
             make_label('Reached', 40, 120, 60, cyan)
             touchdisch()
             time.sleep(1)
             clearall()
             return #exit
          elif condition[0] == 1:
            IFTTTconf().stringinput(app[2])
            global string
            if string == 0: return #exit
            else:
              IFTTTconf().eventname()
              global name
              if name != '': IOTinfo = [name]
              else: return
            IOTinfo.append(condition[0])
            #print condition[1][:(len(app[2])+4)]+'"'+string+'"' #Debugging
            IOTinfo.append(condition[1][:(len(app[2])+4)]+string)
            IFTTTconf().fileinsert(room,info,app,IOTinfo) 
        Control().labelconf(slot,(app[2],app[5],app[4]))
        Control().slotconf(slot,('',black,1,config))
   
 def layout(self,info,room): 
   make_label('Set IFTTT Recipes', 20, 20, 47, yellow)
   
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     #print info #Debugging
     IFTTTconf().layout(info,room)
     while 1:
       clearall()
       IFTTTconf().layout(info,room)
       touchdisch()
       global back
       if back == 1: 
         back = 0
         break
     page = page - 1
     clearall()
     IFTTTconf().layout(info,room)
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(info[5]): break #Stop at no. of programs
     IFTTTconf().modeconf(counter,room, info, info[5][page*6+counter-1])
     counter = counter + 1

   def blynk():
     Blynkconf().load(info,room)
     exit()
   make_button('Back', 25, 186, 27, 82, 5, white, 24, exit)
   #make_button('Blynk', 117, 186, 27, 82, 5, green, 23, blynk)
   make_button('Control', 117, 186, 27, 82, 5, blue, 23, exit)
   make_button('Next', 209, 186, 27, 85, 5, white, 24, nextpage)
   
 def check(self):
  while 1:
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self,info,room):
  global page
  temp = page
  page = 0
  stuff = info
  while 1:
   clearall()
   IFTTTconf().layout(stuff,room)
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  clearall()
  page = temp
  
 def showtype(self,other):
   def layout(other):
     global type
     global condition
     def typech(): 
       global type
       if type == 'Action': type = 'Trigger'
       else: type = 'Action'
       clearall()
       layout(other)
     make_label('Type: ', 30, 35, 60, cyan)
     make_button(type, 150, 40, 45, 140, 5, cyan, 50, typech)

     def change():
       global page
       temp = page
       page = 0
       clearall()
       IFTTTconf().changetypelayout(other)
       IFTTTconf().check()
       clearall()
       page = temp
       layout(other)
     make_button(condition[1], 40, 100, 40, 240, 5, yellow, 40, change)
     
     def exit():
       global condition
       condition = 0
       global back
       back = 1
     def ok(): 
       global back
       back = 1
     Control().slotconf(7, ('Back', white, 24, exit))
     Control().slotconf(8, ('OK', white, 24, ok))
   
   global type
   global condition
   if other[0][0] == 0: type = 'Action'
   else: type = 'Trigger'
   condition = other[0]
   clearall()
   layout(other)
   IFTTTconf().check()
   clearall()
 
 def changetypelayout(self,info):
   info = list(info)
   global type
   make_label(type+'s', 20, 20, 47, yellow)
    
   def log(cond): 
     def login():
       global condition
       condition = cond
       global back
       back = 1 
     return login
   if type == 'Action': btype = 0
   else: btype = 1
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(info): break #Stop at no. of programs
     try: 
       while btype != info[page*6+counter-1][0]: 
         print counter
         print info[page*6+counter-1]
         info.pop(page*6+counter-1)
         print page*6+counter-1
         print info
       Control().slotconf(counter, (info[page*6+counter-1][1],orange,20,log(info[page*6+counter-1])))
     except IndexError:
       pass
     counter = counter + 1
     
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     IFTTTconf().changetypelayout(info)
     IFTTTconf().check()
     global back
     back = 0
     page = page - 1
     clearall()
     IFTTTconf().changetypelayout(info)
   Control().slotconf(7, ('Back', white, 24, exit))
   Control().slotconf(8, ('Next', white, 24, nextpage))

 def stringinput(self,other):
   def layout(other):
     global string
     make_label('String: '+other+':', 30, 35, 60, cyan)
     
     def change():
       global string
       vkey = VirtualKeyboard(screen)
       string = vkey.run(string)
       clearall()
       layout(other)
     make_button(string, 40, 100, 40, 240, 5, yellow, 40, change)
     
     def exit():
       global string
       string = 0
       global back
       back = 1
     def ok(): 
       global back
       back = 1
     Control().slotconf(7, ('Back', white, 24, exit))
     Control().slotconf(8, ('OK', white, 24, ok))
   
   global string
   string = ''
   clearall()
   layout(other)
   IFTTTconf().check()
   clearall()
   
 def eventname(self):
  global name
  name = ''
  def layout():
    clearall()
    make_label('Eventname:', 40, 40, 60, cyan)
    make_button(name, 40, 100, 40, 240, 5, yellow, 40, change)
 
    def exit():
      global name
      name = ''
      global back
      back = 1
    def ok(): 
      global back
      back = 1
    Control().slotconf(7, ('Back', white, 24, exit))
    Control().slotconf(8, ('Set', white, 24, ok))

  def change():
    vkey = VirtualKeyboard(screen)
    global name
    name = vkey.run(name)
    clearall()
    layout()
  
  layout()
  while 1: 
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break
  clearall()
  if name == '':
    make_label('Recipe Not', 40, 60, 60, cyan)
    make_label('Set', 40, 120, 60, cyan)
    touchdisch()
    time.sleep(1)
    clearall()

 def fileinsert(self,room,device,function,IOTinfo): 
   device = device[:4]
   if function[0] == 0: #Set Output mode
      if function[1] == 0: function = function[:5] #Function 
      if function[1] == 1: function = function[:6] #Toggle Mode
   else: #Show Input Mode
      if function[1] == 0: function = function[:3] #Show
   Config.IOT.ifttt.append((1,room,device,function,IOTinfo))
   IOT().filerewrite(Config.IOT.ifttt,Config.IOT.blynk)
   #print (room,device[:4],function[:5],mode,type,IOTinfo)
   #print Config.IOT.ifttt
    
class Blynkconf:
 def __init__(self): pass
 
 def modeconf(self, slot, room, info, app): #Pending More Modification for input
   if app[0] == 0: #Set Output mode
      if app[1] == 0: #Function (input/output,mode,label,colour,font,function)
         def config(): 
           Blynkconf().pininput()
           global pin
           if pin == '': return #exit
           IOTinfo = [pin,'Button']
           if Blynkconf().showmode(1,'Button (On/Off)'): Blynkconf().fileinsert(room,info,app,IOTinfo)
           else: return
           
         Control().slotconf(slot,(app[2],app[3],app[4],config))
      if app[1] == 1: #Toggle Mode
        def config():
           nostates = 0
           modeavaliable = []
           while nostates <= len(app)-6-1: 
             modeavaliable.append((0,'Do "'+app[6+nostates][0]+'"'))
             modeavaliable.append((1,'When "'+app[6+nostates][0]+'"'))
             nostates = nostates + 1
           print modeavaliable
           Blynkconf().pininput()
           global pin
           if pin == '': return #exit
           IOTinfo = [pin,'Slider']
           if Blynkconf().showmode(1,'Slider type (0/1/...)'): Blynkconf().fileinsert(room,info,app,IOTinfo)
           else: return
           
        Control().slotconf(slot,(app[3],app[4],app[5],config))
   else: #Show Input Mode
      if app[1] == 0: #Show
        def config():
          Blynkconf().pininput()
          global pin
          if pin == '': return #exit
          Blynkconf().selection(room,info,app)
        Control().labelconf(slot,(app[2],app[5],app[4]))
        Control().slotconf(slot,('',black,1,config))

     
 def layout(self,info,room): 
   make_label('Blynk config', 20, 20, 47, green)
   
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     #print info #Debugging
     Blynkconf().check(info)
     #global back
     #back = 0
     page = page - 1
     clearall()
     Blynkconf().layout(info)
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(info[5]): break #Stop at no. of programs
     Blynkconf().modeconf(counter, room, info, info[5][page*6+counter-1])
     counter = counter + 1

   def passs(): pass
   make_button('Back', 25, 186, 27, 82, 5, white, 24, exit)
   make_button('Control', 117, 186, 27, 82, 5, cyan, 23, exit)
   make_button('Next', 209, 186, 27, 85, 5, white, 24, nextpage)
   
 def check(self,info,room):
  while 1:
   clearall()
   Blynkconf().layout(info,room)
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self,info,room):
  global page
  temp = page
  page = 0
  clearall()
  Blynkconf().check(info,room)
  clearall()
  page = temp

 def pininput(self):
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

    make_label('Virtual Pin:', 20, 35, 35, cyan)
    def change():pass
    make_button(pin, 25, 83, 35, 95, 5, yellow, 40, change)
    make_button('Del', 120, 83, 35, 35, 5, red, 25, de)

    make_button('1', 175, 35, 35, 35, 5, green, 40, one)
    make_button('2', 223, 35, 35, 35, 5, green, 40, two)
    make_button('3', 270, 35, 35, 35, 5, green, 40, three)
    make_button('4', 175, 83, 35, 35, 5, green, 40, four)
    make_button('5', 223, 83, 35, 35, 5, green, 40, five)
    make_button('6', 270, 83, 35, 35, 5, green, 40, six)
    make_button('7', 175, 131, 35, 35, 5, green, 40, seven)
    make_button('8', 223, 131, 35, 35, 5, green, 40, eight)
    make_button('9', 270, 131, 35, 35, 5, green, 40, nine)
    make_button('0', 270, 178, 35, 35, 5, green, 40, zero)

    def exit():
      global pin
      pin = ''
      global back
      back = 1
    def ok(): 
      #####Pin check##########################################
      global pin
      counter = 1  
      while page*6+counter-1 < len(Config.IOT.blynk): #Stop at no. of programs
        if pin == Config.IOT.blynk[page*6+counter-1][4][0]:
          clearall()
          make_label('Pin Already', 40, 60, 60, cyan)
          make_label('Used', 40, 120, 60, cyan)
          touchdisch()
          time.sleep(1)
          clearall()
          layout()
          break
        counter = counter + 1
      #########################################################
      if page*6+counter-1 >= len(Config.IOT.blynk): #If loop reaches end of no. of programs
        global back
        back = 1
    make_button('Back', 25, 186, 27, 106, 5, white, 24, exit)
    make_button('Set', 146, 186, 27, 106, 5, white, 24, ok)

  layout()
  while 1: 
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break
  clearall()
  if pin == '':
    make_label('Pin Not', 40, 60, 60, cyan)
    make_label('Set', 40, 120, 60, cyan)
    touchdisch()
    time.sleep(1)
    clearall()

 def showmode(self,type,other):
   def layout(type,other):
     def typech(): pass
     make_label('Type: ', 30, 35, 60, cyan)
     make_button(type, 150, 40, 45, 140, 5, cyan, 50, typech)

     def change(): pass
     make_button(other, 40, 100, 40, 240, 5, yellow, 40, change)
     
     def exit():
       global ok
       ok = 0
       global back
       back = 1
     def ok(): 
       global ok
       ok = 1
       global back
       back = 1
     Control().slotconf(7, ('Back', white, 24, exit))
     Control().slotconf(8, ('OK', white, 24, ok))
   
   if type == 0: type = 'Output'
   else: type = 'Input'
   clearall()
   layout(type,other)
   IFTTTconf().check()
   clearall()
   global ok 
   return ok

 def selection(self,room,info,app):
   def layout():
     def exit():
       global back
       back = 1
     Control().slotconf(7, ('Back', white, 24, exit))
     
     def no():
       IOTinfo = [pin,'Value']
       if Blynkconf().showmode(1,'Value Display'): Blynkconf().fileinsert(room,info,app,IOTinfo)
       exit()
     def text():
       IOTinfo = [pin,'LCD']
       if Blynkconf().showmode(1,'LCD (text)'): Blynkconf().fileinsert(room,info,app,IOTinfo)
       exit()
     make_button('Numbers Only', 25, 30, 60, 280, 10, cyan, 50, no)
     make_button('Text', 25, 100, 60, 280, 10, yellow, 50, text)
        
   clearall()
   layout()
   IFTTTconf().check()
   clearall()
   
 def fileinsert(self,room,device,function,IOTinfo): 
   device = device[:4]
   if function[0] == 0: #Set Output mode
      if function[1] == 0: function = function[:5] #Function 
      if function[1] == 1: function = function[:6] #Toggle Mode
   else: #Show Input Mode
      if function[1] == 0: function = function[:3] #Show
   Config.IOT.blynk.append((1,room,device,function,IOTinfo))
   IOT().filerewrite(Config.IOT.ifttt,Config.IOT.blynk)
   #print (room,device[:4],function,IOTinfo)
   #print Config.IOT.blynk   

class IOT:
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
   
 def check(self):
  while 1:
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def layout(self):
   make_label('IOT', 20, 20, 47, cyan)
   def passs(): pass #Debugging
   make_button('IFTTT', 25, 75, 27, 130, 5, yellow, 24, IOT().IFTTTload)
   make_button('Blynk', 165, 75, 27, 130, 5, green, 24, IOT().Blynkremove)
   def exit(): 
     global back
     back = 1 
   make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
    
 def load(self):
  global page
  temp = page
  page = 0
  clearall()
  IOT().layout()
  IOT().check()
  clearall()
  page = temp
  Menu().layout()

 def IFTTTlayout(self):
  make_label('IFTTT', 20, 20, 47, yellow)
  make_button('Auth Key ', 25, 75, 27, 130, 5, orange, 24, IOT().IFTTTauth)
  make_button('Remove Recipes', 165, 75, 27, 130, 5, blue, 20, IOT().IFTTTremove)
  def exit(): 
    global back
    back = 1 
  make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
  
 
 def IFTTTload(self):
  global page
  temp = page
  page = 0
  clearall()
  IOT().IFTTTlayout()
  IOT().check()
  clearall()
  page = temp
  #IOT().layout()
  Menu().layout()  

 def IFTTTauth(self):
   def layout():
     global string
     make_label('Auth Key', 30, 35, 60, cyan)
     
     def change():
       vkey = VirtualKeyboard(screen)
       Config.IOT.iftttkey = vkey.run(Config.IOT.iftttkey)
       clearall()
       layout()
     make_button(Config.IOT.iftttkey, 40, 100, 40, 240, 5, yellow, 30, change)
     
     def exit():
       global back
       back = 1
     def ok(): 
       IOT().filerewrite(Config.IOT.ifttt,Config.IOT.blynk)
       global back
       back = 1
     Control().slotconf(7, ('Back', white, 24, exit))
     Control().slotconf(8, ('OK', white, 24, ok))
   
   clearall()
   layout()
   IFTTTconf().check()
   clearall()
   IOT().IFTTTlayout()

 def IFTTTremovelayout(self):
   make_label('Remove Recipes', 20, 20, 47, cyan)

   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(Config.IOT.ifttt): break #Stop at no. of programs
     ####################################
     thing = Config.IOT.ifttt[page*6+counter-1]
     #####Colour#########################
     if thing[4][1] == 0: colour = yellow #Action
     else: colour = blue #Trigger
     ####################################
     def rm(thing):
       def function():
         IOT().IFTTTremoveconfirm(thing)
         clearall()
         IOT().IFTTTremovelayout()
       return function
     Control().slotconf(counter, (thing[2][0],colour,24,rm(thing)))
     counter = counter + 1

   def exit(): 
     global back
     back = 1 
   make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)

 def IFTTTremoveconfirm(self,thing):
  def layout():
    clearall()
    #####Name#############################
    function = thing[3]
    if function[0] == 0: #Set Output mode
      if function[1] == 0: name = function[2] #Function 
      if function[1] == 1: name = function[3] #Toggle Mode
    else: #Show Input Mode
      if function[1] == 0: name = function[2]
    #####Type#############################
    IOTinfo = thing[4]
    if IOTinfo[1] == 1: type = 'Trigger'
    elif IOTinfo[1] == 0: type = 'Action'
    ######################################
    make_label('Room: '+thing[1][0], 25, 20, 25, thing[1][1])
    make_label('Device: '+thing[2][0], 25, 40, 25, orange)
    make_label(name+': '+type, 25, 60, 50, cyan)
    def passs(): pass
    make_button(IOTinfo[2], 32, 110, 40, 240, 5, yellow, 40, passs)
    make_label('Eventname:'+IOTinfo[0], 25, 150, 25, green)
    
    def exit():
      global back
      back = 1
    def ok(): 
      IOT().iftttfileremove(thing)
      global back
      back = 1
    Control().slotconf(7, ('Back', white, 24, exit))
    Control().slotconf(8, ('Remove', white, 24, ok))
  
  layout()
  while 1: 
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break
  clearall()

 def IFTTTremove(self): 
   global page
   temp = page
   page = 0
   clearall()
   IOT().IFTTTremovelayout()
   IOT().check()
   clearall()
   page = temp
   IOT().IFTTTlayout()
 
 def iftttfileremove(self,thing):
   Config.IOT.ifttt.remove(thing)
   IOT().filerewrite(Config.IOT.ifttt,Config.IOT.blynk)

 def Blynkremovelayout(self):
   make_label('Remove Connections', 20, 20, 40, cyan)

   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(Config.IOT.blynk): break #Stop at no. of programs
     ####################################
     thing = Config.IOT.blynk[page*6+counter-1]
     function = thing[3]
     #####Font and Name###################
     if function[0] == 0: #Set Output mode
       if function[1] == 0:
         name = function[2]
         font = function[4] #Function 
       if function[1] == 1:
         name = function[3] 
         font = function[5] #Toggle Mode
     else: #Show Input Mode
       if function[1] == 0:
         name = function[2]
         font = 24
     ####################################
     def rm(thing):
       def function():
         IOT().Blynkremoveconfirm(thing)
         clearall()
         IOT().Blynkremovelayout()
       return function
     Control().slotconf(counter, (name,yellow,font,rm(thing)))
     counter = counter + 1

   def exit(): 
     global back
     back = 1 
   def nextpage():
     global page
     page = page + 1
     clearall()
     IOT().IFTTTremovelayout()
     IOT().check()
     clearall()
     page = page - 1
     IOT().IFTTTremovelayout()
   make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
   make_button('Next', 165, 186, 27, 130, 5, white, 24, nextpage)

 def Blynkremoveconfirm(self,thing):
  def layout():
    clearall()
    #####Name#############################
    function = thing[3]
    IOTinfo = thing[4]
    if function[0] == 0: #Set Output mode
      if function[1] == 0: name = function[2] #Function 
      if function[1] == 1: name = function[3] #Toggle Mode
    else: #Show Input Mode
      if function[1] == 0: name = function[2]
    ######################################
    make_label('Room: '+thing[1][0], 25, 20, 25, thing[1][1])
    make_label(name+' as:', 25, 40, 53, cyan)
    def passs(): pass
    make_button(IOTinfo[1], 40, 100, 40, 240, 5, yellow, 40, passs)
    make_label('Virtual Pin: '+IOTinfo[0], 25, 145, 25, green)
    
    def exit():
      global back
      back = 1
    def ok(): 
      IOT().blynkfileremove(thing)
      global back
      back = 1
    Control().slotconf(7, ('Back', white, 24, exit))
    Control().slotconf(8, ('Remove', white, 24, ok))
  
  layout()
  while 1: 
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break
  clearall()

 def Blynkremove(self): 
   global page
   temp = page
   page = 0
   clearall()
   IOT().Blynkremovelayout()
   IOT().check()
   clearall()
   page = temp
   IOT().layout()

 def blynkfileremove(self,thing):
   Config.IOT.blynk.remove(thing)
   IOT().filerewrite(Config.IOT.ifttt,Config.IOT.blynk)

 def filerewrite(self,iftttlist,blynklist): 
   #####IFTTT##########################
   os.system('echo "iftttkey = '+"'"+Config.IOT.iftttkey+"'"+' " > Config/IOT.py')
   os.system('echo "ifttt = []" >> Config/IOT.py')
   counter = 1
   while counter <= len(iftttlist):
     thing = list(iftttlist[counter-1])
     thing.pop(0)
     thing.insert(0,counter)
     os.system('echo "ifttt.append('+str(thing)+')" >> Config/IOT.py')
     counter = counter + 1
   #####Blynk###########################
   os.system('echo "blynk = []" >> Config/IOT.py')
   counter = 1
   while counter <= len(blynklist):
     thing = list(blynklist[counter-1])
     thing.pop(0)
     thing.insert(0,counter)
     os.system('echo "blynk.append('+str(thing)+')" >> Config/IOT.py')
     counter = counter + 1
   
#roommod = 0
class Rooms:
 def __init__(self): pass
      
 # Slot Configuration
 def slotconf(self,slot, app, roomno):
    #if roommod == 1:
    #  colour = yellow
    #  font = app[2]
    #  def run():
    #    vkey = VirtualKeyboard(screen)
    #    txt = vkey.run('txt')
    #else:
    colour = app[1]
    font = app[2]
    def run(): Rooms().inload(roomno)
    if slot == 1:
        make_button(app[0], 25, 75, 27, 130, 5, colour, font, run)
    if slot == 2:
        make_button(app[0], 165, 75, 27, 130, 5, colour, font, run)
    if slot == 3:
        make_button(app[0], 25, 112, 27, 130, 5, colour, font, run)
    if slot == 4:
        make_button(app[0], 165, 112, 27, 130, 5, colour, font, run)
    if slot == 5:
        make_button(app[0], 25, 149, 27, 130, 5, colour, font, run)
    if slot == 6:
        make_button(app[0], 165, 149, 27, 130, 5, colour, font, run)
    if slot == 7:
        make_button(app[0], 25, 186, 27, 130, 5, app[1], app[2], app[3])
    if slot == 8:
        make_button(app[0], 165, 186, 27, 130, 5, app[1], app[2], app[3])

 def layout(self): 
   make_label('Rooms', 20, 20, 47, green)
   #def modmode():
   #  global roommod
   #  if roommod == 1: roommod = 0
   #  else: roommod = 1
   #  clearall()
   #  Rooms().layout()
   #make_button('Change', 165, 30, 27, 130, 5, yellow, 24, modmode)
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     Rooms().layout()
     Rooms().check()
     #global back
     #back = 0
     page = page - 1
     clearall()
     Rooms().layout()
   def passs(): pass #Debugging
   shit = ('Shit', green, 24, passs) #Debugging
   app = (shit,shit,shit,shit,shit,shit,shit,shit,shit,shit) #Debugging 
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(Config.things): break #Stop at no. of programs
     Rooms().slotconf(counter, Config.things[page*6+counter-1], page*6+counter-1)
     counter = counter + 1

   Rooms().slotconf(7, ('Back', white, 24, exit),0)
   Rooms().slotconf(8, ('Next', white, 24, nextpage),0)

 def inlayout(self,roomno): 
   make_label(Config.things[roomno][0], 20, 20, 47, green)
   #def modmode():
   #  global roommod
   #  if roommod == 1: roommod = 0
   #  else: roommod = 1
   #  clearall()
   #  Rooms().layout()
   #make_button('Change', 165, 30, 27, 130, 5, yellow, 24, modmode)
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     Rooms().inlayout(roomno)
     Rooms().check()
     #global back
     #back = 0
     page = page - 1
     clearall()
     Rooms().inlayout(roomno)
   def passs(): pass #Debugging
   shit = ('Shit', green, 24, passs) #Debugging
   app = (shit,shit,shit,shit,shit,shit,shit,shit,shit,shit) #Debugging 
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     #print page #Debugging
     if page*6+counter-1+3 >= len(Config.things[roomno]): break #Stop at no. of programs
     #########Room info######################################
     name = Config.things[roomno][0]
     colour = Config.things[roomno][1]
     thing = list(Config.things[roomno][counter-1+3])
     thing.extend([name,colour])
     #########Add Thing#####################################
     Menu().slotconf(counter,thing,1)#Config.things[roomno][page*6+counter-1+3],1)
     counter = counter + 1
   Rooms().slotconf(7, ('Back', white, 24, exit),0)
   Rooms().slotconf(8, ('Next', white, 24, nextpage),0)
 
 def check(self):
  while 1:
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self):
  global page
  temp = page
  page = 0
  clearall()
  Rooms().layout()
  Rooms().check()
  clearall()
  page = temp
  Menu().layout()
 
 def inload(self,roomno):
  global page
  temp = page
  page = 0
  clearall()
  Rooms().inlayout(roomno)
  Rooms().check()
  clearall()
  page = temp
  Rooms().layout()

class Monitoring:
 def __init__(self): pass
    
 def layout(self): 
   make_label('Monitoring', 20, 20, 47, yellow)
   def exit(): 
     global back
     back = 1 
   def passs(): pass #Debugging
   
   make_button('Motion Detected _ times', 25, 75, 27, 270, 5, orange, 24, Monitoring().loader(Monitoring().Alarm,Monitoring().layout))
   make_button('Activity', 25, 112, 27, 270, 5, orange, 24, Monitoring().listloader(0,Monitoring().layout))

   make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
   #Monitoring().slotconf(8, ('Next', white, 24, nextpage))
 
 def Alarm(self):
   make_label('Alarm', 20, 20, 47, yellow)
   def exit(): 
     global back
     back = 1 
   make_label('Alarms people and takes picture when', 20, 60, 20, green)
   make_label('motion is detected', 20, 75, 20, green)
   ####Toggle switch#########################################################
   def switch():
     if Config.Activity.alarm == 0: 
       Config.Activity.alarm = 1
       Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
     else:
       Config.Activity.alarm = 0
       Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
     clearall()
     Monitoring().Alarm()
     
   if Config.Activity.alarm == 0:
      label = 'Turn On '
   else:
      label = 'Turn Off'
   make_button(label, 25, 112, 27, 130, 5, orange, 24, switch)
   ############################################################################ 
   def view():
       disinitdis()
       os.system('cd /home/pi/Software/Camera/adafruit-pi-cam-master && sudo python cam.py')
       initdis()
       Monitoring().Alarm()
   make_button('Camera View', 165, 112, 27, 130, 5, orange, 24, view)
   make_button('Photos', 25, 149, 27, 130, 5, orange, 24, Monitoring().listloader(1,Monitoring().Alarm))
   make_button('Photos Dir', 165, 149, 27, 130, 5, orange, 24, Monitoring().loader(Monitoring().Photodir,Monitoring().Alarm))
   make_button('Back', 25, 186, 27, 130, 5, white, 24, exit)
   #Monitoring().slotconf(8, ('Next', white, 24, nextpage))

 def Photodir(self):
    global string
    make_label('Photo Dir', 30, 35, 60, cyan)
    
    def change():
      vkey = VirtualKeyboard(screen)
      Config.Activity.photodir = vkey.run(Config.Activity.photodir)
      clearall()
      Monitoring().Photodir()
    make_button(Config.Activity.photodir, 40, 100, 40, 240, 5, yellow, 30, change)
    
    def exit():
      global back
      back = 1
    def ok():
      os.system('mkdir '+Config.Activity.photodir)
      Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
      global back
      back = 1
    Control().slotconf(7, ('Back', white, 24, exit))
    Control().slotconf(8, ('OK', white, 24, ok))
 
 def listconf(self,slot,name,func):
    if slot == 1:
        make_button(name, 25, 75, 27, 270, 5, orange, 24, func)
    if slot == 2:
        make_button(name, 25, 112, 27, 270, 5, orange, 24, func)
    if slot == 3:
        make_button(name, 25, 149, 27, 270, 5, orange, 24, func)
    
 def listlayout(self,type):
   if type == 0:
       labeling = 'Activity'
       list = Config.Activity.activity
       #print list #Debugging
       def func(room,device,activity,date):
          def intfunc(): Monitoring().activityshow(room,device,activity,date)
          return intfunc
   elif type == 1:
       labeling = 'Photos'
       list = Config.Activity.photo
       def func(date): 
           def intfunc(): Monitoring().photoshow(date)
           return intfunc
   make_label(labeling, 20, 20, 47, yellow) #'10:30 am'
   
   counter = 1  
   while counter <= 3: #Maximun no. of slots
     if page*3+counter-1 >= len(list): break #Stop at no. of programs
     if type == 0: Monitoring().listconf(counter, list[page*3+counter-1][0], func(list[page*3+counter-1][2],list[page*3+counter-1][1],list[page*3+counter-1][0],list[page*3+counter-1][3]))
     if type == 1: Monitoring().listconf(counter, list[page*3+counter-1], func(list[page*3+counter-1]))
     counter = counter + 1

   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     global back
     page = page + 1
     Monitoring().listlayout(type)
     Monitoring().check()
     back = 0
     page = page - 1
     clearall()
     Monitoring().listlayout(type)
   def clear():
       if type == 0: Config.Activity.activity = []#Activity Clear 
       if type == 1: #Photos Clear
           os.system('rm -rf '+Config.Activity.photodir)
           os.system('mkdir '+Config.Activity.photodir)
           Config.Activity.photo = [] 
       Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
       clearall()
       Monitoring().listlayout(type)
   make_button('Back', 25, 186, 27, 82, 5, white, 24, exit)
   make_button('Clear', 117, 186, 27, 82, 5, white, 23, clear)
   make_button('Next', 209, 186, 27, 85, 5, white, 24, nextpage)

 def activityshow(self,room,device,activity,date):
  global back
  clearall()
  def passs(): pass
  make_label(date, 25, 20, 25, cyan)
  make_button(activity, 32, 50, 50, 280, 10, yellow, 40, passs)
  make_label('Room: '+room, 25, 100, 30, blue)
  make_label('Device: '+device, 25, 130, 30, orange)
  #make_label('Has Been Triggered', 25, 115, 40, cyan)
  #make_label('Eventname:'+eventname, 25, 150, 25, green)
  
  def exit():
    global back
    back = 1
  make_button("Back", 25, 186, 27, 130, 5, white, 25, exit)
  
  Monitoring().check()
  clearall()
  Monitoring().listlayout(0)

 def photoshow(self,date):
  global back
  clearall()
  def passs(): pass
  def delete():
      os.system('rm -rf '+Config.Activity.photodir+'/'+date+'.jpeg')
      Config.Activity.photo.remove(date)
      Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
      global back
      back = 1
  def view():
      disinitdis()
      os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a '+Config.Activity.photodir+'/'+date+'.jpeg')
      time.sleep(5)
      initdis()
      Monitoring().photoshow(date)
  make_button(date, 30, 50, 50, 280, 10, yellow, 40, passs)
  make_button("Delete", 25, 112, 27, 130, 5, red, 25, delete)
  make_button("View", 175, 112, 27, 130, 5, cyan, 25, view)
  #make_label('Room: '+room, 25, 100, 30, blue)
  #make_label('Device: '+device, 25, 130, 30, orange)
  
  def exit():
    global back
    back = 1
  make_button("Back", 25, 186, 27, 130, 5, white, 25, exit)
  
  Monitoring().check()
  clearall()
  Monitoring().listlayout(1)

 def listloader(self,type,end):
  def load():
   global page
   temp = page
   page = 0
   clearall()
   Monitoring().listlayout(type)
   Monitoring().check()
   clearall()
   page = temp
   end()
  return load

 def check(self):
   global back
   while 1:
     touchdisch()
     global back
     if back == 1: 
       back = 0
       break
   
 def loader(self,layout,end):
  def load():
   global page
   temp = page
   page = 0
   clearall()
   layout()
   Monitoring().check()
   clearall()
   page = temp
   end()
  return load

 def fileinsert(self,type,text,device,room,date): 
   if type == 0: Config.Activity.activity.insert(0,(text,device,room,date))#Activity
   elif type == 1: Config.Activity.photo.insert(0,text)#Photos
   Monitoring().filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
   
 def filerewrite(self,alarm,activitylist,photodir,photolist): 
   #####Alarm##########################
   os.system('echo "alarm = '+str(alarm)+' " > Config/Activity.py')
   os.system('echo "activity = []" >> Config/Activity.py')
   counter = 1
   while counter <= len(activitylist):
     thing = list(activitylist[counter-1])
     #thing.pop(0)
     #thing.insert(0,counter)
     os.system('echo "activity.append('+str(thing)+')" >> Config/Activity.py')
     counter = counter + 1
   #####Photo###########################
   os.system('echo "photodir = '+"'"+photodir+"'"+' " >> Config/Activity.py')  
   os.system('echo "photo = []" >> Config/Activity.py')
   counter = 1
   while counter <= len(photolist):
     thing = photolist[counter-1]
     #print thing
     #thing.pop(0)
     #thing.insert(0,counter)
     os.system('echo "photo.append('+"'"+str(thing)+"'"+')" >> Config/Activity.py')
     counter = counter + 1

class Settings:
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
   make_label('Settings', 20, 20, 47, cyan)
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     Settings().layout()
     Settings().check()
     #global back
     #back = 0
     page = page - 1
     clearall()
     Settings().layout()
   def passs(): pass #Debugging
   shit = ('Shit', green, 24, passs) #Debugging
   app = (shit,shit,shit,shit,shit,shit,shit,shit,shit,shit) #Debugging 
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(app): break #Stop at no. of programs
     Settings().slotconf(counter, app[page*6+counter-1])
     counter = counter + 1

   Settings().slotconf(7, ('Back', white, 24, exit))
   Settings().slotconf(8, ('Next', white, 24, nextpage))

 def check(self):
  while 1:
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self):
  global page
  temp = page
  page = 0
  clearall()
  Settings().layout()
  Settings().check()
  clearall()
  page = temp
  Menu().layout()

menu = Menu()
menu.layout()
menu.check()
