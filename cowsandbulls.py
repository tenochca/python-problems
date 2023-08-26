'''Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.'''

import random

def cowNbull():

    rand_num = random.choices('0123456789', k=4) #creating random number
    print(rand_num)

    while True: 
        cow = 0 #init counter variables
        bull = 0
        guesses = 0

        guess = list(input('Guess a 4-digit number: ')) 
        guesses = guesses + 1 #count each guess


        jointList = [[a,b] for a,b in zip(guess, rand_num)]
        #list comprehension joins the two lists into a two-dimensional list
        #where each sublist is a guess/number pair

        for a,b in jointList: #iterating through the pairs
            if a == b: #if the pair is equal
                cow = cow + 1 #add a cow
            elif a in rand_num: #else if the guess is just in rand_num
                bull = bull + 1 #add a bull
    
        print(cow, 'cows, ', bull, 'bulls') #print the cow/bull results


        if cow == 4: #once there are 4 cows the game is over
            print('You won!')
            break   


if __name__ == '__main__':
    print("Welcome to the cows and bulls game :)")
    cowNbull()
    