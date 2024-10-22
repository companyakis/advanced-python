from enum import Enum

class Department(Enum):
    Title = "FinTech"
    Head = "Mustafa Büyükdereli"
    NumberOfEmployees = 17
    YearlyUSDBudget = 2_000_000
    
print(type(Department))

print("-------------------------------")

print(Department.Title.value)

print("-------------------------------")

print(f"Department yearly budget: ${Department.YearlyUSDBudget.value}")

"""
<class 'enum.EnumType'>
-------------------------------   
FinTech
-------------------------------   
Department yearly budget: $2000000

"""
