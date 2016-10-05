def play():
    import random

    high = 2

    for j in range(2):
        for i in range(5):

            print "high: ", high

            factor1 = random.r  andint(0,10)
            factor2 = random.randint(0,high)
            userAnswer = -1
            correctAnswer = factor1*factor2

            while userAnswer != correctAnswer:
                userAnswer = raw_input("Please enter the product of " +str(factor1) + " and " +str(factor2) + ":")
                try:
                    userAnswer = int(userAnswer)
                    if userAnswer == correctAnswer:
                        print "Correct"

                        if j == 1:
                            high += 5

                    else:
                        print "Incorrect"
                except:
                    print "Enter an integer"


def instructions():
    print "Hello!"
    name = raw_input("what is your name?")
    print "Nice to meet you" ,name,". Let's practice multiplication! I will give you two integers and you give me the product"

def main():
    instructions()
    play()

main()
