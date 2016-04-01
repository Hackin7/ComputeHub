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

def setup():
  setupstate = 1
  #try:
  #  Setup code
  #except Type_of_error_in_setup_code:
  #  setupstate = 0
  import time
  time.sleep(1) #Simulate setup time
  
  def function(): print('Function')
  funct = (0,0,'Function', orange, 24, function)

  no = 0 #Starting State #Should be 0
  def switch1(): print('Switched 1')
  def switch2(): print('Switched 2')
  def switch3(): print('Switched 3')    #Label should indicate state it is in if function used #Can have any no of toggle states 
  toggle = [0,1,no,'Output', orange, 24,('Output 1', orange, 24, switch1),('Output 2', orange, 24, switch2),('Output 3', orange, 24, switch3)]
  
  def inputch(): return('Random')
  input = (1,0,'Input',inputch, orange, 22)

  global func
  global info
  if setupstate == 1:
    func = (funct,toggle,input)
    info = ('BasicIOex', 24,'           ','extra info', setup, func)
  else:
    func = ()
    info = ('BasicIOex', 24,'       ','Not Connected',setup, func)
  return info

#Layout = (name, fontsize,spacing,extrainfo,setupfunction)
info = ('BasicIOex', 24,'           ','extra info',setup) #Menu Label