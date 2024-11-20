years:list[int] = [2018, 2019, 2020, 2021]

years2 = years

years3 = years.copy()

years.append(2022)

print("years = ", years)

print("years2 = ", years2)

print("years3 = ", years3)

print("---------------------------------------")

# but we can have a problem!
# look at our years list

years2.append(2050)

print("years = ", years)

print("years2 = ", years2)

print("years3 = ", years3)

# years =  [2018, 2019, 2020, 2021, 2022]
# years2 =  [2018, 2019, 2020, 2021, 2022]
# years3 =  [2018, 2019, 2020, 2021]
# ---------------------------------------
# years =  [2018, 2019, 2020, 2021, 2022, 2050]
# years2 =  [2018, 2019, 2020, 2021, 2022, 2050]
# years3 =  [2018, 2019, 2020, 2021]
