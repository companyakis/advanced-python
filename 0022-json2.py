import json

emp_data = """

{
    "name": "Ayhan Kutlu",
    "title": "senior expert",
    "id": "4296",
    "department": "sales",
    "salary_USD" : 4200
}

"""

emp_data = json.loads(emp_data)
    

print(emp_data.keys()) # dict_keys(['name', 'title', 'id', 'department', 'salary_USD'])

print(f"Employee: {emp_data["name"]} and salary: {emp_data["salary_USD"]}") # Employee: Ayhan Kutlu and salary: 4200
