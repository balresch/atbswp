

# This is a guess the number game.
import random
from customprint import print

print("Hello. What is your name?")
name = input()
low = 0
high = 20
secretNumber = random.randint(low, high)
print("Well, " + name + ", I am thinking of a number between " + str(low) + " and " + str(high))

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print("Take a guess.", "jj", "testerinooooopppppppppppppppppp", "asdasdas")
    try:
        guess = int(input())
    except ValueError:
        print("A number, dipshit!")
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # correct guess

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses.")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber) + ".")
