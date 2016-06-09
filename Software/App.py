import subprocess, os, sys

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

def empty():pass
##################################################
def main():
  #Program launch
  sys.exit()
def exit(): pass
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
Exit = ("Exit", white, 24, main, exit)
###################################
def main():
  #Program launch#############
  os.system('cd Wifi && sudo python Wifi.py &')
def exit(): 
  os.system('pkill -f Wifi.py')
  os.system("sleep 1")
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
Wifi = ("Wifi", green, 24, main, exit)
###################################
def main():
  #Program launch#############
  os.system('cd OpenHAB && sudo python OpenHABUI.py &')
def exit(): 
  os.system('pkill -f OpenHABUI.py')
  os.system("sleep 1")
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
Things = ("OpenHAB", cyan, 24, main, exit)
###################################
def main():
  #Program launch#############
  os.system('cd VNC && sudo python VNC.py &')
def exit(): 
  os.system('pkill -f VNC.py')
  os.system("sleep 1")
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
CloudCom = ("VNC", yellow, 22, main, exit)
###################################
def main():
  #Program launch#############
  os.system('cd Owncloud && sudo python OwncloudUI.py &')
def exit(): 
  os.system('pkill -f OwncloudUI.py')
  os.system("sleep 1")
#Structure  (Label, colour, fontsize, setfunction, exitfunction)       
Owncloud = ("Owncloud", yellow, 22, main, exit)
###################################
def passs(): pass #Debugging
shit = ('Shit', green, 24, passs,passs) #Debugging

#Program layout can be according to piority
programs = [Wifi,Things,CloudCom,Owncloud,Exit]
