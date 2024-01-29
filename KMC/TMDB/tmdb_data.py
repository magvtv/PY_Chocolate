import json, requests
from datetime import datetime


# load the the api token and the api key from the configx.isdisjoint(y)
def load_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
            api_key = config_data["api_key"]
            access_token = config_data["access_token"]
        return api_key, access_token
    except FileNotFoundError:
        print("Config json file not found!")
        exit(1)
    except KeyError:
        print("API key and access token missing in your config file!")
        exit(1)


api_key, access_token = load_config()
# print(f"API Key: {api_key} \nAccess Token: {access_token}")


def search_films(start_year, end_year):
    base_url = "https://api.themoviedb.org/3/search/movie"
    query = input("Enter any film title:\n").capitalize()
    headers = {
        "Authorization": f"Bearer {access_token}", 
        "Content-Type": "application/json"
    }

    parameters = {
        "query": query,
        "release_date": f'{start_year}-01-01',
        "release_date": f'{end_year}-12-31',
    }

    response = requests.get(base_url, params=parameters, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # extract only wanted portions of the data
        film_details = [
            {
                'title': film['title'],
                'release_date': film['release_date'],
                'overview': film['overview']
            }
            for film in data.get('results', [])
        ]
        format_data = json.dumps(
            film_details,
            indent=3
        )
        print(format_data)
    else:
        print(f"Request failed. Status code {response.status_code}")



current_year = datetime.now().year
start_year = 2020
results = search_films(start_year, current_year)

# for film in results:
#     print(f"Title: {film['title']}")
#     print(f'Release Date: {film['release_date']}' )
#     print(f'Overview: \n{film['overview']}')