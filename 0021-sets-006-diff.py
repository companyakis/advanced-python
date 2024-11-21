manager_names = {"aygün", "bilge", "donald", "ayhan", "bilal", "mustafa", "kutluk"}

emp_names = {"mustafa", "sevim", "jale", "elon", "mugan"}

diff1 = manager_names - emp_names

print(diff1)

diff2 = emp_names - manager_names

print(diff2)

symmetric_difference = manager_names ^ emp_names

print(symmetric_difference)

# {'bilge', 'aygün', 'bilal', 'kutluk', 'donald', 'ayhan'}
# {'mugan', 'elon', 'jale', 'sevim'}
# {'mugan', 'bilal', 'kutluk', 'donald', 'jale', 'ayhan', 'bilge', 'aygün', 'elon', 'sevim'}
