#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random 

play = 'continue'
randomint = random.randint(1,9)

guess_counter = 0
while play == 'continue':
    guess = eval(input('Guess a number 1-9: '))
    guess_counter += 1
    if guess == randomint:
        print('You guessed right!')
    elif guess > randomint:
        print('You guessed to high!')
    elif guess < randomint:
        print('You guessed to low!')
    
    play = str(input('Continue or exit?: '))

print('number of guesses: ', guess_counter)

