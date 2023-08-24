#Write a program that asks the user how many 
#Fibonnaci numbers to generate and then generates them.

def fibonacci(n):
    'outputs fibonacci numbers up to the nth term'
    if n == 1: #base cases if the user inputs 1 or 2
        return [1]
    elif n == 2:
        return [1,1] #sequence starts with these two numbers
    else:
        fib = fibonacci(n-1) #recursive call
        fib.append(fib[-1] + fib[-2]) #calculates and appends the next num
        return fib #return the final list
    
def main():  
    n = eval(input('Enter the number of fibonacci numbers to generate: '))
    fib_list = fibonacci(n)
    print(fib_list)
    return fib_list

if __name__ == '__main__':
    main()

