import time
import threading

def calculate_cube(n: int, results):
    time.sleep(2)
    results[n] = n ** 3

results: dict[int, int] = dict()

threads = [threading.Thread(target = calculate_cube, args = (n, results)) for n in range(50)]

[t.start() for t in threads]

[t.join() for t in threads]

print(results) # 2.0 s

"""
{0: 0, 1: 1, 3: 27, 4: 64, 2: 8, 7: 343, 5: 125, 9: 729, 8: 512, 6: 216, 
13: 2197, 12: 1728, 11: 1331, 10: 1000, 15: 3375, 17: 4913, 16: 4096, 
33: 35937, 18: 5832, 20: 8000, 22: 10648, 38: 54872, 19: 6859, 27: 19683, 
23: 12167, 45: 91125, 28: 21952, 25: 15625, 26: 17576, 30: 27000, 34: 39304, 
48: 110592, 29: 24389, 31: 29791, 14: 2744, 36: 46656, 37: 50653, 39: 59319, 
40: 64000, 21: 9261, 35: 42875, 41: 68921, 42: 74088, 44: 85184, 
43: 79507, 24: 13824, 49: 117649, 47: 103823, 32: 32768, 46: 97336}

"""
