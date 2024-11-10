import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6af268ca40d146898e4572530f66a536'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
body  = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_create ={
    "pokemon_id": "126894",
    "name": "New Name",
    "photo_id": 1
}
body_pokeball = {
    "pokemon_id": "126894"
}

'''response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json= body)
print(response_create.text)'''

'''response_create = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)'''

response_create = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_create.text)

