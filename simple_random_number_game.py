# Simple random number game 
# By Johannes Lohmer
# Version 2.0

# Random Number = r
# Guess Number = g
# Number of tries = t

# Print Options:

# Instructions for subsequent tries:
subInst = "Try Again: "
# Wrong Input
wrongInp = "Are you to dumb to read?"
# Guess was to high
toHigh = "Wrong, your Guess was to high"
# Guess was to low
toLow = "Wrong, your Guess was to low"
success = "That is correct, Yay"

t = 0

def userInput(instructions):
   while True:
        try:
            global g
            g = int(input(instructions))
            # Check if input is in range
            if g not in range(1,101):
                print(wrongInp)
            else:
                break
        # keep program running in case of non numeric input
        except ValueError:
            print(wrongInp)
   
def checkAnswer(success, toHigh, toLow,):
    global g, t
    t = t + 1
    if(r == g):
        print(success)
    elif(g > r):
        print(toHigh)
    else:
        print(toLow)

# Generate Random Number
import random
r = int(random.randint(1,100))
print("Ready Player One")
print(r)
t = 0
#Initial Instructions
userInput("Please Guess the randomly generated number between 1 and 100: ")
checkAnswer(success, toHigh, toLow)

while((r != g) and (t <= 5)):
    userInput(subInst)
    checkAnswer(success, toHigh, toLow)

while((r != g) and (t <= 9)):
    print("you are either extremely unlucky or you are not using your Head")
    userInput(subInst)
    checkAnswer(success, toHigh, toLow)

while(r != g):
    print("since you have unsucessfully guessed " + str(t) + " times and a smart person needs a maximum of 7 guesses to reach the correct answer, you either dont have a brain or are to lazy to use it")
    userInput("do you really want to try again? ")
    checkAnswer("that is correct, finally using your brain?", toHigh, toLow)
