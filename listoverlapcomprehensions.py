#Take two lists and write a program that returns a list that contains only the elements that are 
#common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = list(set([y for x in a for y in b if x == y])) #list comprehension iterates throught items
#in a and b and checks if they are equal. Using a set avoids duplicates
print(common)