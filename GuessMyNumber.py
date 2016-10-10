#enhancements: the user enters how many guesses they would like and then the computer gives you that many guesses
def play():
    import random

    useranswer = -1
    correctanswer = random.randint(0, 100)

    score = raw_input('how many guesses do you think you can get it in?')
    while score.isdigit() == False:
        score = raw_input('enter a number. how many guesses do you think you can get it in?')

    score = int(score)


    print "okay cool, you have", score, "guesses to win"

    while score > 0 and useranswer != correctanswer:
        print "guesses remaining =", score
        useranswer = raw_input("enter your guess")
        try:
            useranswer = int(useranswer)
            if useranswer == correctanswer:
                print "you win"
            elif useranswer > correctanswer:
                print "too high"
                score += -1
            else:
                print "too low"
                score += -1
        except:
            print "enter an integer"


    if score == 0:
        print "you lose, try taking more guesses next time"



def instructions():
    print "I'm thinking of a number between 1 and 100. If you can guess my number, you win!"

def main():
    instructions()
    play()

main()
