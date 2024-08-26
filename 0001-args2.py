def multiplication(*floats: float):
    mul: float = 1
    for i in floats:
        mul *= i
    return mul

print(multiplication(3.5, 4)) # 14.0

print(multiplication(3.2, 8.14, 4)) # 104.19200000000001

# print(multiplication("5.2", 4.7)) # TypeError: can't multiply sequence by non-int of type 'float'


