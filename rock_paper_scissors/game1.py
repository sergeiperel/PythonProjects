import random


def game():
    num = random.randint(1, 3)
    if num == 1:
        return 'rock'
    elif num == 2:
        return 'paper'
    else:
        return 'scissors'


def input_data():
    possibleWords = ['paper', 'scissors', 'rock']
    while True:
        input_word = input()
        if input_word not in possibleWords:
            print('Incorrect input! Try again!')
        else:
            break
    return input_word


def determine_winner(compTurn, myTurn):
    global myWin, compWin, draw
    if myTurn == 'rock':
        if compTurn == 'scissors':
            myWin += 1
            print('You won, rock beats scissors!')
        elif compTurn == 'paper':
            compWin += 1
            print('Computer won, paper wraps stone!')
        else:
            draw += 1
            print('Draw! We both chose the rock!')
    elif myTurn == 'scissors':
        if compTurn == 'paper':
            myWin += 1
            print('You won, scissors cut paper!')
        elif compTurn == 'rock':
            compWin += 1
            print('Computer won, rock beats scissors!')
        else:
            draw += 1
            print('Draw! We both chose scissors!')
    else:
        if compTurn == 'rock':
            myWin += 1
            print('You won, paper wraps stone!')
        elif compTurn == 'scissors':
            compWin += 1
            print('Computer won, scissors cut paper!')
        else:
            draw += 1
            print('Draw! We both chose paper!')


myWin, compWin, draw = 0, 0, 0
numGames, gamesPlayed = 5, 0

print("!!!  Let's play rock paper scissors  !!!")
while gamesPlayed < numGames:
    compTurn = game()
    myTurn = input_data()
    determine_winner(compTurn, myTurn)
    gamesPlayed += 1
print('My winnings: ', myWin)
print('Computer winnings: ', compWin)
print('Num of draws: ', draw)
