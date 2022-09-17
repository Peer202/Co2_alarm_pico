from machine import Pin
from neopixel import NeoPixel
import time
import math
pin = Pin(1, Pin.OUT)
np = NeoPixel(pin, 12)

def setcolor(colorarray):
    for _i in range(0,12):
        np[_i] = colorarray
        #print("{}:{}".format(_i, np[_i]))
    np.write()

def doweirdmess():
    timeout =  30 + time.time()
    while (timeout > time.time()):
        t =  time.ticks_ms() - timeinit
        red = abs(int(math.sin(t)*150))
        green = abs(int(math.sin(t)*100))
        blue = abs(int(math.cos(t)*100))
        print([red,green,blue])
        setcolor([red,green,blue])
        time.sleep(0.01)

def interpolatecolor(colorold,colornew,interval):
    stepnumber = interval * 1000
    for _i in range(0,3):
        dif = colornew -colorold
        step = dif /stepnumber
    timeout =  stepnumber + time.ticks_ms()
    tickstart = time.ticks_ms()
    colorarray = [0,0,0]
    while (time.ticks_ms() >= timeout):
        for _i in range(0,2):
            colorarray[_i] = colorarray[_i] * ()
    
def breathcolor(colorarray):
    timeinit =  time.time()
    timeout =  30 + time.time()
    while (timeout > time.time()):
        t =  time.time() - timeinit
        sint = abs(math.sin(t))
        genarray = [];
        for _i in range(0,3):
            genarray.append(int(sint * colorarray[_i]))
        
        print("{} : {}".format(genarray,sint))
        setcolor(genarray)
        time.sleep(0.01)
        
breathcolor([155,0,0])
setcolor([0,0,0])