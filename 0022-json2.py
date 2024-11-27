import json

customer_data = '{"city": "Ankara", "customer": "ayhan bilir", "idx": "2014"}'

print(type(customer_data)) # <class 'str'>

# we can change data type
# use object hook, but only keys are here!

new_customer_data1= json.loads(customer_data, object_hook = list)

print(type(new_customer_data1)) # <class 'list'>

print(new_customer_data1) # ['city', 'customer', 'idx']

# object_pairs_hook = list

new_customer_data2 = json.loads(customer_data, object_pairs_hook = list, object_hook = list)

print(type(new_customer_data2)) # <class 'dict'>

print(new_customer_data2) # [('city', 'Ankara'), ('customer', 'ayhan bilir'), ('idx', '2014')]

cus_idx = new_customer_data2[2][1]

print(cus_idx) # 2014
