import requests

Polygon_API_KEY= "VdhDkZRjOa22pGohohiZ9hQXdUdTeBDE"

BASE_URL = "https://api.polygon.io/v2/aggs/ticker/{symbol}/prev"

def get_stock_price(symbol):
    # Create the URL with the stock symbol (e.g., AAPL for Apple)
    url = BASE_URL.format(symbol=symbol)

    # Set up the headers with the API key
    headers = {
        'Authorization': f'Bearer {Polygon_API_KEY}'
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # If the response is successful, return the stock price
    if response.status_code == 200:
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            price = data['results'][0]['c']  # 'c' is the closing price of the stock
            return price
        else:
            print("No price data available.")
    else:
        print(f"Error: {response.status_code}, {response.text}")