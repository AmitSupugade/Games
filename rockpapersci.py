# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# number_to_name - Converts number to name
def number_to_name(number):
    if number == 0:
        name = "rock"
    
    elif number == 1:
        name = "Spock"
    
    elif number == 2:
        name = "paper"
    
    elif number == 3:
        name = "lizard"
    
    elif number == 4:
        name = "scissors"
    
    else:
        name = "incorrect choice"
    
    return name
    
# name_to_number - Converts name to number
def name_to_number(name):
    if name == "rock":
        number = 0
        
    elif name == "Spock":
        number = 1
        
    elif name == "paper":
        number = 2
        
    elif name == "lizard":
        number = 3
        
    elif name == "scissors":
        number = 4
        
    else:
        number = 5
        
    return number

def rpsls(name):
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    if player_number == 5:
        print "Incorrect choice"
        
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    
    # compute difference of player_number and comp_number modulo five
    result = (player_number - comp_number) % 5
    
    if result < 3:
        winner = "Player"
        
    else:
        winner = "Computer"
    
    # convert comp_number to name using number_to_name
    print "\n" + "player chooses-" + number_to_name(player_number)
    print "computer chooses-" + number_to_name(comp_number)
    
    # print results
    if result == 0:
        print "Player and Computer tie!"
    
    else:
        print winner + " wins!"
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

