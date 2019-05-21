import datetime, time, sys

def takeTime():
    timerAmt = input("Hello, welcome to the Timer application. How long would you like to set the timer for? ")
    timerAmt = " " + timerAmt
    return timerAmt

def inputLogic(timerAmt):
    if "min" in timerAmt:
        locationOfMinutes = timerAmt.find("min")
        amountInMinutes = int(locationOfMinutes) - 3

        threeSpotsOfMinutes = [timerAmt[amountInMinutes], timerAmt[amountInMinutes+1], timerAmt[amountInMinutes+2]]
        minutes = int(''.join(threeSpotsOfMinutes))
        
        minutesInSeconds = minutes * 60

    else: minutesInSeconds = 0

    if "sec" or "secs" or "second" or "seconds" in timerAmt:
        locationOfSeconds = timerAmt.find("sec")
        amountInSeconds = int(locationOfSeconds) - 3

        threeSpotsOfSeconds = [timerAmt[amountInSeconds], timerAmt[amountInSeconds+1], timerAmt[amountInSeconds+2]]
        seconds = int(''.join(threeSpotsOfSeconds))

    else: seconds = 0
    
    totalTimeInSeconds = minutesInSeconds + seconds
    return totalTimeInSeconds

def countdown(totalTimeInSeconds):
    timeLeft = totalTimeInSeconds
    print(str(datetime.datetime.now().time()))
    time.sleep(timeLeft)
    print("Timer Complete")
    print(str(datetime.datetime.now().time()))

def main():
    timerAmt = takeTime()
    totalTimeInSeconds = inputLogic(timerAmt)
    countdown(totalTimeInSeconds) 
    anotherInput()

def anotherInput():
    goAgain = input("Would you like to set another timer? ")
    goAgain
    if "NO" or "No" or "no" or "N" or "n" in goAgain:
        print("Have a great day!")
        sys.exit()    
    else:
        main()

main()
