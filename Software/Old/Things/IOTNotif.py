#Things Internet Link Notif service Frontend
#To be placed in the Service folder of the Main Software
import subprocess
import time
import sys
path = '/mnt/Making/RaspberryPi/SittingFox/Software/Things/' #path of Things folder from root
sys.path.insert(0, path) 
from PitftGraphicLib import *
back = 0

def setup(): os.system('cd '+path+' && sudo python IOTLink.py &')
  
def passs(): pass

def nocon(device,room):
  global back
  initdis()
  make_label('The ', 16, 17, 45, green)
  make_button(device, 83, 20, 38, 170, 5, cyan, 40, passs)
  make_label(' in', 250, 20, 45, green)
  make_button(room, 25, 58, 38, 175, 2.5, orange, 40, passs)
  make_label(' is not', 200, 58, 45, red)
  make_label('connected ', 20, 93, 40, red)
  make_label('and the', 165, 93, 40, green)
  make_label('corrosponding ', 20, 121.5, 40, yellow)
  make_label('functions cant be run', 20, 151, 40, yellow)
  def quit():
    global back
    back = 1
  def restarter():
    os.system('pkill -f IOTLink.py')
    os.system('cd '+path+' && sudo python IOTLink.py &')
    quit()
  make_button("Back", 25, 195, 27, 130, 5, white, 25, quit)
  make_button("Restart", 165, 195, 27, 130, 5, white, 25, restarter)
  while True:
    touchdisch()
    if back == 1: break
  disinitdis()

def functrig(room,device,eventname,type,date):
  global back
  initdis()
  make_label('Room: '+room, 25, 20, 25, blue)
  make_label('Device: '+device, 25, 40, 25, orange)
  def passs(): pass
  make_button(type, 32, 75, 40, 240, 5, yellow, 40, passs)
  make_label('Has Been Triggered', 25, 115, 40, cyan)
  make_label('Eventname:'+eventname, 25, 150, 25, green)
  make_label(date, 165, 150, 20, cyan)
  
  def quit():
    global back
    back = 1
  make_button("Back", 25, 186, 27, 130, 5, white, 25, quit)
  
  while 1: 
    touchdisch()
    global back
    if back == 1: 
      back = 0
      break
  disinitdis()
  
layout = ("", green, 24, passs)
noconnectthings = 0
triggered = 0
globalcounter = 0
def check():
  global globalcounter
  #####Backend Restart Check############################################################################
  text = subprocess.Popen(["cat","/tmp/Things/System/Restarted"],stdout=subprocess.PIPE).stdout.read().decode()
  if text != '':
    os.system("rm -rf /tmp/Things/System/Restarted")
    noconnectthings = 0
    triggered = 0
  #####No Connection Check##############################################################################
  global noconnectthings
  text = subprocess.Popen(["cat","/tmp/Things/System/NoConnect"+str(noconnectthings)],stdout=subprocess.PIPE).stdout.read().decode()
  if text != '':
    os.system("rm -rf /tmp/Things/System/NoConnect"+str(noconnectthings))
    noconnectthings = noconnectthings + 1
    #####Text Check##########################
    counter = 0
    while text[counter] != ' ': counter = counter + 1
    device = text[:counter]
    room = text[counter+1:len(text)-2]  
    #device = 'ESP8266ex' #Debugging
    #room = 'LivingRoom' #Debugging
    #########################################
    def error(): nocon(device,room)
    global layout
    layout = (device+" lost connection", yellow, 24, error, globalcounter)
    globalcounter = globalcounter + 1
    #error() #Debugging
    #print layout #Debugging
    return 1
  ####Function Trigger Check###########################################################################
  global triggered
  text = subprocess.Popen(["cat","/tmp/Things/System/Triggered"+str(triggered)],stdout=subprocess.PIPE).stdout.read().decode()
  if text != '':
    #print text #Debugging
    os.system("rm -rf /tmp/Things/System/Triggered"+str(triggered))
    triggered = triggered + 1
    #####Text Check##########################
    counter = 0
    spaces = 1
    while spaces <= 4:
      if (text[counter] == ' ') & (spaces == 1):
        roomspacing = counter
        spaces = spaces + 1
      elif (text[counter] == ' ') & (spaces == 2):
        devspacing = counter
        spaces = spaces + 1
      elif (text[counter] == ' ') & (spaces == 3):
        eventspacing = counter
        spaces = spaces + 1
      elif (text[counter] == ' ') & (spaces == 4):
        datespacing = counter
        spaces = spaces + 1
      counter = counter + 1
    room = text[:roomspacing]
    device = text[roomspacing+1:devspacing]
    eventname = text[devspacing+1:eventspacing]
    date = text[eventspacing+1:datespacing]
    cond = text[datespacing+1:len(text)-1]
    #device = 'ESP8266ex' #Debugging
    #room = 'LivingRoom' #Debugging
    #eventname = 'eventname'
    #cond = 'When Function'
    #########################################
    def trig(): functrig(room,device,eventname,cond,date)
    global layout
    layout = (cond+' triggered', yellow, 24, trig, globalcounter)
    globalcounter = globalcounter + 1
    #print (roomspacing,devspacing,eventspacing) #Debugging
    #print (room,device,eventname,cond) #Debugging
    #print layout #Debugging
    #trig() #Debugging
    return 1
  ######################################################################################################
  time.sleep(0.5)
  return 0

#while 1: check() #Debugging
#functrig('LivingRoom','ESP8266ex','eventname','When Function') #Debugging
