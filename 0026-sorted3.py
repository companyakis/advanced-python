employees = [
    {"name": "ayhan", "age": 32},
    {"name": "bengü", "age": 42},
    {"name": "aygün", "age": 35},
    {"name": "kağan", "age": 22},
    {"name": "bilge", "age": 52},
]

sorted_by_ages = list(sorted(employees, key = lambda a: a["age"], reverse = True))

sorted_ages = list(map(lambda x: x["age"], sorted_by_ages))

print(sorted_ages) # [52, 42, 35, 32, 22]
