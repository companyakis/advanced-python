years: list[int] = [2020, 2021, 2017, 2019, 2024]

iterator = iter(years)

while True:
    try:
        year = next(iterator)
        print(year)
    except StopIteration:
        break
    
    
# 2020
# 2021
# 2017
# 2019
# 2024
