# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup as bs

# i'll use my own internal page, but we can use external web pages to extract data

url = "http://127.0.0.1:5500/index.html"

response = requests.get(url, headers={"Accept": "text/html"})

# let's parse the text from the response

parsed = bs(response.text, "html.parser")

print(parsed.text)

"""
Mustafa Buyukdereli was here


Year 2024
My name is Mustafa

Lorem Ipsum
A rolling stone gathers no moss
Study hard!

Samsung
Don't waste your time!

214
176
812   
    
"""
