import json

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
        print('API key and access token missing in your config file!')
        exit(1)
        
api_key, access_token = load_config()
print(f'API Key: {api_key} \nAccess Token: {access_token}')