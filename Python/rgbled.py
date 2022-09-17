import neopixel
from machine import Pin
 
rgbLeds = neopixel.NeoPixel(Pin(0, Pin.OUT), 1)
rgbLeds[0] = (255,0 , 0)
rgbLeds.write()