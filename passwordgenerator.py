""" Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new 
password. Include your run-time code in a main method. """

import random as rd

import string

pool = string.ascii_letters + '0123456789' + "!#$%&'()*+-/:;<=>?@[\]^_~"


def password(k: int):
    'creates a password based on k number of characters'
    passwrd = ''.join(rd.choices(pool, k=k))
    return passwrd

def main():
    print(password(10))

if __name__ == '__main__':    
    main()


