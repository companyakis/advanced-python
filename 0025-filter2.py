names: list[str] = ["Mustafa", "Aygün", "Bilge", "Kültigin", "Kutluk", "Bumin", "AYHAN"]

names_contain_a = list(filter(lambda x: str.__contains__(x.lower(),"a"), names))

print(names_contain_a) # ['Mustafa', 'Aygün', 'AYHAN']
