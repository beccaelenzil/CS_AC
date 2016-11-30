import random

def instructions():
    print "Welcome to Camel!"
    print "You have stolen a camel to make your way across the great Mobi desert."
    print "The natives want their camel back and are chasing you down! "
    print "Survive your desert trek and outrun the natives."

def camel():
    done = False
    traveled = 0
    thirst = 0
    tiredness = 0
    nativeDistance = -20
    drinks = 3

    while done == False:
        print "A. Drink from your canteen."
        print "B. Ahead moderate speed."
        print "C. Ahead full speed."
        print "D. Stop for the night."
        print "E. Status check."
        print "Q. Quit."
        print
        input = raw_input("Your Choice? ")
        print
        input = input.upper()
        if input == "Q":
            done = True
        elif input == "B":
           traveled += random.randint(5,13)
           nativeDistance += random.randint(7,15)
           thirst += 1
           tiredness += 1
        elif input == "C":
           traveled += random.randint(10,21)
           nativeDistance += random.randint(7,15)
           thirst += 1
           tiredness += random.randint(1,4)
        elif input == "D":
            tiredness = 0
            nativeDistance += random.randint(7,15)
            print "Your camel is now rested, but the natives are", nativeDistance*-1, "miles behind you!"
        elif input == "E":
            print "Miles traveled: " , traveled
            print "Drinks in canteen: ", drinks
            print "The natives are" , nativeDistance*-1, "miles behind you"

        print


instructions()
camel()
