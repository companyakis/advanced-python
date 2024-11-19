names = ["aygün", "hakan", "kağan", "bilge", "bumin", "kutluk", "kültigin", "ayhan", "timur", "kapgan", "atilla", "teoman", "oğuz"]

# let define normal and generator functions
# find the words containg "t"

# normal func needs more memory!

def t_words(items: list[str]):
    t: list[str] = []
    for item in items:
        if "t" in item:
            t.append(item)
    return t
    
result = t_words(names)

print(result) # ['kutluk', 'kültigin', 'timur', 'atilla', 'teoman']

def gen_t_words(items: list[str]):
    for item in items:
        if "t" in item:
            yield item  
            
gen_result = gen_t_words(names)

print(gen_result) # <generator object gen_t_words at 0x00000183FBE08110>

print(list(gen_result)) # ['kutluk', 'kültigin', 'timur', 'atilla', 'teoman'] 
