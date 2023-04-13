import os
import requests
from dotenv import load_dotenv
import pprint as pp
import inquirer
load_dotenv()
offset = 0
page = 0
url = 'https://pokeapi.co/api/v2/pokemon/?offset='


def IntroduceUser():
    print("Welcome to the Pokemon Library")
    print("-------------------------")
    print("Press enter to check the first list of Pokemon")
    questions = [
        inquirer.List('start',
                      message="Press enter to check library or exit to leave",
                      choices=['ENTER', 'EXIT'],
                      ),
    ]
    answer = inquirer.prompt(questions)
    if (answer['start'] == 'ENTER'):
        runRequest(0)
    else:
        return


def nextSet():

    question = [
        inquirer.List('next',
                      message="Change Page?",
                      choices=["next", "prev", "exit"]
                      ),
    ]
    answer = inquirer.prompt(question)
    if (answer['next'] == 'next'):
        global page
        page += 20
        runRequest(page)
    elif (answer['next'] == 'prev'):
        if (page == 0):
            print('THIS IS THE FIRST PAGE')
            runRequest(page)
        else:
            page -= 20
            runRequest(page)
    elif (answer['next'] == 'exit'):
        print("PEACE")
        return


def runRequest(offset):
    allPokemon = []
    res = requests.get(url + str(offset) + '&limit=20')
    data = res.json()
    results = data['results']
    for poki in results:
        allPokemon.append(poki['name'])
    print(allPokemon)
    pokemon = [inquirer.List('Select',
                             message="select a pokimon",
                             choices=allPokemon),
               ]
    input = inquirer.prompt(pokemon)
    nextSet()


IntroduceUser()
