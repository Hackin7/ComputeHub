#Things Internet Link service backend
import os
import subprocess
import time
import Config
#####Time Date check#########################
import time
import datetime
#############################################

noconnectthings = []
class Things:
 def __init__(self): pass
 
 def setup(self):
   #####Rooms#################################################
   os.system('mkdir /tmp/Things ')
   os.system('mkdir /tmp/Things/System')
   os.system('echo "0" > /tmp/Things/System/Restarted')
   counter = 0
   while counter < len(Config.things):
     os.system('mkdir /tmp/Things/'+Config.things[counter][0])
     counter = counter + 1
   #####Compilation##########################################
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
     thing.insert(0,name)
     thing.insert(1,colour)
     #########Add Thing######################################
     things.append(thing)
     ####Debugging###########################################
     #print roomcheck
     #print counter-1+3 
     #print Config.things[roomcheck][counter-1+3]
     ########################################################
     counter = counter + 1
   #####Device###############################################
   counter = 0
   setupthings = []
   while counter <= len(things)-1:
     #####Prepare Functions##################################
     name = things[counter][0]
     colour = things[counter][1]
     thing = list(things[counter][6]()) #Setup
     thing.insert(0,name)
     thing.insert(1,colour)
     ########################################################
     setupthings.append(thing) #Check Link
     counter = counter + 1
   ##########################################################
   return setupthings

 def load(self,config, things):
   #####Easy Indentification#################################
   room = config[1]
   device = config[2]
   function = config[3]
   #####Device###############################################
   counter = 0
   while not((list(room) == things[counter][:2]) & (list(device[:2]) == things[counter][2:4])):
     #print (list(room) == things[counter][:2]) #Debugging
     #print (list(device[:2]) == things[counter][2:4]) #Debugging
     counter = counter + 1
   device = things[counter]
   setup = device[6]
   #####Function#############################################
   functions = device[7]
   counter = 0
   if len(functions) == 0:
       Things().noconnect(device[2],room[0])
       return 2
   while True:
    if function[0] == 0: #Set Output mode
      if function[1] == 0: #Function
        comparison = (function == functions[counter][:5])
      if function[1] == 1: #Toggle Mode
        comparison = (function == functions[counter][:6])
    else: #Show Input Mode
      if function[1] == 0: #Show
        comparison = (function == functions[counter][:3])
    if comparison:
       function = device[7][counter]
       break
    counter = counter + 1
   ##########################################################
   return function,setup
 
 def noconnect(self,device,room):
   global noconnectthings
   counter = 0
   while counter < len(noconnectthings):
       if noconnectthings[counter] == (device,room): break
       counter = counter + 1
   if counter >= len(noconnectthings):
     os.system('echo "'+device+' '+room+'" > /tmp/Things/System/NoConnect'+str(len(noconnectthings)))
     print('The '+device+' in '+room+' is not connected and the corrosponding function cant be run') #Debugging
     noconnectthings.append((device,room))

firsttry = 0
triggered = 0
class IFTTT:
 def __init__(self): pass

 def triggerset(self):
   #####Compilation##########################################
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
     thing.insert(0,name)
     thing.insert(1,colour)
     #########Add Thing######################################
     things.append(thing)
     ####Debugging###########################################
     #print roomcheck
     #print counter-1+3 
     #print Config.things[roomcheck][counter-1+3]
     ########################################################
     counter = counter + 1
   #####Devices##############################################
   counter = 0
   while counter < len(things):
     os.system('mkdir /tmp/Things/'+things[counter][0]+'/'+things[counter][2])
     counter = counter + 1
   ###########################################################
  
 def assign(self,thing,function,setup):
   if thing[3][0] == 0: #Set Output mode
      if thing[3][1] == 0: #Function (input/output,mode,label,colour,font,function)
        if (thing[4][1] == 0) & (thing[4][2] == 'Do '+thing[3][2]): config = 'ok1'
        if (thing[4][1] == 1) & (thing[4][2] == 'When '+thing[3][2]): config = IFTTT().triggercheck(thing[1][0],thing[2][0],thing[3][2],'1',1,thing[4][0],setup,thing[4][2])
      if thing[3][1] == 1: #Toggle Mode
        if (thing[4][1] == 0) & (thing[4][2] == 'Do '+function[6+(thing[4][3])][0]): config = 'ok3'
        if (thing[4][1] == 1) & (thing[4][2] == 'When '+function[6+(thing[4][3])][0]): config = IFTTT().triggercheck(thing[1][0],thing[2][0],thing[3][3],str(thing[4][3]),1,thing[4][0],setup,thing[4][2])
   else: #Show Input Mode
      if thing[3][1] == 0: #Show
        if (thing[4][1] == 1) & (thing[4][2][:(len(thing[3][2])+4)] == thing[3][2]+' == '): config = IFTTT().inputtriggerch(thing[1][0],thing[2][0],thing[3][2],function[3],thing[4][2][(len(thing[3][2])+4):],1,thing[4][0],setup,thing[4][2])
        if (thing[4][1] == 1) & (thing[4][2][:(len(thing[3][2])+4)] == thing[3][2]+' != '): config = IFTTT().inputtriggerch(thing[1][0],thing[2][0],thing[3][2],function[3],thing[4][2][(len(thing[3][2])+4):],0,thing[4][0],setup,thing[4][2])
   return (thing[4][1],config)

 def triggercheck(self,room,device,function,condition,condtype,eventname,setup,cond):
   def check(): 
     text = subprocess.Popen(["cat","/tmp/Things/"+room+"/"+device+"/"+function],stdout=subprocess.PIPE).stdout.read().decode()
     if condtype == 1: boolean = (text[:len(text)-1] == condition)
     else: boolean = (text[:len(text)-1] != condition)
     if boolean:
        os.system("rm -rf /tmp/Things/"+room+"/"+device+"/"+function)
        print 'GOOD' #Debugging
        os.system('curl -X POST https://maker.ifttt.com/trigger/'+eventname+'/with/key/'+Config.IOT.iftttkey) #Trigger
        IFTTT().notetrigger(room,device,eventname,cond)
   return (check,room,device,setup)
  
 def inputtriggerch(self,room,device,name,function,condition,condtype,eventname,setup,cond):
    def check():
      output = function()
      if condtype == 1: boolean = (output == condition)
      else: boolean = (output != condition)
      print output#boolean #Debugging
      text = subprocess.Popen(["cat","/tmp/Things/"+room+"/"+device+"/"+name+"1"],stdout=subprocess.PIPE).stdout.read().decode()
      if boolean & (text[:len(text)-1] != output):
        os.system('echo "'+output+'" > /tmp/Things/'+room+'/'+device+'/'+name+"1")
        print 'GOOD' #Debugging
        os.system('curl -X POST https://maker.ifttt.com/trigger/'+eventname+'/with/key/'+Config.IOT.iftttkey) #Trigger
        IFTTT().notetrigger(room,device,eventname,cond)
      if (not boolean) & (text[:len(text)-1] != output): os.system('echo "'+output+'" > /tmp/Things/'+room+'/'+device+'/'+name+"1")
    return (check,room,device,setup)

 def notetrigger(self,room,device,eventname,cond):
   date = str(datetime.date.today())+'-'+str(datetime.datetime.now().time())[0:8]
   global triggered
   #print room,device,eventname,cond #Debugging
   os.system('echo "'+room+' '+device+' '+eventname+' '+date+' '+cond+'" > /tmp/Things/System/Triggered'+str(triggered))
   os.system('echo "activity.insert(0,'+str((cond+' Triggered',device,room,date))+')" >> Config/Activity.py')
   print(cond+' has been triggered') #Debugging
   triggered = triggered + 1
 
 def assignment(self):
    ifttttriggers = []
    iftttactions = []
    IFTTT().triggerset()
    counter = 0
    while counter <= len(Config.IOT.ifttt)-1:
      function =  Things().load(Config.IOT.ifttt[counter], things) #Function to access
      if function != 2: 
        config = IFTTT().assign(Config.IOT.ifttt[counter],function[0],function[1])
        #print config #Debugging
        if config[0] == 0: iftttactions.append(config[1]) #Action
        elif config[0] == 1: ifttttriggers.append(config[1]) #Trigger
      counter = counter + 1
    return (ifttttriggers,iftttactions)

 def allcheck(self,ifttttriggers,iftttactions):
    global firsttry
    #####IFTTT Triggers############################################################
    counter = 0
    while counter < len(ifttttriggers):
      if ifttttriggers[counter][3]() == 1:
         if firsttry != 0:
             Things().noconnect(ifttttriggers[counter][2],ifttttriggers[counter][1])
             ifttttriggers.remove(ifttttriggers[counter])
      else: ifttttriggers[counter][0]()
      time.sleep(0.1) #Delay to prevent overuse of CPU 
      counter = counter + 1
    ###############################################################################

things = Things().setup()
#print things #Debugging

ifttt = IFTTT()
iftttassigned = ifttt.assignment()
while True:
    ifttt.allcheck(iftttassigned[0],iftttassigned[1])
    if firsttry == 0: firsttry = 1
