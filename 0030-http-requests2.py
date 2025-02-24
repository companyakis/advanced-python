import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos",
                        params = {"userId": "3", "completed": "true"}
                        )
result = response.json()

#print(result)

print(result[1]["title"]) # cum debitis quis accusamus doloremque ipsa natus sapiente omnis
