#Ask the user for a number and determine whether the number is prime or not. 

divisors = [] #init empty list to hold divsors
def prime_num(x):
    num_list = list(range(1,x+1)) #list of numbers leading up to x
    for i in num_list: #iterating through the list
        if x%i == 0: #if the number is a divisor of x
            divisors.append(i) #add to the list
    if len(divisors) == 2: #outside the loop, if the len of the list = 2
        print('Prime') #the number is prime
    else:
        print('Composite') #otherwise it is composite

num = eval(input('Enter a number: '))
prime_num(num)
