# What is it?
# You are shown 3 doors. Behind 2 of the doors, there are goats. However behind one of the doors, there is a brand new car. After you select a door, one of the doors revealing a goat will be opened leaving you with 2 options. Do you keep the original door you selected or do you switch?

# The answer.
# You need to switch. 

# Purpose.
# Test out to see randomized outcomes if you stay with the original choice or if you switch. 

# Result
# I don't know if I did the math wrong, but from a purely random standpoint (as random as the python random library can get) it seems to be better to stay with your original choice most of the time.

import random

start = 0
numTimesToRun = 5

switchWins = 0
stayWins = 0

# Goats = 0, 1 & Car = 2
def doorCreation():
    doorsWContents = random.sample(range(3), 3)
    return doorsWContents

def selectingADoor():
    selectDoor = random.randrange(3)
    while selectDoor == 0: selectDoor = random.randrange(3) 
    return selectDoor

def switchDoor(selectedDoor):
    if selectedDoor == 1: selectedDoor = 2
    elif selectedDoor == 2: selectedDoor = 1
    return selectedDoor

while start < numTimesToRun:
    doorsWContents = doorCreation()
    selectedDoor = selectingADoor()
    doorLogic = switchDoor(selectedDoor)

    originalSel = doorsWContents.index(selectedDoor)
    switchedSel = doorsWContents.index(doorLogic)
    goatDoor = doorsWContents.index(0)

    #If you are going to test more than 5, I recommend commenting this chunk out
    print("Run #", start+1)
    print(doorsWContents)
    print("You have selected door #", originalSel+1)
    print("Door #", goatDoor+1, "has a goat")
    print("You have opted to switch to door #", switchedSel+1)

    if switchedSel == doorsWContents.index(2): switchWins += 1
    elif switchedSel == doorsWContents.index(1): stayWins += 1

    start += 1

print("By switching you have won", '{:,}'.format(switchWins), "times")
print("If you stayed on your original selection you would have won", '{:,}'.format(stayWins), "times")
