#!/usr/bin/env python
 
import time
import RPi.GPIO as GPIO
from Movement import registerStepper

# Initiate IO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

HPins = [17, 27, 22, 23]
VPins = [6, 13, 19 , 26]
# definePins(Pins)
Hori = registerStepper(HPins)
Vert = registerStepper(VPins)
print Hori

for pin in HPins:
    print pin
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

for pin in VPins:
    print pin
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
    
# Breathe
time.sleep(0.5)

# Main program
Hori.moveTo(100)
Vert.moveTo(100)
Hori.moveTo(-100)
