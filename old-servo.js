const pins = [11, 12, 13, 14];

// The steps required to tick in either direction /////////////////////
const forwardSteps = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
];
const backwardSteps = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]


// The current position of the stepper (not calibrated) //////////////
let xPos = 0;


// The High lvl command to move to a new position //////////////////
function moveTo(targetPos) {
    determineDirection(targetPos) === 'forward' ? moveForwardTo(targetPos) :moveBackwardTo(targetPos);
}

function determineDirection(targetPos) {
    return targetPos > xPos ? 'forward' : 'backward';
}


// Directional ticks ///////////////////////////////////////////////
function moveForwardTo(targetPos) {
    tick(forwardSteps);
    xPos !== targetPos ? moveForwardTo(targetPos) : null;
}

function move(ticks) {
    // 
}

function moveBackwardTo(targetPos) {
    tick(backwardSteps);
    xPos !== targetPos ? moveBackwardTo(targetPos) : null;
}


// Perform the entire stepList i.e. one tick /////////////////////
function tick(stepList, currentStep = 0) {
    const numberOfSteps = stepList.length - 1;
    performSingleStep(stepList[currentStep]);
    // Need a wait time 0.0015;
    currentStep++;
    if (currentStep !== numberOfSteps) {
        tick(stepList, currentStep)
    } else {
        stepList === forwardSteps ? xPos++ : xPos--;
    }
}

function performSingleStep(step) {
    for (i = 0; i < step.length; i++) {
        // step[i] === 1 ? console.log(pins[i], " = ", 1) : null;
    }
}


moveTo(10); 
console.log(xPos);
moveTo(-10);
console.log(xPos);