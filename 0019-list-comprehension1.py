my_info = "Hi. My name is Mustafa. How are you?"

def clean_sentence(sentence: str) -> str:
    clenad = sentence.replace(".", "").replace("?", "").lower()
    return clenad

result = [clean_sentence(i) for i in my_info.split()]

print(result)

# ['hi', 'my', 'name', 'is', 'mustafa', 'how', 'are', 'you']
