names = ["aygün", "hakan", "kağan", "bilge", "bumin", "kutluk", "kültigin", "ayhan", "timur", "kapgan", "atilla", "teoman", "oğuz"]

def gen_t_words(items: list[str]):
    for item in items:
        if "t" in item:
            yield item  
            
gen_result = gen_t_words(names)

# lazy evaluation
# available if we want!

print(next(gen_result))
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))
print(next(gen_result))

"""
kutluk
kültigin
timur
atilla
teoman
Traceback (most recent call last):
  File "d:\src\pydaily\main.py", line 18, in <module>
    print(next(gen_result))
          ^^^^^^^^^^^^^^^^
StopIteration
"""
