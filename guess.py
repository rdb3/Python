# This is a guess the number game.
import random

guessesTaken = 0 # Var dec, counter for while loop (player gets 6 guesses)

print('"Now hello there! What is your name?" the kind wizard, Potts, inquires.')
myName = input() # Dec var, run function that evals to the str that stores in var

number = random.randint(1, 20) #Program determines the number the player will be guessing

print('"Well, ' +myName + ', I am thinking of a number between 1 and 20" he teases with a wink.')
print()

while guessesTaken < 6: #At first run of this loop, guessesTaken = 0. This loop will not run if player has guessed 6 times, game over 

    if guessesTaken == 0:
        print('"Care to take a guess? ;)"') # There are four spaces in front of print.
    else:
        print('"Why don\'t we try again? ;)"')
        
    guess = input()
    guess = int(guess) #Takes the str the user inputs, and converts it to an integer that python can use to compare

    guessesTaken = guessesTaken + 1 # adds to the counter, the player has guessed

    if guess < number:
        print('"Err.., no. That guess was too low."') # There are eight spaces in front of print
        print()
        
    if guess > number:
        print('"Err.., no. That guess was too high."')
        print()
        
    #Goes back to the top and runs loop again until either number is guessed, or counter hits 6

    if guess == number:
        print() #newline for formatting,
                #basically, anything after this will have a newline before it
                #works well because it works for if the player loses too.
        break #Immediately breaks while loop, moves execution down below the loop now

if guess == number: #i.e. player has won
        guessesTaken = str(guessesTaken)
        print('"Good job, my ' + myName + '! It only took you ' + guessesTaken + ' guesses!')
        print('"Bless you and your kin, and may you live well and peacefully!"')
        print('"I must be going now, but it has been a pleasure. Until next time. Adieu!"')

if guess != number: #i.e. player has lost, does not equal number
        number = str(number)
        print('"The number I was thinking of was ' + number + '. Don\'t worry, we can always play again!"')
        print('"How\'ere, for now, I must be off!"')
        print('"For now, adieu."')

print()
print('...and *POOF!* THE WIZARD WAS GONE.')
