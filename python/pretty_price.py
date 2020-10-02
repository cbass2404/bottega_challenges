import math


def pretty_price(price, change):
    if change >= 10:
        price = math.floor(price) + change * 0.01
    elif change >= 1:
        price = math.floor(price) + change * 0.10
    else:
        price = math.floor(price) + change
    return format(price, '.2f')


print(pretty_price(3.20, 99))
print(pretty_price(3.20, 0.99))
print(pretty_price(3.99, 20))
print(pretty_price(3, 2))
