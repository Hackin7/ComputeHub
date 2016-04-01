#Do Not Edit
#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
black   = (  0,   0,   0)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
yellow  = (255, 255,   0)
orange  = (255, 127,   0)


#########################################################################
notif = []
def putup(nc): 
  global notif
  #                Notif Structure  (Label, colour, fontsize, setfunction) 
  if nc.check() == 1: notif.insert(0, nc.layout)
#########################################################################
service = [] 
def run(sv):
  global service
  #print service
  if sv.check() == 1: service.insert(0,sv.func)
#########################################################################

###Debugging#############################################################
def code():
  print 'WHAT THE FRUCK IS THIS MOTHERFUCKING SHIT?'
 #Put code to direct to other program

shit = 1
notif = [("F", green, 24, code),("F", blue, 24, code),("F", red, 24, code),("F", cyan, 24, code),("F", yellow, 24, code)]
##########################################################################

######The Service/Notifications List ##### Layout: import (service)######
import CloudComSetup
import IOTNotif
######Layout: (service).setup()########################################### 
def setup():
  IOTNotif.setup()
  CloudComSetup.setup()
#########################################################################

def check():
  ########Notif layout: putup(notif)#####################################
  global notif
  putup(IOTNotif) 
  global shit
  if shit == 1: 
     #Notif Structure  (Label, colour, fontsize, setfunction)       
     notif.insert(0, ("F", green, 24, code))
     shit = 0
  #######################################################################
 
  ########Service layout: run(service)###################################
  global service
  #run(FONAservice)
  #######################################################################
