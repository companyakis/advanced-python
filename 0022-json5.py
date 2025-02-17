import json

emp_data = [
    {
    "name": "Bilge Gok",
    "title": "manager",
    "id": "2216",
    "department": "operations",
    "salary_USD" : 3700
},
    {
    "name": "Kutluk Al",
    "title": "director",
    "id": "2236",
    "department": "HR",
    "salary_USD" : 6700
},  
]

print(type(emp_data)) # <class 'list'>

# write to a file

with open("employee.json", "w") as file: 
    json.dump(emp_data, file, indent=2)
