import json

customer_data = '{"city": "Ankara", "customer": "ayhan bilir", "idx": "2014"}'

print(type(customer_data)) # <class 'str'>

new_customer_data = json.loads(customer_data)

print(type(new_customer_data)) # dict

for key, value in new_customer_data.items():
    print(f"{key} -> {value}")
    
"""
city -> Ankara
customer -> ayhan bilir
idx -> 2014
"""
