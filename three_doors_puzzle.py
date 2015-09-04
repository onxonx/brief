#!/usr/bin/env python3
 
import random
 
# all possible combinations, 1 is the door with prize, 0-empty door
cases = [(1,0,0),(0,1,0),(0,0,1)]
 
def man_guess(switch):
    # randomly select on of 3 possible combinations with the doors
    case = random.randint(0, 2)
 
    # randomly make a choice for the contestant
    guess = random.randint(0, 2)
 
    # find the empty door to open for contestant
    show = guess
    while show == guess or cases[case][show] == 1:
        show = random.randint(0, 2)
 
    # switch or not
    if switch:
        guess = next(
            i for i,x in enumerate(cases[case]) if i not in [guess, show]
        )
 
    # return the doors combination and the final pick from contestant
    return cases[case], guess
 
 
def check(count, switch):
    guesses = 0
    for i in range(count):
        case, guess = man_guess(switch=switch)
        if case[guess] == 1:
            guesses += 1
 
    # return ratio of success
    return guesses/count
 
 
print("Don't switch:", check(1000, switch=False))
print("Switch      :", check(1000, switch=True))

