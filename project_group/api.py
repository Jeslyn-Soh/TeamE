api_key = "IUMVK4SLEPVSK1MW"

import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=IUMVK4SLEPVSK1MW'

response = requests.get(url)
print(response.json())