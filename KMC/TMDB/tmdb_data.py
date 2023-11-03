import json, requests


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

def tmdb_movie_data():
    url = "https://api.themoviedb.org/3/search/movie"
    query = input("Enter now playing film from TMDB:\n").capitalize()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    parameters = {
        'query': query
    }
    
    response = requests.get(url, params=parameters, headers=headers)
    
    if(response.status_code == 200):
        data = response.json()
        format_data = json.dumps(data, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=3, separators=None, default=None, sort_keys=True)
        print(format_data)
    else:
        print(f'Request failed. Status code {response.status_code}')
    
tmdb_movie_data()
