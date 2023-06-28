# import http.client
# import pandas as pd

# column = ['column1, column2']
# conn = http.client.HTTPSConnection("yahoo-finance127.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "be8959d384msh564d6fb51a898fdp1e17e6jsn9eba691cc508",
#     'X-RapidAPI-Host': "yahoo-finance127.p.rapidapi.com"
# }

# conn.request("GET", "/price/eth-usd", headers=headers)

# res = conn.getresponse()
# my_dict = res.read()
# df = pd.DataFrame(eval(data=my_dict))

import pandas as pd
import requests

API_KEY = "CGg7hwPyCocCW0EBAY0rGpQEecQMhzqF"
url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey={API_KEY}"

response = url.get()
data = response.text

print(data)
