ages = [11, 16, 22, 47, 49, 11, 98, 32, 34, 44, 41, 18, 24, 25, 24]

odd_unique_ages = {age for age in ages if age % 2 != 0} 

print(odd_unique_ages) # {41, 11, 47, 49, 25}
