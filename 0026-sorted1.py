nums: list[float] = [-12.23, -12.32, 10.789, 10.7892, -12.23456]

sorted1 = sorted(nums)

print(sorted1)

sorted2 = sorted(nums, reverse=True)

print(sorted2)

print("Original list: ", nums)

# [-12.32, -12.23456, -12.23, 10.789, 10.7892]

# [10.7892, 10.789, -12.23, -12.23456, -12.32]

# Original list:  [-12.23, -12.32, 10.789, 10.7892, -12.23456]
