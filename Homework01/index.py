#0 - rock
#1 - Spok
#2 - paper
#3 - lizard
#4 - scissors

#to call function random
import random

#convert name to number using if/elif/else
def name_to_number(name):
    if name == 'rock':
        return int(0)
    elif name == 'Spok':
        return int(1)
    elif name == 'paper':
        return int(2)
    elif name == 'lizard':
        return int(3)
    elif name == 'scissors':
        return int(4)
    else:
#completion of the code execution
        exit("Error, value does not match")

#convert number to name using if/elif/else
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spok'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        exit ('Error, value does not match')

def rpsls(player_choice):
    print ''
    print 'Player chooses', player_choice
#causes a function, convert name to number
    player = name_to_number(player_choice)
#generates random numbers from 0 to 4
    comp = random.randrange(5)
    print 'Computer chooses', number_to_name(comp)
#determines who has won
    res = (player - comp) % 5
    if (res == 1) or (res == 2):
        print 'Player wins!'
    elif player == comp:
        print 'Draw'
    else:
        print 'Computer wins!'

#test your code
rpsls('rock')
rpsls('Spok')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

