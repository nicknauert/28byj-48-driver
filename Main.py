#!/usr/bin/env python
 
import time
import RPi.GPIO as GPIO
from Stepper import Stepper
from StepperGroup import StepperGroup
from threading import Thread
from Threader import createThread, startThread, startAllThreads, clearThreads


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

# Breathe
time.sleep(0.5)

# Main program
createThread(Hori.moveTo, -300)
createThread(Vert.moveTo, 150)
startAllThreads()
clearThreads()

createThread(Vert.moveTo, -150)
startAllThreads()
clearThreads()

createThread(Hori.moveTo, 100)
startAllThreads()
clearThreads()


print('Resetting steppers')
GPIO.cleanup()
print('Done')

