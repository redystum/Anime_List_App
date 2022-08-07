import sqlite3
import os
from cryptography.fernet import Fernet

def request():
    try:
        roaming = os.getenv('APPDATA')
    except:
        return {'Info': 'Error', 'Data': 'No roaming folder found'}

    if not os.path.exists(roaming + '\\AnimeList\\data\\LocalStorage.db'):
        return {'Info': 'Error', 'Data': 'Database not found'}

    try:
        path = roaming + '\\AnimeList\\data\\'
        conn = sqlite3.connect(path + 'LocalStorage.db')
        c = conn.cursor()
        c.execute('''SELECT clientId FROM tokens WHERE id = 1''')
        token = c.fetchone()[0]
        conn.commit()
        conn.close()

        tokenD = decryptToken(token)
        tokenD = tokenD[:-1] if tokenD[-1] == ' ' else tokenD
    except:
        return {'Info': 'Error', 'Data': 'Database error'}

    return {'Info': 'Success', 'Data': tokenD}

def update(client_id):
    try:
        roaming = os.getenv('APPDATA')
    except:
        return {'Info': 'Error', 'Data': 'No roaming folder found'}

    if not os.path.exists(roaming + '\\AnimeList\\data\\LocalStorage.db'):
        return {'Info': 'Error', 'Data': 'Database not found'}

    try:
        client_idE = encryptToken(str(client_id))

        path = roaming + '\\AnimeList\\data\\'
        conn = sqlite3.connect(path + 'LocalStorage.db')
        c = conn.cursor()
        query = f'''UPDATE tokens SET clientId = "{str(client_idE)} WHERE id = 1'''
        c.execute(query)
        conn.commit()
        conn.close()
    except:
        return {'Info': 'Error', 'Data': 'Database error'}
    return {'Info': 'Success'}

def getClient():
    response = request('client_id')
    return response['Data'] if response['Info'] == 'Success' else response

def encryptToken(text):
    key = b'Z_o7m9cRDZP9JzPNu2p2KnO06KewlnyQwXCl3gQ4vo8='
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def decryptToken(text):
    key = b'Z_o7m9cRDZP9JzPNu2p2KnO06KewlnyQwXCl3gQ4vo8='
    f = Fernet(key)
    return f.decrypt(text.encode()).decode()


if __name__ == '__main__':
    print(getClient())