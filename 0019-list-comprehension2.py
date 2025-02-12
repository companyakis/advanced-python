ages = [11, 16, 22, 47, 49, 11, 98, 32, 34, 44, 41, 17, 24, 25, 24]

voters = [age for age in ages if age >= 18]

#print(f"Ages of voters: {voters}") # Ages of voters: [22, 47, 49, 98, 32, 34, 44, 41, 24, 25, 24]

non_voters = [age for age in ages if age < 18]

#print(non_voters) # [11, 16, 11, 17]

voters_warning = [age if age >= 18 else "Young person!" for age in ages]

print(voters_warning) # ['Young person!', 'Young person!', 22, 47, 49, 'Young person!', 98, 32, 34, 44, 41, 'Young person!', 24, 25, 24]
