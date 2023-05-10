# i have used random library it is inbuilt library of python
import random

print('Welcome to your Password Generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*.,()?0123456789'

number=input("Amount of passwords to generator") 
#number variable will take input from user how many passwords you need
number=int(number)

length=input('Input your password length:')
#length variable will ask how many character length you need to make a password
length=int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords= ''
    for c in range(length):
        passwords+=random.choice(chars)
    print("password is ",passwords)