import random


def generate_list(n):
    rand_no_list = []
    for i in range(n):
        rand_no_list.append((random.randint(0, 1000000000)))

    return rand_no_list
