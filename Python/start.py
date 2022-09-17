import neopixelclass
import mhzclass
from machine import Pin
import time

LEDRing = neopixelclass.Neopixelobject(Npin = 1,NLeds = 12)
sensor = mhzclass.MHZ19BSensor(tx_pin = Pin(4),rx_pin = Pin(5),co2_yellow = 700,co2_red = 1200,neopixelobject = LEDRing)
timeout = time.time() + (20 * 60 * 60)
while (time.time() <= timeout):
    sensor.measure()
    time.sleep(5)
    