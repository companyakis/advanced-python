emp_numbers: dict[str, int] = {"fintech": 7, "sales": 5, "finance": 2, "operations": 4}

if ("Sales".lower() in emp_numbers):
    
    print(f"Sales department employee number: {emp_numbers["Sales".lower()]}") # Sales department employee number: 5

else:
    
    print("Nout found!")
