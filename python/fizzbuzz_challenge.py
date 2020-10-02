"""
fizzbuzz exercise
prints from 1 to 100
multiples of 3 print "Fizz"
multiples of 5 print "Buzz"
multiples of 3 and 5 print "FizzBuzz"
top range should be dynamic
"""

# First Attempt

# def fizz_buzz(range_stop):
#     for number in range(1, range_stop):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 5 == 0 and number % 3 != 0:
#             print("Buzz")
#         elif number % 5 != 0 and number % 3 == 0:
#             print("Fizz")
#         else:
#             print(number)
#
#
# fizz_buzz(100)

# from operator import mod
#
#
# def fizz_buzz(range_stop):
#     for number in range(range_stop):
#         def find_truth(divider):
#             return True if mod(number, divider) == 0 else False
#         if find_truth(3) and find_truth(5) is True:
#             print("FizzBuzz")
#         elif find_truth(5) is True:
#             print("Buzz")
#         elif find_truth(3) is True:
#             print("Fizz")
#         else:
#             print(number)
#
#
# fizz_buzz(100)

from operator import mod


def fizz_buzz():
    start_program = True
    while start_program is True:
        for number in range(1, int(input("What number would you like to go to?\n\t"))):
            def find_truth(divider):
                return True if mod(number, divider) == 0 else False
            if find_truth(3) and find_truth(5) is True:
                print("FizzBuzz")
            elif find_truth(5) is True:
                print("Buzz")
            elif find_truth(3) is True:
                print("Fizz")
            else:
                print(number)
        if input("Would you like to continue?\n Yes or No?\n\t") == 'Yes':
            start_program = True
        else:
            start_program = False


fizz_buzz()
