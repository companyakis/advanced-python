def create_employee(id: int, name: str) -> dict[int, str]:
    
    new_emp = {id: name}
    
    return new_emp

emp_1 = create_employee(101, "Mustafa Büyükdereli")

print(type(emp_1))

print(emp_1)

for key, value in emp_1.items():
    print(f"Employee id: {key} and name: {value}")
    
"""
<class 'dict'>
{101: 'Mustafa Büyükdereli'}
Employee id: 101 and name: Mustafa Büyükdereli
    
"""
