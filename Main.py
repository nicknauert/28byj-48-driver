#!/usr/bin/env python
 
import time
import RPi.GPIO as GPIO
from Stepper import Stepper
from StepperGroup import StepperGroup

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
steppers = [Hori, Vert]

registerGPIO(HPins)
registerGPIO(VPins)

group = StepperGroup(steppers)
group.readGroup()

# Breathe
time.sleep(0.5)

# Main program
# print 'MOVING > h to 200'
Hori.moveTo(-200)
# time.sleep(.5)
# print 'MOVING > v to 50'
Vert.moveTo(50)
# group.joinTasks()
# time.sleep(1)
print 'Resetting steppers'
# Vert.moveTo(0)
# Hori.moveTo(0)
print 'Done'
# exit()
