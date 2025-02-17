# deserializing

import json

with open("employee.json") as file:
    data = json.load(file)
    
    
print(type(data)) # <class 'dict'>

print(data.keys()) # dict_keys(['name', 'title', 'id', 'department', 'salary_USD'])

print(f"Employee: {data["name"]} and salary: {data["salary_USD"]}") # Employee: Ayhan Kutlu and salary: 4200
