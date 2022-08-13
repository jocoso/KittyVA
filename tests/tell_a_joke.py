import requests
import random


def get_joke():
    # Setting up the API Connection
    information = requests.get("https://icanhazdadjoke.com/search", headers= {"Accept":"application/json"})
    connection = information.ok

    # Getting a bunch of jokes
    result = information.json()
    jokes = result['results']

    # Return one random joke
    selected = random.randrange(1, 20, 3)
    return jokes[selected]['joke']

