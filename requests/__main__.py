import os
import requests

import pprint as pp
import inquirer
from pokiApi import *
offset = 0
page = 0
url = 'https://pokeapi.co/api/v2/pokemon/?offset='
choices = ['next -->', '<-- prev', '[exit]']
fightList = []
allPokemon = []


def clearConsole():
    os.system('clear')


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


def nextPage():
    global page
    clearConsole()
    page += 20
    runRequest(page)


def prevPage():
    global page
    if (page == 0):
        clearConsole()
        print("THIS IS THE ALREADY FIRST PAGE")
        runRequest(page)
    else:
        clearConsole()
        page -= 20
        runRequest(page)


def nextSet():

    question = [
        inquirer.List('next',
                      message="Change Page?",
                      choices=choices
                      ),
    ]
    answer = inquirer.prompt(question)
    if (answer['next'] == 'next -->'):
        nextPage()
    elif (answer['next'] == '<-- prev'):
        if (page == 0):
            print('THIS IS THE FIRST PAGE')
            runRequest(page)
        else:
            prevPage()
    elif (answer['next'] == '[exit]'):
        print("PEACE")
        return


def runRequest(offset):
    count = 0
    global allPokemon
    global fightList
    res = requests.get(url + str(offset) + '&limit=10')
    data = res.json()
    results = data['results']

    for poki in results:
        allPokemon.append(poki['name'])
    for choice in choices:
        allPokemon.append(choice)
    pokemon = [inquirer.List('Select',
                             message="select a pokimon",
                             choices=allPokemon),
               ]
    while count < 2:

        input = inquirer.prompt(pokemon)
        selected = input['Select']
        if (input['Select'] == 'next -->'):
            nextPage()
        elif (input['Select'] == '<-- prev'):
            prevPage()
        elif (input['Select'] == '[exit]'):
            clearConsole()
            print('GOODBYE')
            return
        else:
            print(selected)
            fightList.append(selected)
            clearConsole()
            print('Fighter ' + str((count + 1)) + ' ' + fightList[count - 1])
            count += 1
    grabPokiInfo(fightList)


IntroduceUser()
