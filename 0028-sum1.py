sales_by_employees = [
    {"name": "ayhan", "sales_USD": 4500},
    {"name": "kağan", "sales_USD": 3200},
    {"name": "bilge", "sales_USD": 4300},
    {"name": "kutluk", "sales_USD": 2500},
    {"name": "bumin", "sales_USD": 4800},
] 

sales = [s["sales_USD"] for s in sales_by_employees]

print(sales)

total_sales = sum(sales)

print(total_sales)

# [4500, 3200, 4300, 2500, 4800]
# 19300
