"""
 python -m eel main.py web --onefile --noconsole
"""

import pathlib
import eel
import time
import os
import sys
# project imports
import getData
import threading
import dbManager
import globalVars
import updater
import math
import subprocess

global VERSION
VERSION = '1.1.0'

@eel.expose
def getAnime(data):
    animeList = getData.searchAnime(data)
    eel.chooseAnime(animeList)

@eel.expose
def AnimeData(data):
    animeData = getData.getAnimeData(data)
    if "error" in animeData:
        return animeData['error']
    # onDbCheck_ = threading.Thread(target=onDbCheck, args=(animeData['id'],))
    # onDbCheck_.start()
    onDbCheck(animeData['id'])
    saveDb = threading.Thread(target=dbManager.addAnimeToDb, args=(animeData,))
    saveDb.start()
    changeJs = threading.Thread(target=changeJsFunction, args=(animeData['id'],))
    changeJs.start()
    return animeData

@eel.expose
def getAnimeList(data):
    return dbManager.getAnimeList(data)

@eel.expose
def deleteAnime(data):
    dbManager.deleteAnime(data)

@eel.expose
def setViewed(data):
    dbManager.viewedAnime(data)

@eel.expose
def setUnviewed(data):
    dbManager.setUnviewed(data)

@eel.expose
def getAnimeInfo(data):
    return dbManager.getAnimeInfo(data)

@eel.expose
def updateNotesAndScore(notes, score, id):
    dbManager.updateNotesScore(notes, score, id)

@eel.expose
def favAnime(data):
    dbManager.favAnime(data)

@eel.expose
def unFavAnime(data):
    dbManager.unFavAnime(data)

@eel.expose
def checkToken(data):
    r = getData.checkToken(data)
    if r['status'] == "success":
        updateDb = threading.Thread(target=dbManager.updateClient, args=(data,))
        updateDb.start()
    return r
    
@eel.expose
def getFavList():
    return dbManager.getFavList()

def changeJsFunction(id):
    while globalVars.adding_to_db:
        time.sleep(0.1)
    row = dbManager.getRowId(id)
    time.sleep(.5)
    eel.changeBtnId(row, id)
@eel.expose
def dbSize():
    file_stat = os.stat(globalVars.path + 'LocalStorage.db')
    size_bytes = file_stat.st_size
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
    
@eel.expose
def cssFile():
    return dbManager.getCssFile() if dbManager.getCssFile()!=0 else "style.css"

@eel.expose
def getSettings():
    return dbManager.getSettings()

@eel.expose
def setTheme(data):
    dbManager.setTheme(data)

@eel.expose
def setOtherOptions(data):
    dbManager.setOtherOptions(data)

@eel.expose
def updateAnime(data):
    dbManager.updateAnime(data)

@eel.expose
def deleteAllAnimes():
    dbManager.deleteAllAnimes()

@eel.expose
def deleteAllData():
    globalVars.running_a_task = True
    os.remove(globalVars.path + 'LocalStorage.db')
    os.remove(globalVars.path + 'settings.json')
    globalVars.running_a_task = False


@eel.expose
def checkForUpdates():
    return updater.checkForUpdates(VERSION)

@eel.expose
def updateApp():
    updater.updateApp()

def onDbCheck(id):
    r = dbManager.onDbCheck(id)    
    if r:
        eel.showToast("Info", "Just to know that the anime you added was already on the list.", "soft-green", "soft-primary")

def close_callback(route, websockets):
    if globalVars.running_a_task:
        while globalVars.running_a_task:
            time.sleep(1)
            print("Waiting for task to finish")
            continue
    print("Closing")
    sys.exit()

globalVars.init()

path = globalVars.path
if not os.path.exists(path + "LocalStorage.db"):
    globalVars.running_a_task = True
    import setUpDb
    setUpDb.main()
    globalVars.running_a_task = False
    file = "getStarted"
else:
    tk = dbManager.checkToken();
    if tk == False:
        file = "getStarted"
    else:
        file = "index"
        dbManager.updateDBonUpdate()
    

eel.init('web', allowed_extensions=['.js', '.html', '.css'])
try:
    eel.start(f'{file}.html', close_callback=close_callback) # , mode='mozilla' for firefox
except OSError:
    try:
        eel.start(f'{file}.html', close_callback=close_callback, port=8001) # , mode='mozilla' for firefox
    except OSError:
        sys.exit()

