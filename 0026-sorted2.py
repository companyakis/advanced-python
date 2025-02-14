tweet_people = [
  
    {"person": "Mustafa", "tweets": ["xfddf", "ssads", "sdsad", "sdsd", "dsfsdfsdfsd"]},
    {"person": "Aygün", "tweets": ["dsax", "ds", "few", "dss"]},
    {"person": "Bilge", "tweets": ["xwew"]},
    {"person": "Hakan", "tweets": ["dsax", "saaas", "dsds", "sdsdd", "ddfd", "sdasdas", "sdd"]},
    {"person": "Kültigin", "tweets": ["x", "dssa"]},
]

sorted_by_tweet_numbers = sorted(tweet_people, key = lambda x: len(x["tweets"]), reverse = True)

print(sorted_by_tweet_numbers)

names_of_people_sorted_by_tweet_numbers = list(map(lambda p: p["person"], sorted_by_tweet_numbers))

print(names_of_people_sorted_by_tweet_numbers) # ['Hakan', 'Mustafa', 'Aygün', 'Kültigin', 'Bilge']
