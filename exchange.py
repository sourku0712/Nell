import requests

fx_API= "<API-Key>"

def currency(base,target,amount):
    url = f"https://v6.exchangerate-api.com/v6/{fx_API}/pair/{base}/{target}"
    # Making our request
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate= data.get('conversion_rate')
        try:
            value= int(amount)*(int(rate))
            return (int(value))
        except Exception as e:
            return None
