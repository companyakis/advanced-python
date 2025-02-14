employees = [
    {"name": "ayhan", "age": 32},
    {"name": "bengü", "age": 42},
    {"name": "aygün", "age": 35},
    {"name": "kağan", "age": 22},
    {"name": "bilge", "age": 52},
]

min_aged_emp = min(employees, key = lambda e: e["age"])

print(min_aged_emp) # {'name': 'kağan', 'age': 22}

max_aged_emp = max(employees, key = lambda e: e["age"])

print(max_aged_emp) # {'name': 'bilge', 'age': 52}

# max_age = 0

# for emp in employees:
#     if (emp["age"] > max_age):
#         max_age = emp["age"]

# print(max_age) # 52
