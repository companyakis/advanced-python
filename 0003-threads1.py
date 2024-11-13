import time
import threading

def calculate_cube(n: int):
    time.sleep(2)
    return n ** 3

# before threads

# now, slow but let's calculate

result = [calculate_cube(i) for i in range(10)] # 20.0 s

print(result) # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
