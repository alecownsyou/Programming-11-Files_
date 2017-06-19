import random
import sys 
guessesTaken = 0
guess = 0
print('Hello!')

number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100.')
my_input = input("A)Guess a number\nB)Quit\n")
if my_input.lower()== "a":
    while guessesTaken < 101:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < number:
            print('Your guess is too low.') 

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break
else: 
    my_input.lower()== "b"    
    sys.exit 
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number and guess != 0:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)