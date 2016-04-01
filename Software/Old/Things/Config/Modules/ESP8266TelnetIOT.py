#Do Not Edit
#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
yellow  = (255, 255,   0)
orange  = (255, 127,   0)

import telnetlib
class Connection():
  def __init__(self,ip): 
    global esp8266
    esp8266 = telnetlib.Telnet(ip)
  def on(self): esp8266.write('output 1')
  def off(self):esp8266.write('output 0')
  def state(self): 
    esp8266.write('shwinput')
    output = esp8266.read_until(" input",1)
    return str(output)

def setup():
  setupstate = 1
  try:
    ip = '192.168.1.13'
    Device = Connection(ip)
  except:
    setupstate = 0
  def setupconf():
    esp8266.write('shwinput')
    output = esp8266.read_until(" input",1)
    state = 0
    if output == '': state = 1
    return state #check whether still connected
  if setupstate == 1:
    no = 0 #can only be 0 or 1
    toggle = [0,1,no,'LED', orange, 24,('LED off', orange, 24, Device.off),('LED on', orange, 24, Device.on)]
    func = ((0,0,'On', orange, 24, Device.on),(0,0,'Off', orange, 24, Device.off),toggle,(1,0,'Button',Device.state, orange, 24))
    info = ('ESP8266ex', 24,'           ',ip, setupconf, func)
  else:
    func = ()
    info = ('ESP8266ex', 24,'            ','No Link',setup, func)
  return info

info = ('ESP8266ex', 24,'           ','extra info',setup,) #Menu Label
