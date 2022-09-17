
from machine import Pin
from machine import UART
import time
import dht
import machine


class MHZ19BSensor:

    # initializes a new instance
    def __init__(self, tx_pin, rx_pin,co2_yellow,co2_red,neopixelobject):
        self.uart = UART(1, baudrate=9600, bits=8, parity=None, stop=1, tx=tx_pin, rx=rx_pin)
        self.co2_yellow= int(co2_yellow)
        self.co2_red= int(co2_red)
        self.neopixel = neopixelobject
    
    # measure CO2
    def measure(self):
        while True:
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep(1)  # in seconds

            # read and validate the data
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break

            # retry if the data is wrong
           
            print('error while reading MH-Z19B sensor: invalid data')
            print('retry ...')


        co2 = buf[2] * 256 + buf[3]
        print('co2         = %.2f' % co2)
        
        self.setlights(co2)
    # check data returned by the sensor
    def is_valid(self, buf):
        if buf is None or buf[0] != 0xFF or buf[1] != 0x86:
            return False
        i = 1
        checksum = 0x00
        while i < 8:
            checksum += buf[i] % 256
            i += 1
        checksum = ~checksum & 0xFF
        checksum += 1
        return checksum == buf[8]
    
    #sets the lights in a nice way to indicate the current state of the air
    def setlights(self,co2):        
        
        if (co2 < self.co2_yellow):
            
            greensteps =  self.neopixel.NLeds / self.co2_yellow
            leds = round(greensteps * co2)
            self.neopixel.setcolor([0,100,0],leds)
            
        elif(co2 >= self.co2_yellow and co2 <= self.co2_red):
            
            yellowsteps = self.neopixel.NLeds / (self.co2_red - self.co2_yellow)
            leds = round(yellowsteps * (co2 - self.co2_yellow))
            self.neopixel.setcolor([161,80,0],leds)
            
        elif(co2 >= self.co2_red):
            
            redsteps = self.neopixel.NLeds / 1000
            leds = round(redsteps *(co2 - self.co2_red))
            self.neopixel.setcolor([100,0,0],leds)

        
        