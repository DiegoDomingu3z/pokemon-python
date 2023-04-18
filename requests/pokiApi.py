import requests
from PIL import Image
import requests
from io import BytesIO
from colorit import init_colorit, background
import climage
import subprocess
url = 'https://pokeapi.co/api/v2/pokemon/'
poki1 = {}
pok1moves = {}
poki1lines = {}
poki2 = {}
poki2moves = {}
poki2lines = {}
poki1abilities = []
poki1images = []
poki2images = []


def grabPokiInfo(pokemon):
    print(pokemon)
    counter = 0
    global poki1
    global poki2
    for info in pokemon:
        res = requests.get(url + info)
        data = res.json()
        counter += 1
        if (counter == 1):
            poki1 = data
        elif (counter == 2):
            poki2 = data
    getImages(pokemon)


def getImages(pokemon):
    images = []
    for i in range(2):
        name = pokemon[i]
        if (i == 0):
            img = poki1['sprites']['back_default']
            res = requests.get(img, stream=True)
            downloadImage(res, name)
            path = name + '.jpeg'
            images.append(path)
        elif (i == 1):
            img = poki2['sprites']['back_default']
            res = requests.get(img, stream=True)
            downloadImage(res, name)
            path = name + '.jpeg'
            images.append(path)

        image_path = images[i]  # Replace with the path to your JPEG 2000 image
        # jp2a command with image file path as argument
        cmd = f"jp2a {image_path}"
        output = subprocess.check_output(cmd, shell=True, text=True)
        print(output)


def downloadImage(res, name):
    fileName = str(name) + '.jpeg'
    if res.status_code == 200:
        with open(str(fileName), 'wb') as file:
            for chunk in res.iter_content(1024):
                file.write(chunk)
        return
        print('Image downloaded successfully.')
    else:
        print('Failed to download image. Status code:', res.status_code)
