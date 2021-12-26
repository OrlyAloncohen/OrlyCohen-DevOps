import random
from forex_python.converter import CurrencyRates


def get_money_interval(dif_game, num):
    shaar = 1 / (CurrencyRates.get_rates('ILS', 'USD'))
    t = shaar * num
    return range(t - (5 - dif_game), t + (5 - dif_game))


def get_guess_from_user():
    guess_user = random.randint(1, 100)
    num = input(f"please guess a number in ILS")
    return num, guess_user


def play(dif_game):
    num, guess_number = get_guess_from_user()
    total = get_money_interval(dif_game, guess_number)
    return num in total
