# num_list = [1, 2, 3, 4, 5, 6]
#
#
# def average_of_list(list_name):
#     sum = 0
#     for num in list_name:
#         sum = sum + num
#     print(average / len(list_name))
#
#
# average_of_list(num_list)
from functools import reduce

def get_average(num_list):
    total = reduce(
        (lambda total, element: total + element),
        num_list)

    return total / len(num_list)

num_list = [1, 2, 3, 4, 5, 6]

print(get_average(num_list))
