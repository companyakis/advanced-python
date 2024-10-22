from enum import Enum

class Cities(Enum):
    ISTANBUL = 34
    IZMIR = 35
    ANKARA = 6
    ADANA = 1
    
print(f"İstanbul plate code: {Cities.ISTANBUL.value}") # İstanbul plate code: 34
