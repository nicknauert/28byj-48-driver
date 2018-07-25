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
        self.addTask = None

    def assignToQueue(self, queue, addTask):
        self.q = queue
        self.addTask = addTask
        self.partOfQueue = True

    def moveTo(self, targetPos):
        steps = self.determineDirection(targetPos)
        while self.xPos != targetPos:
            if self.partOfQueue:
                self.addTask(self.tick, steps)
            else:
                self.tick(steps)

    def determineDirection(self, targetPos):
        return ForwardSteps if targetPos > self.xPos else BackwardSteps

    # Directional tick functions
    def tick(self, moveList, currentStep = 0):
        numberOfSteps = len(moveList) - 1
        while currentStep != numberOfSteps:
            self.performSingleStep(moveList[currentStep])
            # Wait a bit
            time.sleep(0.0025)
            currentStep += 1
        else:
            self.xPos = self.xPos + 1 if moveList == ForwardSteps else self.xPos - 1

    def performSingleStep(self, step):
        for (ind, val) in enumerate(step):
            if (val == 1):
                GPIO.output(self.pins[ind], True)
            else:
                GPIO.output(self.pins[ind], False)
