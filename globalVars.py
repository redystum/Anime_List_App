import os

def init():
    global running_a_task
    running_a_task = False
    global path
    path = os.getenv('APPDATA') + '\\AnimeList\\data\\'
    global adding_to_db
    adding_to_db = False