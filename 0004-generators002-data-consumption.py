names = ["aygün", "hakan", "kağan", "bilge", "bumin", "kutluk", "kültigin", "ayhan", "timur", "kapgan", "atilla", "teoman", "oğuz"]

def gen_t_words(items: list[str]):
    for item in items:
        if "t" in item:
            yield item  
            
gen_result = gen_t_words(names)

print("Print 1: ",  list(gen_result)) # ['kutluk', 'kültigin', 'timur', 'atilla', 'teoman'] 

# we'll see empty results, because "data consumed!"

print("Print 2: ", list(gen_result)) # Print 2:  []  

print("Print 3: ", list(gen_result)) # Print 3:  []

# If we want to print, we should create again
# we can use set, tuple...

print("Print 4: ", set(gen_t_words(names))) # Print 4:  {'atilla', 'kültigin', 'timur', 'teoman', 'kutluk'}
