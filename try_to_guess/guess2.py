import random

guesses_made = 0
number = random.randint(1, 20)
attemptsNum = 6
print('Привет, я загадал число между 1 и 20. Сможешь угадать?')

while guesses_made < attemptsNum:
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess < number:
        print('Твое число меньше того, что я загадал.')

    if guess > number:
        print('Твое число больше загаданного мной.')

    if guess == number:
        break

if guess == number:
    print('Поздравляю! Ты угадал мое число, использовав {0} попыток!'.format(guesses_made))
else:
    print('А вот и не угадал! Я загадал число {0}'.format(number))
