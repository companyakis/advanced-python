employee_salaries_usd = {"mustafa": 6500, "aygün": 5250, "ayhan": 4800, "bengü": 4000}

employee_names = list(map(lambda x: x, employee_salaries_usd.keys()))

print(employee_names) # ['mustafa', 'aygün', 'ayhan', 'bengü']

employee_only_salaries = list(map(lambda x: x, employee_salaries_usd.values()))

print(employee_only_salaries) # [6500, 5250, 4800, 4000]
