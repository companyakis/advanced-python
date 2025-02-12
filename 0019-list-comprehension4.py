people = ["ayhan", "hakan", "barbaros", "aygün", "bengü"]

ages = [29, 34, 45, 35, 19]

p_and_a = [{people[i]: ages[i]} for i in range(len(people))]

print(p_and_a) # [{'ayhan': 29}, {'hakan': 34}, {'barbaros': 45}, {'aygün': 35}, {'bengü': 19}]

over_30 = [{people[i]: ages[i]} for i in range(len(ages)) if ages[i] > 30]

print(over_30) # [{'hakan': 34}, {'barbaros': 45}, {'aygün': 35}]
