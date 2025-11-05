import requests

def get_crypto_price(symbol, convert):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": symbol,
        "convert": convert
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "172b24e5-70ad-4bee-b045-b094e9f7ee15",
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    try:
        price = data["data"][symbol]["quote"][convert]["price"]
        return price
    except KeyError:
        return f"Error retrieving data: {data}"