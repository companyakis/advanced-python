# serialize => to file/ json

import json

emp_data = {
    "name": "Ayhan Kutlu",
    "title": "senior expert",
    "id": "4296",
    "department": "sales",
    "salary_USD" : 4200
}

print(type(emp_data)) # <class 'dict'>

emp_data_json = json.dumps(emp_data)

print(type(emp_data_json)) # <class 'str'>

print(emp_data_json[:10]) # {"name": " => why? because string data!


