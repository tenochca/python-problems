#guessinggameone

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

