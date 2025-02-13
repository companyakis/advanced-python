employee_salaries_usd = [
    {"name": "mustafa", "salary": 7500},
    {"name": "aygün", "salary": 6300},
]

salaries = list(map(lambda x: x["salary"], employee_salaries_usd))

print(salaries) # [7500, 6300]
