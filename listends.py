#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and 
#makes a new list of only the first and last elements of the given list. 
#or practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
new_list = []

def listends(L):
    first = L.pop(0)
    last = L.pop(len(a)-1)
    new_list.extend((first,last))
    print(new_list)

listends(a)

#------------------------------------
#simpler method using list comprehension 

b = [5, 10, 15, 20, 25, 30]

listend = [item for item in b if item == b[0] or item == b[len(b)-1]]
print(listend)