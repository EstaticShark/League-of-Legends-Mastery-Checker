import ast
import json
import requests
from champid import champ_id

API_KEY = 'RGAPI-14137a0d-3681-4b24-96ed-79dacca647b4' # As of 07/10/19

# Insert summoner name below
SUMMONER_NAME = 'Ieatyourweapon'

url_id = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + SUMMONER_NAME + '?api_key=' + API_KEY

r_id = requests.get(url_id)
summoner_info = ast.literal_eval(r_id.content.decode())

url = 'https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/' + summoner_info['id'] + '?api_key=' + API_KEY

r = requests.get(url)

# r contains some non-python literals, so we must use the json module instead
champ_mast = json.loads(r.content.decode())

for champ in champ_mast[:3]:
    print('\n' + champ_id[champ['championId']])
    for key in champ.keys():
        if key != 'championId':
            print(key + ':', champ[key])
