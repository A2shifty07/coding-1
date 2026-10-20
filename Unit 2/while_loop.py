# loop - a loop is a construct (special function) that repeats
# itself; in programming, a loop allows you to repeat instructions

# There are two types of loops: for loops and while loops

# while loop - a type of loop where, so long as a condition is true,
# it will keep running

# the keyword is while --> do while

# syntax

num = 4
while 2 + 2 == num:  # condition --> operators - must be true
    # print(num == 4)
    print("the program is running...")

# While loops will ALWAYS run unless you change the condition
# We can do this by writing instructions to manually change it

def guessingGame():
    correctanswer = 10
    userGuess = int(input("please type in a number to guess: "))
    attempts = 3

    while userGuess != correctanswer:
        print("sorry that's incorrect")
        print("try again...")
        attempts += 1
        print("number of attempts: " + str(attempts))
        userGuess = int(input("please type in a number to guess: "))

    print("congratulations, you got it correct!")


guessingGame()