import random


MAX_TRIES = 10
MIN = 1
MAX = 1023


def game():
    # загадываем число
    n = random.randint(MIN, MAX)

    # приветствие
    print("Программа загадала число. У вас есть {} попыток на то, чтобы угадать.".format(MAX_TRIES))

    i = 1
    guess = 0
    while ((guess != n) and (i <= MAX_TRIES)):
        # get user input
        guess = int(input("{} попытка>".format(i)))

        # if correct
        if (guess == n):
            print("Поздравляем. Было загадано число {}".format(n))
            return True
        
        # if out of range
        if ((guess < MIN) or (guess > MAX)):
            print("число должно быть от {} до {}".format(MIN, MAX))
        else:
            # get 1 if guess is smaller and 0 if is bigger
            smaller = (guess < n)

            # if index is 0 print first var, if it's 1 print the second
            print(("Ваше число больше загаданного", "Ваше число меньше загаданного")[smaller])
            i += 1
        # elif (guess > n):
        #     print("Ваше число больше загаданного")
        #     i += 1

    print("Попытки истекли. Было загадано число {}".format(n))
    game()

# запуск игры
game()
