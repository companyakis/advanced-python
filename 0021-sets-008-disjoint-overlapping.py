manager_names = {"aygün", "bilge", "donald", "ayhan", "bilal", "mustafa", "kutluk"}

emp_names = {"mustafa", "sevim", "jale", "elon", "mugan"}

childrens = {"bengü", "günay"}

print(childrens.isdisjoint(manager_names))

print(emp_names.isdisjoint(manager_names))

# i don't know any overlapping method

overlapped = len(manager_names & emp_names) > 0

print(overlapped)

not_overlapped = len(emp_names & childrens) == 0

print(not_overlapped)

# True
# False
# True
# True
