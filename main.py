import requests

base_url = "http://www.omdbapi.com/"
api_key = "&apikey=738d3f40"

def get_movie_info(name):
    url = f"{base_url}?t={name}{api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retreive data {response.status_code}")

movie_name = "Oppenheimer"
movie_info = get_movie_info(movie_name)

if movie_info:
    print(f"{movie_info["Title"]}")