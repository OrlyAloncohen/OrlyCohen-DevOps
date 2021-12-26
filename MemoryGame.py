import random

def get_list_from_user(dif_game):
    rand_list_from_user = []
    for i in range(dif_game):
        rand_game_user = int(input("please enter number in your list"))
        rand_list_from_user.append(rand_game_user)
    return rand_list_from_user


def generate_sequenc(dif_game):
    rand_list = []
    for i in range(dif_game):
        rand_game = random.randint(1, 101)
        rand_list.append(rand_game)
    return rand_list


def is_list_equal(rand_list_from_user, rand_list):
    return rand_list_from_user == rand_list


def play(dif_game):
    rand_list = generate_sequenc(dif_game)
    rand_list_from_user = get_list_from_user(dif_game)
    return is_list_equal(rand_list_from_user, rand_list)
