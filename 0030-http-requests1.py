# pip install requests
# https://jsonplaceholder.typicode.com/todos

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")

print(response.status_code) # 200

result = response.text

#print(result)

print(type(result)) # <class 'str'>

result = json.loads(result)

for i in result[:10]:
    print(i["title"])

"""
delectus aut autem
quis ut nam facilis et officia qui
fugiat veniam minus
et porro tempora
laboriosam mollitia et enim quasi adipisci quia provident illum
qui ullam ratione quibusdam voluptatem quia omnis
illo expedita consequatur quia in
quo adipisci enim quam ut ab
molestiae perspiciatis ipsa
illo est ratione doloremque quia maiores aut
"""
