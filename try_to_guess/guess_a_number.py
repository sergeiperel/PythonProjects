import random


def comp_num():
    rand_num = random.randint(1, 10)
    return rand_num


print("Try to guess the number I guessed")
attempt = -1
hidden_num = comp_num()
while hidden_num != attempt:
    attempt = int(input())
    if hidden_num != attempt:
        print(f"No, it's not number {attempt}. Try again!")
    else:
        print(f"!!! You guess well, it's number {attempt} !!!")
        break
