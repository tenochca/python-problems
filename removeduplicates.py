#Write a program (function!) that takes a list and returns 
#a new list that contains all the elements of the first list minus all the duplicates.

l = [1,2,2,3]

def dupe(L):
    'takes a list and removes duplicates'
    new_l = list(set(l))
    return new_l

print('set method: ', dupe(l))

#--------------------------#
#method using a loop

new_list = []
for i in l:
    if i not in new_list:
        new_list.append(i)
    else:
        pass

print('loop method: ', new_list)
    
