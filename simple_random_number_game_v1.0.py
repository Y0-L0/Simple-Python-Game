# Simple random number game 
# By Johannes Lohmer
# Version 1.0

# Random Number = r
# Guess Number = g

# Generate Random Number
import random
r = int(random.randint(1,100))
print("Ready Player One")
# 1st Try

while True:
    try:
        g = int(input("Please Guess the randomly generated number between 1 and 100: "))
        break
    except ValueError:
        print ("are you to dumb to read?")


# Main Loop:
while(r != g):
    g = int(input("Try Again: "))
    if g not in range(1,100):
        print("i guess you are to dumb to read")
    if(g < r):
        print("Wrong, your guess was to low")
    else:
        print("Wrong, your guess was to high")

print("congratulations, you have just proven that you can read and type")
