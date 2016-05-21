# import PitftGraphicLib first and initdis() first before usage in code

from PitftGraphicLib import *
screen = pygame.display.set_mode(size)

back = 0
page = 0
class Menusys:
 def __init__(self): pass
 # Slot Configuration
 def slotconf(self,slot,app):
    name = app[0]
    colour = app[1]
    font = app[2]
    run = app[3]
    if slot == 1:
        make_button(name, 25, 75, 27, 130, 5, colour, font, run)
    if slot == 2:
        make_button(name, 165, 75, 27, 130, 5, colour, font, run)
    if slot == 3:
        make_button(name, 25, 112, 27, 130, 5, colour, font, run)
    if slot == 4:
        make_button(name, 165, 112, 27, 130, 5, colour, font, run)
    if slot == 5:
        make_button(name, 25, 149, 27, 130, 5, colour, font, run)
    if slot == 6:
        make_button(name, 165, 149, 27, 130, 5, colour, font, run)
    if slot == 7:
        make_button(name, 25, 186, 27, 130, 5, colour, font, run)
    if slot == 8:
        make_button(name, 165, 186, 27, 130, 5, colour, font, run)

 def layout(self,slotconf,tag,tagcolour,app,others): 
   make_label(tag, 20, 20, 47, tagcolour)
   counter = 1  
   while counter <= 6: #Maximun no. of slots
     if page*6+counter-1 >= len(app): break #Stop at no. of programs
     slotconf(counter, app[page*6+counter-1])
     counter = counter + 1
   def exit(): 
     global back
     back = 1 
   def nextpage():
     clearall()
     global page
     page = page + 1
     Menusys().layout(slotconf,tag,tagcolour,app,others)
     Menusys().check(slotconf,tag,tagcolour,app,others)
     page = page - 1
     clearall()
   if counter > 6: slotconf(8, ('Next', white, 24, nextpage))
   slotconf(7, ('Back', white, 24, exit))
   others()
 
 def check(self,slotconf,tag,tagcolour,app,others):
  while 1:
   clearall()
   Menusys().layout(slotconf,tag,tagcolour,app,others)
   touchdisch()
   global back
   if back == 1: 
     back = 0
     break
  
 def load(self,slotconf,tag,tagcolour,app,others):
  global page
  temp = page
  page = 0
  clearall()
  Menusys().check(slotconf,tag,tagcolour,app,others)
  clearall()
  page = temp

def passs(): pass #Debugging
shit = ('Shit', green, 24, passs) #Debugging
app = (shit,shit,shit,shit,shit,shit,shit,shit,shit,shit) #Debugging

#initdis() #Debugging
menu = Menusys()
#menu.load('Test',cyan,app,passs) #Debuging
