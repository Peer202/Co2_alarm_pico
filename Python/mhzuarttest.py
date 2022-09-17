from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

uart1.write(b"\xff\x01\x86\x00\x00\x00\x00\x00\x79")
time.sleep(0.1)
rxData = bytes()
while uart1.any() > 0:
    rxData += uart1.read(1)

if (rxData is ""):
    print("rxdata empty")
    
ppm = ord(chr(rxData[2])) * 256 + ord(chr(rxData[3]))
print(ppm)
