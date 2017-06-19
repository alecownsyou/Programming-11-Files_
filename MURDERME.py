import random
my_number = random.randrange(1, 101)
guessesTaken = 0
print("help")
my_input = input("A)Guess a number\nB)Quit\n")
if my_input.lower()== "a":
    My_number=input("Guess a number between 0 and 100!\n")
    
    while guessesTaken < 1000:
	print('Take a guess.') 
	guess = input()
	guess = int(guess)
	guessesTaken = guessesTaken + 1
	    
	if guess < number:
	    print('Your guess is too low.')
	
	if guess > number:
	    print('Your guess is too high.')
		
	if guess == number:
	    guessesTaken = str(guessesTaken)
	    print('Good job, ! You guessed my number in ' + guessesTaken + ' guesses!')
	    break


if My_input.lower() == "b":
    done = False
    if quit == "b":
    	done = True