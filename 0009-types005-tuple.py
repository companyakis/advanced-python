def immutable_data(name: str, birth_year: int) -> tuple[str, int]:
    
    return (name, birth_year)
    
    
user1 = immutable_data("Mustafa", 2045)

print(type(user1))

print(user1[0])

print(user1[1])

# <class 'tuple'>
# Mustafa
# 2045
