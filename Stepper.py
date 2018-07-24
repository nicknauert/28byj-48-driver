import StepLists
import RPi.GPIO as GPIO
import time

ForwardSteps = StepLists.ForwardSteps
BackwardSteps = StepLists.BackwardSteps

class Stepper():
    
    def __init__(self, pins):
        self.pins = pins
        self.xPos = 0
        self.partOfQueue = False
        self.queue = None

    def assignToQueue(self, queue, group):
        self.q = queue
        self.group = group
        self.partOfQueue = True

    def moveTo(self, targetPos):
        steps = self.determineDirection(targetPos)
        while self.xPos != targetPos:
            if self.partOfQueue:
                self.group.queueTask(self.tick, steps)
            else:
                self.tick(steps)

    def determineDirection(self, targetPos):
        return ForwardSteps if targetPos > self.xPos else BackwardSteps

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
            print currentStep
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
