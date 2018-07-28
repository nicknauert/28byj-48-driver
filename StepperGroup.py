class StepperGroup():

    def __init__(self, steppers):
        self.steppers = steppers
        self.numberOfSteppers = len(self.steppers)
        self.q = self.createQueue(self.numberOfSteppers)
        for stepper in self.steppers:
            print(stepper)
            stepper.assignToQueue(self.q, self.queueTask)

    def readGroup(self):
        print('We got ' + str(self.numberOfSteppers) + ' steppers here.')
        print(self.q)
    
