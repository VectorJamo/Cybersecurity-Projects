# Password cracker
import random

target = 'Aa3'
small_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
domain = ''

# First, check the contents of the password
for c in target:
    if c.islower():
        domain += small_letters
        small_letters = ''
    elif c.isupper():
        domain += capital_letters
        capital_letters = ''
        
    elif c.isnumeric():
        domain += numbers
        numbers = ''

guess = ''
# Then, crack the password
while (guess != target):
    guess = ''
    for x in range(len(target)):
        guess += domain[random.randint(0, len(domain)-1)]


print("Your password is: ", guess)
