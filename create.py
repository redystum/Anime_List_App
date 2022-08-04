import os
import sqlite3
import globalVars
globalVars.init()

def main(reset=False):
    path = globalVars.path
    if reset:
        if os.path.exists(path):
            os.remove(path)

    if not os.path.exists(path):
        os.makedirs(path)

    conn = sqlite3.connect(path + 'LocalStorage.db')

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS 
    tokens(id INTEGER PRIMARY KEY AUTOINCREMENT, clientId TEXT, token TEXT, refreshToken TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS 
    anime(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, titleJp TEXT, animeID INTEGER, image TEXT, notes TEXT, startDate TEXT, endDate TEXT, synopsis TEXT, episodes INTEGER, averageEpDuration INTEGER, globalScore FLOAT, localScore FLOAT, pictures TEXT, viewed BOOLEAN, status TEXT, genres TEXT, background TEXT, studio TEXT, relatedAnime TEXT, relatedManga TEXT)''')

    c.execute('''INSERT INTO tokens (clientId, token, refreshToken) VALUES(0, 0, 0)''')

    conn.commit()
    conn.close()

def test(): # delete this later
    path = globalVars.path
    if not os.path.exists(path):
        print('run main first')

    conn = sqlite3.connect(path + 'LocalStorage.db')

    c = conn.cursor()

    clientID = 123465789
    token = 1234567890
    refreshToken = 1234567890123456

    jsontest = [
        {
            "node": {
                "id": 31,
                "title": "Neon Genesis Evangelion: Death & Rebirth",
                "main_picture": {
                    "medium": "https://api-cdn.myanimelist.net/images/anime/1993/113122.jpg",
                    "large": "https://api-cdn.myanimelist.net/images/anime/1993/113122l.jpg"
                }
            },
            "relation_type": "summary",
            "relation_type_formatted": "Summary"
        },
        {
            "node": {
                "id": 32,
                "title": "Neon Genesis Evangelion: The End of Evangelion",
                "main_picture": {
                    "medium": "https://api-cdn.myanimelist.net/images/anime/1404/98182.jpg",
                    "large": "https://api-cdn.myanimelist.net/images/anime/1404/98182l.jpg"
                }
            },
            "relation_type": "sequel",
            "relation_type_formatted": "Sequel"
        }]



    # c.execute(f'''INSERT INTO tokens (clientId, token, refreshToken) VALUES({clientID}, {token}, {refreshToken})''') 

    c.execute(f'''INSERT INTO anime (title,animeID, image, startDate, endDate, synopsis, episodes, globalScore, localScore, viewed, status, genres, background, studio, relatedAnime, relatedManga, notes, titleJp, averageEpDuration, pictures) VALUES('title test', 123, 'img link', '32/8/10000', '32/8/10000', 'ganda anime tipo mm inclivel tasa ver', 12, 8.0, 7.0, 0, 'full', 'action', 'back dos grounds', 'studio studio', "{jsontest}", "{jsontest}", 'something', '\u3088\u3046\u3053\u305d\u5b9f\u529b\u81f3\u4e0a\u4e3b\u7fa9\u306e\u6559\u5ba4\u3078',1440, "{jsontest}")''') 

    conn.commit()
    conn.close()

if __name__ == '__main__':
    test()

