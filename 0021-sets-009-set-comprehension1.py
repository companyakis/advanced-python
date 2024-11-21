squared_set = {i ** 2 for i in {3, 3, 1, 2, 5, 4}}

print(squared_set) # {1, 4, 9, 16, 25}

sentence = "Hi How are you Are you fine"

unique_chars = {c for c in sentence.lower().replace(" ", "")}

print(unique_chars) # {'h', 'r', 'e', 'w', 'o', 'n', 'a', 'y', 'i', 'f', 'u'}
