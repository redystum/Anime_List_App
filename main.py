"""
 python -m eel main.py web --onefile --noconsole
"""

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

global VERSION
VERSION = '1.0.0'

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
def checkForUpdates():
    return updater.checkForUpdates(VERSION)

@eel.expose
def updateApp():
    if os.path.exists("updater.exe"):
        eel.exitApp()
        os.system("updater.exe update")
        sys.exit()
    else:
        eel.showToast("Error", "Something went wrong while updating the app! Go to my github and update manually <a href='https://github.com/redystum/Anime_List_App/releases' class='visibleLink'>Click Here</a>", "red", "black")

def onDbCheck(id):
    r = dbManager.onDbCheck(id)    
    if r:
        eel.showToast("Info", "Just to know that the anime you added was already on the list.", "soft-green", "soft-black")

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
    

eel.init('web', allowed_extensions=['.js', '.html'])
try:
    eel.start(f'{file}.html', close_callback=close_callback) # , mode='mozilla' for firefox
except OSError:
    try:
        eel.start(f'{file}.html', close_callback=close_callback, port=8001) # , mode='mozilla' for firefox
    except OSError:
        sys.exit()

