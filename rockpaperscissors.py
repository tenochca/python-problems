#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
#compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

play = 'y'

while play == 'y':
    p1 = str(input('Enter your move p1: '))
    p2 = str(input('Enter your move p2: '))

    if (p1, p2) == ('rock', 'rock') or (p1,p2) == ('scissors', 'scissors') \
        or (p1,p2) == ('paper', 'paper'):
        print('tie')

        play = str(input('would you like to play again? y/n :'))
           
        

    elif (p1, p2) == ('rock', 'scissors') or (p1, p2) == ('scissors', 'paper') \
        or (p1,p2) == ('paper', 'rock'):
        print('p1 wins!')

        play = str(input('would you like to play again? y/n :'))
        


    elif (p2, p1) == ('rock', 'scissors') or (p2, p1) == ('scissors', 'paper') \
        or (p2,p1) == ('paper', 'rock'):
        print('p2 wins!')

        play = str(input('would you like to play again? y/n :'))
        

    