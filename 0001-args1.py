def sum_numbers(*args: int):
    total: int = 0
    for i in args:
        total += i
    return total

print(sum_numbers(5, 11, 17)) # 33

print(sum_numbers(47, 11, 10, 3, 4, 2))

# print(sum_numbers(3, 11, "22")) # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
