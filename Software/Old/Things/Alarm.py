#Alarm Software For Things
#To be placed in the Service folder of the Main Software
import sys
path = '/mnt/Making/RaspberryPi/SittingFox/Software/Things/' #path of Things folder from root
sys.path.insert(0, path)
from PitftGraphicLib import *
#screen = pygame.display.set_mode(size)
import Config
#####Time Date check#########################
import time
import datetime
#####PIR Setup###############################
import RPi.GPIO as gpio
pirpin = 22 #GPIO pin for PIR motion sensor
gpio.setmode(gpio.BCM)
gpio.setup(pirpin,gpio.IN)
#############################################
back = 0

def passs(): pass

def photoshow(date):
  initdis()
  global back
  def layout(date):
    clearall()
    def passs(): pass
    def delete():
        os.system('rm -rf '+Config.Activity.photodir+'/'+date+'.jpeg')
        Config.Activity.photo.remove(date)  
        filerewrite(Config.Activity.alarm,Config.Activity.activity,Config.Activity.photodir,Config.Activity.photo)
        global back
        back = 1
    def view():
        disinitdis()
        os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose -a '+Config.Activity.photodir+'/'+date+'.jpeg')
        time.sleep(5)
        initdis()
        layout(date)
    def exit():
      global back
      back = 1
    make_button(date, 30, 50, 50, 280, 10, yellow, 40, passs)
    make_button("Delete", 25, 112, 27, 130, 5, red, 25, delete)
    make_button("View", 175, 112, 27, 130, 5, cyan, 25, view)
    make_button("Back", 25, 186, 27, 130, 5, white, 25, exit)
  layout(date)
  while 1:
    touchdisch()
    if back == 1:
      back = 0
      break
  disinitdis()

def filerewrite(alarm,activitylist,photodir,photolist): 
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

globalcounter = 0
repeattrig = 0
if Config.Activity.alarm == 1:
  def check():
    print gpio.input(pirpin) #Debugging
    global globalcounter
    global repeattrig
    if gpio.input(pirpin) & (repeattrig == 0 ):
    #if True & (repeattrig == 0 ):
        date = str(datetime.date.today())+'-'+str(datetime.datetime.now().time())[0:8]
        os.system('cd '+Config.Activity.photodir+' && raspistill -t 1000 -o '+date+'.jpeg')
        os.system('echo "photo.insert(0,'+"'"+date+"'"+')" >> '+path+'Config/Activity.py')
        os.system('echo "activity.insert(0,'+str(('Alarm was Triggered','-','-',date))+')" >> '+path+'Config/Activity.py')
        Config.Activity.photo.insert(0,date)
        globalcounter = globalcounter + 1
        repeattrig = 1
        global layout
        def info(date):
          def insidefunc(): photoshow(date)
          return insidefunc
        layout = ("The Alarm was Triggered", yellow, 24, info(date), globalcounter)
        print date #Debugging
        print layout #Debugging
        info(date)() #Debugging
        return 1
    elif not gpio.input(pirpin) & (repeattrig == 1): repeattrig = 0
    return 0
else:
    def check(): pass

while 1: check() #Debugging
