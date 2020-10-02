# import numpy as np

# def weighted_lottery(weights):
#     container_list = []
    
#     for (name, weight) in weights.items():
#         for _ in range(weight):
#             container_list.append(name)
            
# other_weights = {
#     'winning': 1,
#     'break_even': 2,
#     'losing': 3
#     }

# print(weighted_lottery(other_weights))

import random


def dollars_bet(value):
    cash_on_hand = 20
    dollars_bet = {
        1: {
            'high': 30,
            'med': 70,
            'low': 71,
        },
        2: {
            'high': 40,
            'med': 75,
            'low': 76,
        },
        3: {
            'high': 45,
            'med': 80,
            'low': 81,
        },
    }

    while cash_on_hand > 0:
        result = random.randint(1, 100)
        if result >= (dollars_bet[value]['low']):
            cash_on_hand += value
            print('You win $' + str(value * 2))
            print('$' + str(cash_on_hand))
        elif result <= (dollars_bet[value]['med']) and result > (dollars_bet[value]['high']):
            print('Broke even, try again.')
            print('$' + str(cash_on_hand))
        elif result <= (dollars_bet[value]['high']):
            cash_on_hand -= value
            print('Bad luck, try again..')
            print('$' + str(cash_on_hand))
        elif cash_on_hand <= 0:
            break
    print('Game over')
dollars_bet(2)
