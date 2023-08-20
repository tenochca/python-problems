#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.

def reverse(s):
    'takes a string a reverses the word order'
    if len(s) == 1:
        return s[0]
    else:
        firstitem = s[0]
        s.remove(firstitem)
        x = reverse(s) + ' ' + firstitem
        return x
    

string = (input('Enter a sentence: ')).split()
print(reverse(string))

#----------------------------------------------#
#non recursive method

def reversal(s):
    reversedlist = s[::-1]
    finalstring = ' '.join(reversedlist)
    return finalstring

sentence = (input('Enter a sentence: ')).split()
print('regular way: ', reversal(sentence))

