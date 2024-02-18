# Guessing Game
import random

print('Hello, what is your name?')
name = input()


print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20) # random number 1 to 20

try:
    for guessesTaken in range(1, 7):  # 1 up to, but not including 7
        print('Take a guesss.')
        guess = int(input())    # ensures argument passed is an integer

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # this condition is for the correct guesses
except ValueError:
        print('That is not a number. Please guess with a number.')
        

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
        
print('You took ' + str(guessesTaken) + ' guesses.')
