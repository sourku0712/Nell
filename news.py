import requests
import time
newsapi= "51790b3fc84a4aaab7b8144fd1c4d392"

def News():
    r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
    if r.status_code == 200:
        # Parse the JSON response
        data = r.json()
        
        # Extract the articles
        articles = data.get('articles', [])
        
        # Speak the headlines
        for article in articles:
            print(article['title'])
            print()
            time.sleep(0.5)