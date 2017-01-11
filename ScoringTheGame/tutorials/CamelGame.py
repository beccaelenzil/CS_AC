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
        distance =  traveled - nativeDistance
        randint = random.randint(0,21)

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
        elif input == "A":
            drinks += -1
            thirst = 0
            if drinks > 0:
                print "Your thirst has been quenched. You have", drinks, "left in your canteen."
            elif drinks == 0:
                print "You are out of drinks!"
        elif input == "B":
            newtravel = random.randint(5,13)
            traveled += newtravel
            nativeDistance += random.randint(7,14)
            thirst += 1
            tiredness += 1
            print "You traveled", newtravel, "miles"
        elif input == "C":
            newtraveled = random.randint(10,21)
            traveled += newtraveled
            nativeDistance += random.randint(7,14)
            thirst += 1
            tiredness += random.randint(1,4)
            print "You traveled" , newtraveled , "miles"
        elif input == "D":
            tiredness = 0
            nativeDistance += random.randint(7,15)
            print "Your camel is now rested, but the natives are", distance, "miles behind you!"
        elif input == "E":
            print "Miles traveled: " , traveled
            print "Drinks in canteen: ", drinks
            print "The natives are" , distance, "miles behind you"

        if randint == 21:
            print "You have found an oasis! your camel is rested and your thirst is quenched."
            tiredness = 0
            thirst = 0

        if 6 > thirst >= 4:
            print "You are thirsty!"
        elif thirst >= 6:
            print "You died of thirst."
            done = True

        if 8 > tiredness >= 5 and done == False:
            print "Your camel is getting tired!"
        elif tiredness >= 8 and done == False:
            print "Your camel died."
            done = True

        if 10 >= distance < 0 and done == False:
            print "The natives are getting close!"
        elif distance <= 10 and done == False:
            print "The natives have caught up."
            done = True


        if traveled >= 200 and done == False:
            print "You made it across the desert! You won!"

        print

instructions()
camel()
