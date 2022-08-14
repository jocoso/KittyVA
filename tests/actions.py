import requests
import random
import os

DIR_FILE = "../resources/dirfile.txt"

""" Gives you a bad joke """
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

""" Opens directory iff directory exists """
def open_directory(dir):

    try:
        path = os.path.realpath(dir)
        os.startfile(path)
        return True
    
    except FileNotFoundError:
        return False

# TODO: Make a class out of this 
""" Save directory give in a txt file for future retrieval """
def save_directory(dir):
    
    file = open(DIR_FILE, 'a+')

    if(open_directory(dir)):
        # If directory exists
        realpath = os.path.realpath(dir).strip()

        # Do not add to the list if it is already in the list
        if not in_directory_list(realpath):
            file.write(realpath + '\n')
            print("Added") 
        else:
            print("Directory was already added")
            
    else:
        print("Directory does not exist")

    file.close()

""" Check if directory is true """
def in_directory_list(dir):
    
    file = open(DIR_FILE).readlines()

    for line in file:
        # For some reason the readlines comes with // instead of /
        line = line.replace('//', '/').strip()
        if line.strip() == dir:
            return True
        
    return False

