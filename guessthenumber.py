# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
guess_number = 0
secret_number = 0
attempts = 0
restart = 0

# define event handlers for control panel
def init():
    if restart == 0:
        range100()
    else:
        range1000()
    
# button that changes range to range [0,100) and restarts    
def range100():
    global secret_number
    global attempts
    global restart
    n = 100 - 0 + 1
    p = math.log(n , 2)
    attempts = math.ceil(p)
    restart = 0
    secret_number = random.randrange(0, 100)
    print "\nNew Game. Range is from 0 to 100"
    print "Number of remaining guesses is", attempts
    
# button that changes range to range [0,1000) and restarts
def range1000():
    global secret_number
    global attempts
    global restart
    n = 1000 - 0 + 1
    p = math.log(n , 2)
    attempts = math.ceil(p)
    restart = 1
    secret_number = random.randrange(0, 1000)
    print "\nNew Game. Range is from 0 to 1000"
    print "Number of remaining guesses is", attempts

# main game logic goes here	
def get_input(guess):
    global guess_number
    global secret_number
    global attempts
    guess_number = int (guess)
    attempts = attempts - 1
    print "\nGuess was", guess_number
    print "Number of remaining guesses is", attempts
    if attempts > 0:
        if guess_number > secret_number:
            print "Lower!"
        elif guess_number < secret_number:
            print "Higher!"    
    if attempts >= 0:
        if guess_number == secret_number:
            print "Correct!"
            init()
        elif attempts <= 0:
            print "You ran out of guesses. The number was", secret_number
            init()

            
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
button1 = frame.add_button("Range (0, 100)",range100, 200)
button2 = frame.add_button("Range (0, 1000)", range1000, 200)
inp = frame.add_input("Enter Guess", get_input, 200)
button3 = frame.add_button("Restart Game", init, 200)

init()

# start frame
frame.start()
