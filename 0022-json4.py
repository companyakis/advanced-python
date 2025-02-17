# serialize => to file/ json

import json

emp_data = {
    "name": "Bilge Gok",
    "title": "manager",
    "id": "2216",
    "department": "operations",
    "salary_USD" : 3700
}

print(type(emp_data)) # <class 'dict'>

# write to a file

with open("employee.json", "w") as file:
    json.dump(emp_data, file, indent=2)
