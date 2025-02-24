import requests

response = requests.post("https://jsonplaceholder.typicode.com/todos",
                        data = {"userId": "500",
                                "title": "Mustafa was here",
                                "body": "A rolling stone gathers no moss"
                                }
                        )
result = response.json()

print(result) # {'userId': '500', 'title': 'Mustafa was here', 'body': 'A rolling stone gathers no moss', 'id': 201}

