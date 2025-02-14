numbers: list[int] = [3, 22, -21, 12, 9, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers) # [22, 12, 8]
