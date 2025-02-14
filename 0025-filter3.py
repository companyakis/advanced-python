tweet_people = [
    {"person": "Mustafa", "tweets": ["xfddf", "ssads", "sdsad", "sdsd", "dsfsdfsdfsd"]},
    {"person": "Aygün", "tweets": ["dsax", "ds", "few", "dss"]},
    {"person": "Bilge", "tweets": ["xwew"]},
    {"person": "Hakan", "tweets": ["dsax", "saaas", "dsds", "sdsdd", "ddfd", "sdasdas", "sdd"]},
    {"person": "Kültigin", "tweets": ["x", "dssa"]},
]

people_more_than_two_tweets = list(filter(lambda p: len(p["tweets"]) > 2, tweet_people))

print(people_more_than_two_tweets)

#[{'person': 'Mustafa', 'tweets': ['xfddf', 'ssads', 'sdsad', 'sdsd', 'dsfsdfsdfsd']}, {'person': 'Aygün', 'tweets': ['dsax', 'ds', 'few', 'dss']}, {'person': 'Hakan', 'tweets': ['dsax', 'saaas', 'dsds', 'sdsdd', 'ddfd', 'sdasdas', 'sdd']}]

print(people_more_than_two_tweets[0]["person"]) # Mustafa

names_of_people_more_than_two_tweets = list(map(lambda p: p["person"], people_more_than_two_tweets))

print(names_of_people_more_than_two_tweets) # ['Mustafa', 'Aygün', 'Hakan']

