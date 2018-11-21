# mini-project "Guess the number"
# input will come from buttons and an input field

import simplegui
import random
import math

# global variables

num_range = 100
secret = 0
user_guess = 0
num_guesses = 7

# helper function to start and restart the game
def new_game ():
    global secret, num_guesses
    secret = random.randrange(0, num_range)

#sets number of guesses based on range
    if num_range == 100:
        num_guesses = 7
    elif num_range == 1000:
        num_guesses = 10

    print ''
    print 'A new game has started with a range from 0 to', num_range
    print 'You have', num_guesses, 'guesses remaining'

# helper function to decrement guesses remaining
def decrement_guesses ():
    global num_guesses
    num_guesses = num_guesses - 1

    if num_guesses == 0:
        print ''
        print 'End of the game, You lose'
        print 'Secret number', secret
        new_game ()
    else:
        print 'Remaining guesses', num_guesses

# event handlers for control panel
def range_100 ():
    global num_range
    num_range = 100
    new_game ()

def range_1000 ():
    global num_range
    num_range = 1000
    new_game ()

# player number input function
def input_guess(guess):
    global user_guess
    user_guess = int(guess)
    print ''
    print 'Your guess was', guess

# determining the entered number
    if (user_guess >= num_range) or (user_guess < 0):
        print 'Incorrect value, enter a number from 0 to', num_range
    elif user_guess == secret:
        print 'You win!'
        new_game ()
    elif user_guess > secret:
        print 'Lower!'
        decrement_guesses ()
    else:
        print 'Higher'
        decrement_guesses ()

# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements
frame.add_button ('Range [0, 100]', range_100, 200)
frame.add_button ('Range [0, 1000]', range_1000, 200)
frame.add_input('Enter guess', input_guess, 50)

# call new_game and start frame
new_game()
frame.start()
