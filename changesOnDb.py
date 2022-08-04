import sqlite3
import os

roaming = os.getenv('APPDATA')

path = roaming + '\\AnimeList\\data\\'

conn = sqlite3.connect(path + 'LocalStorage.db')

c = conn.cursor()

c.execute('DELETE FROM anime WHERE id = 6')
# c.execute('DROP TABLE anime')



conn.commit()
conn.close()
