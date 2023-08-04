#Ask the user for a string and print out whether this 
#string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

#NOTE: I wanted to mess around using recursion with this. A non recursive solution is below this one

string =  eval(input('Input a word: ')) #asks user for input
stringlist = list(string) #converts string into list

def reverse(L): #recurive function to reverse list
    if len(L) == 1:
        return L #base case
    else:
        x = L[0] #fist item gets removed
        L.remove(x)
        reverse(L).append(x) #function calls itself and appends fist item
        return L #return new list
    
reversed_string = reverse(stringlist) #call recurive functuon on stringlist

print(stringlist)
print(reversed_string)

if reversed_string == stringlist: #if the reversed list and string list are equal
    print('This is a palindrome')
else:
    print('This is not a palindrome')


#alternative way--------------------------------------------------------------------

wrd = str(input('input a word: '))

reverse = wrd[::-1] #this slices the input backwards
if reverse == wrd: #if the input and reversed input are the same
    print('This is a palindrome')
else: #if they are not the same
    print('This is not a palindrome')