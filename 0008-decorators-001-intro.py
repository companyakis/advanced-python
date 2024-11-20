def sum_normal_1(x: int, y: int, z: int):
     print(x + y + z)

sum_normal_1(3, 4, 5) # 12

def mutiply_two(func) :
    def wrapper(x: int, y: int, z: int):
        func(x * 2, y * 2, z * 2)
    return wrapper

@mutiply_two
def sum_normal_2(x: int, y: int, z: int):
     print(x + y + z)


sum_normal_2(3, 4, 5) # 24
