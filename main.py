import requests

# To make string-building easier
base_url = "https://api.themoviedb.org/"
content_filter = "&language=en-US&page=1"

# Authenticates user w/my API key
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMmYyMjFiMWQwYTAzYTRlMGM0NDBiOThjOGNiMjQyNyIsIm5iZiI6MTc0NTcxNzU5Mi43Nywic3ViIjoiNjgwZDg5NTgzYzcxOGU4YzU1MzdiZmQ3Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.vlBCp5QFtDDar-Mg3TndqXFr2sVli_n_YizZ-230lng"
}

# Returns information about a movie given a movie title
def get_movie_info(name):
    url = f"{base_url}3/search/movie?query={name}{content_filter}"  # Sets up the url to search for the movie, limiting results to English-speaking movies (will probably change to include all movies)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        id = f"{response.json()["results"][0]["id"]}"  # Pulls first result
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        response = requests.get(url, headers=headers)
        return response.json()
    else:
        print(f"Failed to retreive data {response.status_code}")


# Testing function
movie_name = "Oppenheimer"
movie_info = get_movie_info(movie_name)

if movie_info:
    print(f"{movie_info["title"]}")
    print(f"{movie_info["release_date"]}")