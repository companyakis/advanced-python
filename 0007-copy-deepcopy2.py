import copy

years:list[int] = [2018, 2019, 2020, 2021]

# shallow copy

# there is also deep copy, but now we don't use -> later

new_years = copy.copy(years)

new_years.append(3000)

print("years = ", years)

print("new_years = ", new_years)

print("-------------------------------")

years.append(4000)

print("years = ", years)

print("new_years = ", new_years)

print("-------------------------------")

new_years[0] = 5000

print("years = ", years)

print("new_years = ", new_years)

print("-------------------------------")

"""
years =  [2018, 2019, 2020, 2021]
new_years =  [2018, 2019, 2020, 2021, 3000]
-------------------------------
years =  [2018, 2019, 2020, 2021, 4000]    
new_years =  [2018, 2019, 2020, 2021, 3000]
-------------------------------
years =  [2018, 2019, 2020, 2021, 4000]    
new_years =  [5000, 2019, 2020, 2021, 3000]
-------------------------------
years =  [2018, 2019, 1990, 2021, 4000]    
new_years =  [5000, 2019, 2020, 2021, 3000]

"""



years[2] = 1990

print("years = ", years)

print("new_years = ", new_years)
