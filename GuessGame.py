import random


def generate_number(dif_game):
    secret_number = random.randint(1, dif_game)
    return secret_number


def get_guess_from_user(dif_game):
    guess_user = input("guess a game number between 1-" + str(dif_game))
    return guess_user


def compare_results(guess, genarate):
    if guess == genarate:
        return True
    else:
        return False


def play(dif_game):
    gen = generate_number(dif_game)
    gus = get_guess_from_user(dif_game)
    result = compare_results(gen, gus)
    return result
