# Simple random number game 
# By Johannes Lohmer
# Version 1.2

# Random Number = r
# Guess Number = g

# Generate Random Number (step1)
import random
r = int(random.randint(1,100))
g = 0

# Main Loop:
while(r != g):

    # User Input: 
    while True:
        try:
            g = int(input("Please Guess the randomly generated number between 1 and 100: "))
            # Check if input is in range
            if g not in range(1,101):
                print("Wrong Input!")
            else:
                break
        # keep program running in case of non numeric input
        except ValueError:
            print("Wrong Input!")

    # Game Output: (step3)
    if(r == g):
        print("You win")
        input("thank you for playing, press any key to exit the program")
    elif(g > r):
        print("Sorry, your guess was to high")
    else:
        print("Sorry, your guess was to low")
