import sqlite3
import globalVars
import json
import getData
import datetime
globalVars.init()

def addAnimeToDb(data):
    globalVars.running_a_task = True
    globalVars.adding_to_db = True
    title = data['title'].replace('"', "'")
    titleJp = data['alternative_titles']['ja'].replace('"', "'")
    animeID = int(data['id'])
    image = data['main_picture']["large"].replace('"', "'")
    notes = "".replace('"', "'")
    startDate = data['start_date'].replace('"', "'")
    try:
        endDate = data['end_date'].replace('"', "'")
    except:
        endDate = "still being released"
    synopsis = data['synopsis'].replace('"', "'")
    episodes = data['num_episodes'] if data['num_episodes']!=0 else "Unknown"
    try:
        globalScore = float(data['mean'])
    except:
        globalScore = -9990
    localScore = float(0.0)
    viewed = 0
    status = data['status'].replace('"', "'")
    genres = ""
    for g in data['genres']:
        genres += g['name'].replace('"', "'") + ", "
    genres = genres[:-2]
    background = data['background'].replace('"', "'").replace('"', "'")
    pictures = [x['large'] for x in data['pictures']]
    averageEpDuration = data['average_episode_duration']
    studio = ""
    for s in data['studios']:
        studio += s['name'].replace('"', "'") + ", "
    studio = studio[:-2]
    relatedAnime = data['related_anime']
    relatedManga = data['related_manga']
    favorite = 0

    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    q = f'''INSERT INTO anime (title, titleJp, animeID, image, notes, startDate, endDate, synopsis, episodes, globalScore, localScore, pictures, viewed, status, genres, background, studio, relatedAnime, relatedManga, averageEpDuration, favorite, lastUpdate) VALUES ("{title}", "{titleJp}", "{animeID}", "{image}", "{notes}", "{startDate}", "{endDate}", "{synopsis}", "{episodes}", "{globalScore}", "{localScore}", "{pictures}", "{viewed}", "{status}", "{genres}", "{background}", "{studio}", "{relatedAnime}", "{relatedManga}", "{averageEpDuration}", "{favorite}", "{datetime.datetime.now()}")'''
    c.execute(q)
    conn.commit()
    conn.close()
    globalVars.running_a_task = False
    globalVars.adding_to_db = False

def getAnimeList(order):
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    q = 'SELECT * FROM anime'
    if order == 0:
        pass
    elif order == 'a-z':
        q += ' ORDER BY title'
    elif order == 'z-a':
        q += ' ORDER BY title DESC'
    elif order == 'l-g':
        q += ' ORDER BY globalScore'
    elif order == 'g-l':
        q += ' ORDER BY globalScore DESC'
    elif order == 'p-e':
        q += ' ORDER BY episodes'
    elif order == 'e-p':
        q += ' ORDER BY episodes DESC'
    elif order == 'd-i':
        q += ' ORDER BY animeID'
    elif order == 'i-d':
        q += ' ORDER BY animeID DESC'
    else:
        pass
    c.execute(q)
    animeList = c.fetchall()
    conn.close()
    names = list(map(lambda x: x[0], c.description))
    finalAnimeList = []
    for i in range(len(animeList)):
        animeList[i] = list(animeList[i])
        listWKeys = {}
        for j in range(len(animeList[i])):
            listWKeys[names[j]] = animeList[i][j]
        finalAnimeList.append(listWKeys)

    for i in finalAnimeList:
        i['pictures'] = eval(i['pictures'])
        i['relatedAnime'] = eval(i['relatedAnime'])
        i['relatedManga'] = eval(i['relatedManga'])
        i['viewed'] = bool(i['viewed'])
        i['favorite'] = bool(i['favorite'])

    return finalAnimeList

def deleteAnime(AnimeId):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'DELETE FROM anime WHERE id = {AnimeId}')
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

def viewedAnime(id):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'UPDATE anime SET viewed = 1 WHERE id = {id}')
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

def setUnviewed(id):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'UPDATE anime SET viewed = 0, favorite = 0 WHERE id = {id}')
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

def getRowId(Animeid):
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'SELECT id FROM anime WHERE animeID = {Animeid}')
    rowId = list(c.fetchall())[-1][0]
    conn.close()
    return rowId

def getAnimeInfo(AnimeId):
    settings = getSettings()
    if settings != 0:
        if settings['updateOnInfo'] == True:
            updateAnime(AnimeId)

    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM anime WHERE animeID = {AnimeId}')
    animeList = c.fetchall()
    conn.close()
    names = list(map(lambda x: x[0], c.description))
    finalAnimeList = []
    for i in range(len(animeList)):
        animeList[i] = list(animeList[i])
        listWKeys = {}
        for j in range(len(animeList[i])):
            listWKeys[names[j]] = animeList[i][j]
        finalAnimeList.append(listWKeys)

    for i in finalAnimeList:
        i['pictures'] = eval(i['pictures'])
        i['relatedAnime'] = eval(i['relatedAnime'])
        i['relatedManga'] = eval(i['relatedManga'])
        i['viewed'] = bool(i['viewed'])
    
    return finalAnimeList[0]

def updateNotesScore(notes, score, id):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    q = f'''SELECT animeId from anime WHERE id = {id}'''
    c.execute(q)
    animeId = c.fetchall()[0][0]
    conn.commit()
    conn.close()
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    q = f'''UPDATE anime SET notes = "{notes.replace('"', "'")}"'''
    if score != "":
        q += f', localScore = "{score}"'

    q += f' WHERE animeId = {animeId}'
    c.execute(q)
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

def favAnime(id):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'UPDATE anime SET favorite = 1 WHERE id = {id}')
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

def unFavAnime(id):
    globalVars.running_a_task = True
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'UPDATE anime SET favorite = 0 WHERE id = {id}')
    conn.commit()
    conn.close()
    globalVars.running_a_task = False


def checkToken():
    from Tokens import tokenManager
    tk = tokenManager.request()
    if tk['Info'] == "Success":
        if tk['Data'] != "" or tk['Data'] != 0 or tk['Data'] != "0" or tk['Data'] != None:
            return True
    return False

def updateClient(clientId):
    globalVars.running_a_task = True
    from Tokens import tokenManager
    tokenManager.update(clientId)
    globalVars.running_a_task = False

def onDbCheck(AnimeId):
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM anime WHERE animeID = {AnimeId}')
    animeList = c.fetchall()
    conn.close()
    if len(animeList) == 0:
        return False
    else:
        return True

def getFavList():
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute('SELECT * FROM anime WHERE favorite = 1 ORDER BY localScore DESC')
    animeList = c.fetchall()
    conn.close()
    names = list(map(lambda x: x[0], c.description))
    finalAnimeList = []
    for i in range(len(animeList)):
        animeList[i] = list(animeList[i])
        listWKeys = {}
        for j in range(len(animeList[i])):
            listWKeys[names[j]] = animeList[i][j]
        finalAnimeList.append(listWKeys)

    for i in finalAnimeList:
        i['pictures'] = eval(i['pictures'])
        i['relatedAnime'] = eval(i['relatedAnime'])
        i['relatedManga'] = eval(i['relatedManga'])
        i['viewed'] = bool(i['viewed'])
    
    return finalAnimeList

def getCssFile():
    try:
        open(globalVars.path + 'settings.json', 'r')
    except FileNotFoundError:
        return 0
    with open(globalVars.path + 'settings.json', 'r') as f:
        data = json.load(f)
    return data['cssFile'] if data['cssFile'] != 0 else 0
    
def getSettings():
    try:
        open(globalVars.path + 'settings.json', 'r')
    except FileNotFoundError:
        return 0
    with open(globalVars.path + 'settings.json', 'r') as f:
        data = json.load(f)
    return data

def setTheme(theme):
    globalVars.running_a_task = True
    template = """{
    "cssFile": 0,
    "themeId": 1,
    "markAirAnime": false,
    "updateOnInfo": false
    }
    """
    templateJson = json.loads(template)
    try:
        open(globalVars.path + 'settings.json', 'r')
    except FileNotFoundError:
        f = open(globalVars.path + 'settings.json', 'w')
        json.dump(templateJson, f, indent=4)
        f.close()

    with open(globalVars.path + 'settings.json', 'r') as f:
        data = json.load(f)
    data['themeId'] = theme
    if theme == 0:
        data['cssFile'] = 0
    elif theme == 1:
        data['cssFile'] = "style.css"
    elif theme == 2:
        data['cssFile'] = "styleMono.css"
    elif theme == 3:
        data['cssFile'] = "styleWhite.css"
    elif theme == 4:
        data['cssFile'] = "styleWhiteMono.css"

    with open(globalVars.path + 'settings.json', 'w') as f:
        json.dump(data, f, indent=4)

    globalVars.running_a_task = False

def setOtherOptions(option):
    globalVars.running_a_task = True
    template = """{
    "cssFile": 0,
    "themeId": 1,
    "markAirAnime": false,
    "updateOnInfo": false,
    "ListStatus": false
    }
    """
    templateJson = json.loads(template)
    try:
        open(globalVars.path + 'settings.json', 'r')
    except FileNotFoundError:
        f = open(globalVars.path + 'settings.json', 'w')
        json.dump(templateJson, f, indent=4)
        f.close()

    with open(globalVars.path + 'settings.json', 'r') as f:
        data = json.load(f)

    for i in templateJson:
        if i not in data:
            data[list(templateJson.keys())[i]] = templateJson[list(templateJson.keys())[i]]

    if option == "markAirAnime":
        data['markAirAnime'] = not data['markAirAnime']
    elif option == "updateOnInfo":
        data['updateOnInfo'] = not data['updateOnInfo']
    elif option == "listStatus":
        data['ListStatus'] = not data['ListStatus']

    with open(globalVars.path + 'settings.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    globalVars.running_a_task = False


def updateAnime(animeId):
    globalVars.running_a_task = True
    globalVars.adding_to_db = True
    data = getData.getAnimeData(animeId)
    title = data['title'].replace('"', "'")
    titleJp = data['alternative_titles']['ja'].replace('"', "'")
    animeID = int(data['id'])
    image = data['main_picture']["large"].replace('"', "'")
    notes = "".replace('"', "'")
    startDate = data['start_date'].replace('"', "'")
    try:
        endDate = data['end_date'].replace('"', "'")
    except:
        endDate = "still being released"
    synopsis = data['synopsis'].replace('"', "'")
    episodes = data['num_episodes'] if data['num_episodes']!=0 else "Unknown"
    try:
        globalScore = float(data['mean'])
    except:
        globalScore = -9990
    status = data['status'].replace('"', "'")
    genres = ""
    for g in data['genres']:
        genres += g['name'].replace('"', "'") + ", "
    genres = genres[:-2]
    background = data['background'].replace('"', "'").replace('"', "'")
    pictures = [x['large'] for x in data['pictures']]
    averageEpDuration = data['average_episode_duration']
    studio = ""
    for s in data['studios']:
        studio += s['name'].replace('"', "'") + ", "
    studio = studio[:-2]
    relatedAnime = data['related_anime']
    relatedManga = data['related_manga']
    lastUpdate = datetime.datetime.now()

    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    q = f'''UPDATE anime SET title="{title}", titleJp="{titleJp}", animeID="{animeID}", image="{image}", startDate="{startDate}", endDate="{endDate}", synopsis="{synopsis}", episodes="{episodes}", globalScore="{globalScore}", pictures="{pictures}", status="{status}", genres="{genres}", background="{background}", studio="{studio}", relatedAnime="{relatedAnime}", relatedManga ="{relatedManga}", averageEpDuration="{averageEpDuration}", lastUpdate="{lastUpdate}" WHERE animeID={animeID}'''
    c.execute(q)
    conn.commit()
    conn.close()
    globalVars.running_a_task = False
    globalVars.adding_to_db = False

def updateDBonUpdate():
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'SELECT * FROM anime')
    conn.commit()
    conn.close()
    names = list(map(lambda x: x[0], c.description))

    if "lastUpdate" not in names:
        conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
        c = conn.cursor()
        c.execute(f'ALTER TABLE anime ADD COLUMN lastUpdate TEXT')
        conn.commit()
        conn.close()

def deleteAllAnimes():
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'''DELETE FROM anime''')
    c.execute("DELETE FROM sqlite_sequence WHERE name='anime'")
    conn.commit()
    conn.close()

def exportAnimeList(path):
    globalVars.running_a_task = True
    try:
        conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
        c = conn.cursor()
        q = 'SELECT * FROM anime'
        c.execute(q)
        animeList = c.fetchall()
        conn.close()
        names = list(map(lambda x: x[0], c.description))
        finalAnimeList = []
        for i in range(len(animeList)):
            animeList[i] = list(animeList[i])
            listWKeys = {}
            for j in range(len(animeList[i])):
                listWKeys[names[j]] = animeList[i][j]
            finalAnimeList.append(listWKeys)

        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute('''DROP TABLE IF EXISTS anime''')
        conn.commit()
        conn.close()
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS 
        anime(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, titleJp TEXT, animeID INTEGER, image TEXT, notes TEXT, startDate TEXT, endDate TEXT, synopsis TEXT, episodes INTEGER, averageEpDuration INTEGER, globalScore FLOAT, localScore FLOAT, pictures TEXT, viewed BOOLEAN, status TEXT, genres TEXT, background TEXT, studio TEXT, relatedAnime TEXT, relatedManga TEXT, favorite BOOLEAN, lastUpdate TEXT)''')
        conn.commit()
        conn.close()
        conn = sqlite3.connect(path)
        c = conn.cursor()
        for anime in finalAnimeList:
            c.execute(f'''INSERT INTO anime VALUES (NULL, "{anime['title']}", "{anime['titleJp']}", "{anime['animeID']}", "{anime['image']}", "{anime['notes']}", "{anime['startDate']}", "{anime['endDate']}", "{anime['synopsis']}", "{anime['episodes']}", "{anime['averageEpDuration']}", "{anime['globalScore']}", "{anime['localScore']}", "{anime['pictures']}", "{anime['viewed']}", "{anime['status']}", "{anime['genres']}", "{anime['background']}", "{anime['studio']}", "{anime['relatedAnime']}", "{anime['relatedManga']}", "{anime['favorite']}","{anime['lastUpdate']}")''')
        conn.commit()
        conn.close()
    except Exception as e:
        globalVars.running_a_task = False
        return {"error": str(e)}
    globalVars.running_a_task = False
    return True


def importSavedList(path, overWrite, importLoadFav, importLoadWatched, importLoadScore, importLoadNotes):
    globalVars.running_a_task = True
        
    try:
        if overWrite == True:
            deleteAllAnimes()

        conn = sqlite3.connect(path)
        c = conn.cursor()
        q = 'SELECT * FROM anime'
        c.execute(q)
        animeList = c.fetchall()
        conn.close()
        names = list(map(lambda x: x[0], c.description))
        finalAnimeList = []
        for i in range(len(animeList)):
            animeList[i] = list(animeList[i])
            listWKeys = {}
            for j in range(len(animeList[i])):
                listWKeys[names[j]] = animeList[i][j]
            finalAnimeList.append(listWKeys)

        conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
        c = conn.cursor()

        for anime in finalAnimeList:
            if importLoadFav == False:
                anime['favorite'] = 0
            if importLoadWatched == False:
                anime['viewed'] = 0
            if importLoadScore == False:
                anime['localScore'] = ""
            if importLoadNotes == False:
                anime['notes'] = ""
            c.execute(f'''INSERT INTO anime VALUES (NULL, "{anime['title']}", "{anime['titleJp']}", "{anime['animeID']}", "{anime['image']}", "{anime['notes']}", "{anime['startDate']}", "{anime['endDate']}", "{anime['synopsis']}", "{anime['episodes']}", "{anime['averageEpDuration']}", "{anime['globalScore']}", "{anime['localScore']}", "{anime['pictures']}", "{anime['viewed']}", "{anime['status']}", "{anime['genres']}", "{anime['background']}", "{anime['studio']}", "{anime['relatedAnime']}", "{anime['relatedManga']}", "{anime['favorite']}","{anime['lastUpdate']}")''')
        conn.commit()
        conn.close()
    except Exception as e:
        globalVars.running_a_task = False
        print(e)
        return False
    globalVars.running_a_task = False
    return True

def verifyDBFile(path):
    try:
        conn = sqlite3.connect(path)
        c = conn.cursor()
        q = 'SELECT * FROM anime'
        c.execute(q)
        animeList = c.fetchall()
        conn.close()
        if len(animeList) == 0:
            return False, 'The selected file does not contain any saved anime'
    except:
        return False, "The selected file is not a valid anime list save"
    
    return True, str(len(animeList)) + " Anime found"

def getTableInfos():
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()

    q = ['SELECT count(*) from anime where viewed=true', 'SELECT count(*) from anime where viewed=false', 'SELECT sum(episodes) from anime where viewed=true', 'SELECT sum(episodes) from anime where viewed=false', 'SELECT sum(averageEpDuration*episodes) from anime where viewed=true', 'SELECT sum(averageEpDuration*episodes) from anime where viewed=false']
    result = {
        'watched': 0,
        'notWatched': 0,
        'watchedEpisodes': 0,
        'notWatchedEpisodes': 0,
        'watchedDuration': 0,
        'notWatchedDuration': 0
    }

    for i, query in enumerate(q):
        c.execute(query)
        response = c.fetchall()[0][0]
        result[list(result.keys())[i]] = response if response != None else 0

    result['watchedDuration'] = datetime.datetime.utcfromtimestamp(result['watchedDuration']).strftime('%Hh%Mm')
    result['notWatchedDuration'] = datetime.datetime.utcfromtimestamp(result['notWatchedDuration']).strftime('%Hh%Mm')

    conn.close()
    return result

if __name__ == '__main__':
    getAnimeList()