import requests
from apikey import API_KEY

# To make string-building easier
base_url = "https://api.themoviedb.org/"
content_filter = "&language=en-US&page=1"


# Returns information about a movie given a movie title
def get_movie_info(name):
    url = f"{base_url}3/search/movie?query={name}{content_filter}"  # Sets up the url to search for the movie, limiting results to English-speaking movies (will probably change to include all movies)
    response = requests.get(url, headers=API_KEY)
    
    if response.status_code == 200:
        id = f"{response.json()["results"][0]["id"]}"  # Pulls first result
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        response = requests.get(url, headers=API_KEY)
        return response.json()
    else:
        print(f"Failed to retreive data {response.status_code}")


# Testing function
movie_name = "Oppenheimer"
movie_info = get_movie_info(movie_name)

if movie_info:
    print(f"{movie_info["title"]}")
    print(f"{movie_info["release_date"]}")
#testing