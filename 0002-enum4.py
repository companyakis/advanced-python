from enum import Enum, auto

class Months(Enum):
    January = auto()
    February = auto()
    March = auto()
    April = auto()
    May = auto()
    
for month in Months:
    print(f"{month.value} - {month.name}")
    
"""
1 - January
2 - February
3 - March
4 - April
5 - May

"""
