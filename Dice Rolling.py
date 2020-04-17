from random import randint

min = 1
max = 6

rollAgain = 'yes'

while rollAgain == 'yes' or rollAgain == 'y':
    print('Rolling the dice....')
    print(randint(min,max))
    rollAgain = input('Do you want to roll again Yes/y: ').lower()