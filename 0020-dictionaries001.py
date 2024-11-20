# add types => str, int

emp_numbers: dict[str, int] = {"fintech": 7, "sales": 5, "finance": 2}

# add a new department info

emp_numbers["operations"] = 4

print(emp_numbers)

# update

emp_numbers["fintech"] = 9

print(emp_numbers)

# delete a department

del emp_numbers["sales"]

print(emp_numbers)

# clear all the info

emp_numbers.clear()

print(emp_numbers)

# {'fintech': 7, 'sales': 5, 'finance': 2, 'operations': 4}
# {'fintech': 9, 'sales': 5, 'finance': 2, 'operations': 4}
# {'fintech': 9, 'finance': 2, 'operations': 4}
# {}
