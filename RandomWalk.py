# python 2
#
# Homework 5, Problem 1
#
# Name: Alison Cohen
#

import random
import time

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos( start, nsteps ):
    """ Function that simulates a sleepwalker. The sleepwalker starts at start, an integer representing
    the starting location. For nseteps number of steps, the sleep walker takes a random step either
    forwards or backwards.
    """
    position = start
    print "starting postion:" , position
    for i in range(nsteps):
        position += rs()
        print "current postion:" , position
    return position

#print rwpos(40, 4)

def rwsteps( start, low, high ):
    """Function that simulates a sleepwalker. an integer start, representing the starting position of
    our sleepwalker, an integer low, which  will always be nonnegative, representing the smallest value
    our sleepwalker will be allowed to wander to, and an integer hi, representing the highest value our
    sleepwalker will be allowed to wander to. Prints a visual representation of the position."""

    position = start
    counter = 0

    while position != low and position != high:
        beforespaces = position - low - 1
        afterspaces = high - position - 1
        print "|" , " "*beforespaces, "S" , " "*afterspaces , "|"
        position += rs()
        counter += 1
        #time.sleep(0.1)

    return counter

rwsteps( 10, 5, 15 )

def rwposPlain(start, nsteps):
    """ Function that simulates a sleepwalker. The sleepwalker starts at start, an integer representing
    the starting location. For nseteps number of steps, the sleep walker takes a random step either
    forwards or backwards.
    """

    position = start

    for i in range(nsteps):
        position += rs()

    return position

#print rwposPlain(40, 4)

def ave_signed_displacement( numtrials ):
    """
    takes in number of simulations of 100 steps
    returns average distance from start
    """
    posList= []

    for n in range(numtrials):
        pos = rwposPlain(0, 100)
        posList.append(pos)
    avePos = sum(posList)/float(numtrials)
    return avePos

print ave_signed_displacement( 1000 )


def ave_squared_displacement( numtrials ):
    """
    takes in number of simulations of 100 steps
    returns average distance squared from start
    """
    posList= []

    for n in range(numtrials):
        pos = rwposPlain(0, 100)
        posList.append(pos**2)
    avePos = sum(posList)/float(numtrials)
    return avePos

print ave_squared_displacement(50)

"""
1) The average signed displacement after 100 steps is 0. The average signed displacement after N steps is 0.
2) The average squared displacement after 100 steps is 100. The average squared displacement after N steps is N.
"""


