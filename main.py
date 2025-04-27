import requests
from apikey import API_KEY

# To make string-building easier
base_url = "https://api.themoviedb.org/"
content_filter = "&language=en-US&page=1"

class Movie:
    def __init__(self, title):
        url = f"{base_url}3/search/movie?query={title}{content_filter}"  # Sets up the url to search for the movie, limiting results to English-speaking movies (will probably change to include all movies)
        response = requests.get(url, headers=API_KEY)
    
        if response.status_code == 200:
            id = f"{response.json()["results"][0]["id"]}"  # Pulls first result
            url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
            response = requests.get(url, headers=API_KEY)
        else:
            print(f"Failed to retreive data {response.status_code}")

        self.title = response.json()["title"]
        self.id = response.json()["id"]
        self.year = response.json()["release_date"]
        self.genre = response.json()["genres"][0]["id"]

def recommendations(movie):
    url = f"https://api.themoviedb.org/3/discover/movie?language=en-US&with_genres={movie.genre}"  # Finds movie of the same genre
    response = requests.get(url, headers=API_KEY)

    recList = []
    recList.append(f"{response.json()["results"][0]["title"]}")
    recList.append(f"{response.json()["results"][1]["title"]}")
    recList.append(f"{response.json()["results"][2]["title"]}")
    recList.append(f"{response.json()["results"][3]["title"]}")
    recList.append(f"{response.json()["results"][4]["title"]}")

    for i in range(5):
        print(str(i+1) + ". " + recList[i])


def main():
    print("----Menu----\n" \
    "1. Provide a movie title\n" \
    "2. Search for a movie\n" \
    "3. Search by genre\n" \
    "4. Print information about a given movie\n")

    while True:
        try:
            menuSelection = input("Please enter your menu selection: ")
            menuSelection = int(menuSelection)
            if menuSelection < 1 or menuSelection > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer (1 - 4).")

    if(menuSelection == 1):
        name = input("Please enter a movie title: ")
        movie = Movie(name)
        print("You chose: " + movie.title + ", released: " + movie.year + ".")
        print("Here's a list of similar movies!")
        recommendations(movie)

    if(menuSelection == 2): raise Exception("No option 2")
    if(menuSelection == 3): raise Exception("No option 3")
    if(menuSelection == 4): raise Exception("No option 4")

main()