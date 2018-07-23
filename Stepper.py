import StepLists
import RPi.GPIO as GPIO
import time
from Threader import TaskQueue

ForwardSteps = StepLists.ForwardSteps
BackwardSteps = StepLists.BackwardSteps

class Stepper(object):
    pins = None
    xPos = 0

    def __init__(self, pins):
        self.pins = pins
        self.xPos = 0
        self.q = TaskQueue(1)

    def moveTo(self, targetPos):
        direction = self.determineDirection(targetPos)
        self.moveForwardTo( targetPos) if direction == 'forward' else self.moveBackwardTo(targetPos)

    def determineDirection(self, targetPos):
        return 'forward' if targetPos > self.xPos else 'backward'

    # Directional tick functions
    def moveForwardTo(self, targetPos):
        while self.xPos != targetPos:
            self.tick(ForwardSteps)

    def moveBackwardTo(self, targetPos):
        while self.xPos != targetPos:
            self.tick(BackwardSteps)

    def tick(self, moveList, currentStep = 0):
        numberOfSteps = len(moveList) - 1
        while currentStep != numberOfSteps:
            self.performSingleStep(moveList[currentStep])
            # Wait a bit
            time.sleep(0.0015)
            currentStep += 1
        else:
            self.xPos = self.xPos + 1 if moveList == ForwardSteps else self.xPos - 1

    def performSingleStep(self, step):
        for (ind, val) in enumerate(step):
            if (val == 1):
                GPIO.output(self.pins[ind], True)
            else:
                GPIO.output(self.pins[ind], False)
