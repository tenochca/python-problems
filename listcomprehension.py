#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [num for num in a if num % 2 == 0] #list comprehension
#for each value(num) in a, if it is even it is added to this list.
#avoids the use of a loop and append statement

print(even)