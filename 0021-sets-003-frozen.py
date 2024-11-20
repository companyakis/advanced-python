# mutable set

cities = {"Newyork", "Izmir", "Ankara", "Baku", "Astana", "London"}

cities.add("Milano")

cities.remove("London")

print(cities) # {'Newyork', 'Astana', 'Milano', 'Ankara', 'Izmir', 'Baku'}

# immutable set

years = frozenset({1990, 2013, 2016})

years.add(2024) 

print(years) # AttributeError: 'frozenset' object has no attribute 'add'
