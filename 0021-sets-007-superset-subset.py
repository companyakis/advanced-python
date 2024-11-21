manager_names = {"aygün", "bilge", "donald", "ayhan", "bilal", "mustafa", "kutluk"}

emp_names = {"mustafa", "sevim", "jale", "elon", "mugan"}

childrens = {"bilge", "aygün"}

print(childrens.issubset(manager_names))

print(emp_names.issuperset(childrens))

print(manager_names.issuperset(childrens))

# True
# False
# True
