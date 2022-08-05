import eel
import time
import getData
import threading
import dbManager
import globalVars

@eel.expose
def getAnime(data):
    animeList = getData.searchAnime(data)
    eel.chooseAnime(animeList)

@eel.expose
def AnimeData(data):
    animeData = getData.getAnimeData(data)
    if "error" in animeData:
        return animeData['error']
    globalVars.running_a_task = True
    globalVars.adding_to_db = True
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
def viewedAnime(data):
    dbManager.viewedAnime(data)

@eel.expose
def getAnimeInfo(data):
    return dbManager.getAnimeInfo(data)

@eel.expose
def updateNotesAndScore(notes, score, id):
    dbManager.updateNotesScore(notes, score, id)

def changeJsFunction(id):
    while globalVars.adding_to_db:
        time.sleep(0.1)
    row = dbManager.getRowId(id)
    eel.changeBtnId(row)


def close_callback(route, websockets):
    if globalVars.running_a_task:
        while globalVars.running_a_task:
            time.sleep(1)
            continue
    exit()


globalVars.init()
eel.init('web', allowed_extensions=['.js', '.html'])
eel.start('index.html', close_callback=close_callback) # , mode='mozilla' for firefox
