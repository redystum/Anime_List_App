import eel
import time
import getData
import threading
import dbManager
import globalVars
import os

@eel.expose
def getAnime(data):
    animeList = getData.searchAnime(data)
    eel.chooseAnime(animeList)

@eel.expose
def AnimeData(data):
    animeData = getData.getAnimeData(data)
    if "error" in animeData:
        return animeData['error']
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

def changeJsFunction(id):
    while globalVars.adding_to_db:
        time.sleep(0.1)
    row = dbManager.getRowId(id)
    time.sleep(.5)
    eel.changeBtnId(row, id)


def close_callback(route, websockets):
    if globalVars.running_a_task:
        while globalVars.running_a_task:
            time.sleep(1)
            continue
    exit()


globalVars.init()

path = globalVars.path
if not os.path.exists(path):
    import setUpDb
    setUpDb.main()
    

eel.init('web', allowed_extensions=['.js', '.html'])
eel.start('index.html', close_callback=close_callback) # , mode='mozilla' for firefox
