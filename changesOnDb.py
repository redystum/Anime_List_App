import sqlite3
import os

"""
file to make specific manual changes that are not part of the app.
basically it is for testing
"""

roaming = os.getenv('APPDATA')

path = roaming + '\\AnimeList\\data\\'

conn = sqlite3.connect(path + 'LocalStorage.db')

c = conn.cursor()

c.execute('update anime set favorite = 0 where id = 84')
c.execute('update anime set favorite = 1 where id = 85')
c.execute('update anime set favorite = 0 where id = 87')
# c.execute('DROP TABLE anime')



conn.commit()
conn.close()
