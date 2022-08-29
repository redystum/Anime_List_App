"""
 python -m eel main.py web --onefile --noconsole
"""

import eel
import time
import os
import sys
import math
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
# project imports
import getData
import dbManager
import globalVars
import updater


global VERSION
VERSION = '1.2.0'

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
def exportAnimeList():
    path = getSavedDbLocation()
    if path != "" or path != False or path != None:
        return dbManager.exportAnimeList(path)
    return {"error": "No path selected"}

@eel.expose
def importSavedList(path, overWrite, importLoadFav, importLoadWatched, importLoadScore, importLoadNotes):
    return dbManager.importSavedList(path, overWrite, importLoadFav, importLoadWatched, importLoadScore, importLoadNotes)

@eel.expose
def chooseImportFile():
    path = getOpenDbLocation()
    if path == False or path == "":
        return {"info": "error", "message": "No file selected"}
    result, msg = dbManager.verifyDBFile(path)
    if result == True:
        return {"info": "success", "filePath": str(path), "message": str(msg)}
    else:
        return {"info": "error", "message": str(msg)}

@eel.expose
def getSavedDbLocation():
    file = App().saveFileDialog()
    return file

@eel.expose
def getOpenDbLocation():
    file = App().openFileNameDialog()
    return file

class App(QWidget):
    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, str("Import Anime List Save"), "", str("Data Base File (*.db)"))
        return fileName
    
    def saveFileDialog(self):
        fileName, _ = QFileDialog.getSaveFileName(self, str("Save Anime List Save"), "Anime_List_Save.db", str("Data Base File (*.db)"))
        return fileName


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
app = QApplication(["C:\\"])

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

