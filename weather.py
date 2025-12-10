import requests

accu_api_key = "<Accu-API-Key>"

# ====== WEATHER =======
def getWeather(city):
    #Get Location Key of City
    def get_location_key(city_name, api_key):
        url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
        params = {
            "q": city_name,
            "apikey": api_key
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                location_key = data[0]["Key"]
                return location_key
            else:
                print("City not found")
        else:
            print(f"Error fetching location data: {response.status_code}")
        
        return None

    #Get weather report for the location key
    def get_weather(location_key, api_key):
        url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
        params = {
            "apikey": api_key
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                weather_info = data[0]
                temperature = weather_info["Temperature"]["Metric"]["Value"]
                weather_text = weather_info["WeatherText"]
                print(f"Current temperature: {temperature}°C")
                print(f"Weather conditions: {weather_text}")
            else:
                print("No weather data found.")
        else:
            print(f"Error fetching weather data: {response.status_code}")

    location_key = get_location_key(city, accu_api_key)
    if location_key:   
        get_weather(location_key, accu_api_key)  
