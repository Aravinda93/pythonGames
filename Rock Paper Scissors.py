from random import randint

print('---- Welcome to Rock Paper Scissors Game ----')
print('You will be playing against the computer for best of 3')

computerOptions = ['Rock', 'Paper', 'Scissors']
userOption = ''
computerChoosen = ''
computerCount = 0
userCount = 0

def validatorLogic():
    global computerCount,userCount
    global computerChoosen, userOption
    if userOption == 'rock' or userOption == 'paper' or userOption == 'scissors':
        if userOption == computerChoosen:
            print('You and computer both choosen same', userOption)
        elif userOption == 'rock' and computerChoosen == 'paper':
            print('You lost because ',computerChoosen, ' covers ', userOption)
            computerCount += 1
        elif userOption == 'paper' and computerChoosen == 'rock':
            print('You win because ',userOption,' covers ',computerChoosen)
            userCount += 1
        elif userOption == 'scissors' and computerChoosen == 'rock':
            print('You lost because ', computerChoosen, ' crushes ', userOption)
            computerCount += 1
        elif userOption == 'rock' and computerChoosen == 'scissors':
            print('You win because ',userOption,' crushes ',computerChoosen)
            userCount += 1
        elif userOption == 'paper' and computerChoosen == 'scissors':
            print('You lost because ', computerChoosen, ' cuts ', userOption)
            computerCount += 1
        elif userOption == 'scissors' and computerChoosen == 'paper':
            print('You win because ', userOption, ' cuts ', computerChoosen)
            userCount += 1
    else:
        userOption = input('Please Enter: Rock/Paper/Scissors: ').lower()
        validatorLogic()

def bestOfThree():
    global computerChoosen,userOption
    global computerCount, userCount
    validator = True
    for i in range(0,3,1):
        computerChoosen = computerOptions[randint(0, 2)].lower()
        userOption = input('Please Enter: Rock/Paper/Scissors: ').lower()
        validatorLogic()

    print('');
    if(computerCount > userCount):
        print('You lost the series ',userCount,' - ',computerCount)
    elif(computerCount < userCount):
        print('You won the series ', userCount, ' - ', computerCount)
    else:
        print('Series is Drwan ',computerCount,' - ',userCount)


bestOfThree()