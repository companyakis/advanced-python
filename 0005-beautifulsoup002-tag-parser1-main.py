import requests
from bs4 import BeautifulSoup as bs

url = "http://127.0.0.1:5500/index.html"

response = requests.get(url, headers={"Accept": "text/html"})

parsed = bs(response.text, "html.parser")

# let's parse price info

parsed_price = parsed.find_all("p", class_ = "price")

for p in parsed_price:
    print(f"Price = {p.text}")
    
# Price = 214
# Price = 176
# Price = 812
