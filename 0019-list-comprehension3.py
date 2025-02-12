sentence = "She was born in 1990 and now she is 35"

number_list = [int(c) for c in sentence if c.isdigit()]

print(number_list) # [1, 9, 9, 0, 3, 5]
