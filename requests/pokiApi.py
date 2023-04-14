import requests
url = 'https://pokeapi.co/api/v2/pokemon/'


def showPokemon():


def grabPokiInfo(pokemon):
    for info in pokemon:
        res = requests.get(url + info)
        data = res.json()
        # print(data)
