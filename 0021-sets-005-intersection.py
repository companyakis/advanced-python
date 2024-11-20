years = [2018, 2020, 2022, 2023, 2024, 2018, 1990, 2013, 2016, 1987, 1923, 2012, 2024]

years_set_from_list = set(years)

years_ten = {1990, 2000, 2010, 2020, 2030, 2040}

intersection_years = years_set_from_list & years_ten

print(intersection_years) # {2020, 1990}
