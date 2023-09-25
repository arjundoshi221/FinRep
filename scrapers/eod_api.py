# URL: https://eodhd.com/financial-apis/stock-market-financial-news-api/

import json
import requests
from scapers.env import EOD_API_TOKEN

URL = f"https://eodhistoricaldata.com/api/news?api_token={EOD_API_TOKEN}&s=AAPL.US&offset=0&limit=1"

response = requests.get(url=URL).json()[0]
print(response)
print("\n\n\n######################\n\n\n")
print(type(response))

with open("response_eod.json", "w") as file:
    json.dump(response, file)
