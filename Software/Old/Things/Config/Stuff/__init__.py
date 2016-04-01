#Do Not Edit
#colors     R    G    B
white   = (255, 255, 255)
red     = (255,   0,   0)
green   = (  0, 255,   0)
blue    = (  0,   0, 255)
cyan    = ( 50, 255, 255)
magenta = (255,   0, 255)
orange  = (255, 127,   0)
#Rooms info = [Room name, colour, font]
info = ['Stuff', blue, 24]

import BasicIOex
info.append(BasicIOex.info)

import ESP8266TelnetIOT
info.append(ESP8266TelnetIOT.info)