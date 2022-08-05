import sqlite3
import globalVars
globalVars.init()

def addAnimeToDb(data):
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
    globalScore = float(data['mean'])
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
    q = f'''INSERT INTO anime (title, titleJp, animeID, image, notes, startDate, endDate, synopsis, episodes, globalScore, localScore, pictures, viewed, status, genres, background, studio, relatedAnime, relatedManga, averageEpDuration, favorite) VALUES ("{title}", "{titleJp}", "{animeID}", "{image}", "{notes}", "{startDate}", "{endDate}", "{synopsis}", "{episodes}", "{globalScore}", "{localScore}", "{pictures}", "{viewed}", "{status}", "{genres}", "{background}", "{studio}", "{relatedAnime}", "{relatedManga}", "{averageEpDuration}", "{favorite}")'''
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

def getRowId(Animeid):
    conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
    c = conn.cursor()
    c.execute(f'SELECT id FROM anime WHERE animeID = {Animeid}')
    rowId = list(c.fetchall())[-1][0]
    conn.close()
    return rowId

def getAnimeInfo(AnimeId):
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
    q = f'''UPDATE anime SET notes = "{notes.replace('"', "'")}"'''
    if score != "":
        q += f', localScore = "{score}"'

    q += f' WHERE id = {id}'
    c.execute(q)
    conn.commit()
    conn.close()
    globalVars.running_a_task = False

if __name__ == '__main__':
    getAnimeList()