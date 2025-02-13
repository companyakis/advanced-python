numbers: list[int] = [-5, 2, 0, 3, -4]

# f(x) = 2 * x - 1

new_numbers: list[int] = list(map(lambda n: 2 * n - 1, numbers))

print(new_numbers) # [-11, 3, -1, 5, -9]
