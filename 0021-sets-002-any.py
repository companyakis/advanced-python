years = [2018, 2020, 2022, 2023, 2024, 2018, 1990, 2013, 2016, 1987, 1923, 2012, 2024]

years_set_from_list = set(years)

search_years = {1990, 2013, 2016}

result = any(year in years_set_from_list for year in search_years)

print(result) # True

if result:
    print("Yes, we have some data")
    
else:
    print("No data!")
