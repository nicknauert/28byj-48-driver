#!/usr/bin/env python
 
import time
import RPi.GPIO as GPIO
from Stepper import Stepper

# Initiate IO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

def registerGPIO(pins):
    for pin in pins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)

HPins = [17, 27, 22, 23]
VPins = [6, 13, 19 , 26]

Hori = Stepper(HPins)
Vert = Stepper(VPins)

registerGPIO(HPins)
registerGPIO(VPins)

# Breathe
time.sleep(0.5)

# Main program
Hori.moveTo(-200)
print 'h 200'
time.sleep(.5)
Vert.moveTo(50)
print 'v 50'
time.sleep(1)
print 'resetting'
Vert.moveTo(0)
Hori.moveTo(0)
print 'done'
exit()
