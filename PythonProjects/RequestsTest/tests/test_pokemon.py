import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6af268ca40d146898e4572530f66a536'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID = '9011'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200