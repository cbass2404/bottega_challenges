# cents_per_hit = {
#     "Google": 4,
#     "Facebook": 3,
#     "Youtube": 5,
#     "Amazon": 2,
# }

# for key, value in cents_per_hit.items():
#     print(key[0] + ' ' + value * '$')
    
# print(cents_per_hit.items())
# print(cents_per_hit.keys())
# print(cents_per_hit.values())

sales = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12,
}

print('g ' + sales['google'] * '$')

for key, value in sales.items():
    print(key[0] + ' ' + value * '$')