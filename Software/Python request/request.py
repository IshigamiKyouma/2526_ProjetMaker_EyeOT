import requests

# 1. Use the regional routing (europe) for Account-V1
ACCOUNT_URL = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{}/{}?api_key={}"
# 2. Use the platform routing (euw1) for Summoner-V4 via PUUID
SUMMONER_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{}?api_key={}"

url_all_data = "https://127.0.0.1:2999/liveclientdata/allgamedata"

import requests

def get_player_data(game_name, tag_line, api_key):
    # Use headers instead of putting the key in the URL string
    headers = {
        "X-Riot-Token": api_key
    }
    
    # URL without the api_key parameter
    acc_url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    
    response = requests.get(acc_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        # This will tell you if it's still 401
        print(f"Error {response.status_code}: {response.text}")
        return None


# Usage (Note: Split the name and tag)
api_key = ""
print(get_player_data("IshigamiKyouma", "HAINE", api_key))


