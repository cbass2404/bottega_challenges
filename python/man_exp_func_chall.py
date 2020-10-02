from functools import reduce
from decimal import Decimal

def manual_exponent(value, exponent):
    if type(value) == (int or float or complex or Decimal) and type(exponent) == (int or float or complex or Decimal):
        print(Decimal(reduce(lambda x, y : pow(x, y), [value, exponent])))
    else:
        print('Invalid')
manual_exponent([1 , 3], 2)