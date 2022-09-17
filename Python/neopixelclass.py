from machine import Pin
from neopixel import NeoPixel
import time
import math

class Neopixelobject():
    def __init__(self,Npin,NLeds):
        self.NLeds = NLeds
        self.pin = Pin(Npin, Pin.OUT)
        self.np = NeoPixel(self.pin, NLeds)
    
    def setcolor(self,colorarray,nLEDs):
        if (nLEDs > self.NLeds):
            nLEDs = self.NLeds
        for _i in range(0,nLEDs):
            self.np[_i] = colorarray
        for _i in range(nLEDs + 1,self.NLeds):
            self.np[_i] = [0,0,0]
        self.np.write()
        
