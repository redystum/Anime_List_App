import requests
import sqlite3
import os
from cryptography.fernet import Fernet

def request(parameter=False):
    if not parameter:
        return {'Info': 'Error', 'Data': 'No parameter'}
    if parameter not in ['client_id', 'token', 'refresh_token']:
        return {'Info': 'Error', 'Data': 'Invalid parameter'}

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
        query = 'token' if parameter == 'token' else ('refreshToken' if parameter == 'refresh_token' else 'clientId')
        c.execute(f'''SELECT {query} FROM tokens WHERE id = 1''')
        token = c.fetchone()[0]
        conn.commit()
        conn.close()

        tokenD = decryptToken(token)
        tokenD = tokenD[:-1] if tokenD[-1] == ' ' else tokenD
    except:
        return {'Info': 'Error', 'Data': 'Database error'}

    return {'Info': 'Success', 'Data': tokenD}


def update(token=0, client_id=0, refresh_token=0):
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
        query = '''UPDATE tokens SET '''
        first = 0
        if client_id != 0:
            query += ',' if first != 0 else ''
            client_idE = encryptToken(str(client_id))
            query += f'''clientId = "{str(client_idE)}"'''
            first = 1
        if token != 0:
            query += ',' if first != 0 else ''
            tokenE = encryptToken(str(token))
            query += f'''token = "{str(tokenE)}"'''
            first = 1
        if refresh_token != 0:
            query += ',' if first != 0 else ''
            refresh_tokenE = encryptToken(str(refresh_token))
            query += f'''refreshToken = "{str(refresh_tokenE)}"'''
            first = 1   

        query += ''' WHERE id = 1''' 
        c.execute(query)
        conn.commit()
        conn.close()
    except:
        return {'Info': 'Error', 'Data': 'Database error'}
    return {'Info': 'Success'}

def refreshToken():
    try:
        roaming = os.getenv('APPDATA')
    except:
        return {'Info': 'Error', 'Data': 'No roaming folder found'}

    if not os.path.exists(roaming + '\\AnimeList\\data\\LocalStorage.db'):
        return {'Info': 'Error', 'Data': 'Database not found'}

    refresh_token = request('refresh_token')
    clientId = request('client_id')

    if refresh_token['Info'] != 'Success':
        return refresh_token
    if clientId['Info'] != 'Success':
        return clientId

    refresh_token = refresh_token['Data']
    clientId = clientId['Data']
    
    try:
        url = 'https://myanimelist.net/v1/oauth2/token'
        data = {
            'client_id': clientId,
            'client_secret': '',
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        }
        response = requests.post(url, data=data)
    except:
        return {'Info': 'Error', 'Data': 'Network error'}
    return {'Info': 'Success', 'Data': response.json()}

def getToken():
    response = request('token')
    return response['Data'] if response['Info'] == 'Success' else response
def getClient():
    response = request('client_id')
    return response['Data'] if response['Info'] == 'Success' else response
def getRefresh():
    response = request('refresh_token')
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
    print(getToken())
    print(getClient())
    print(getRefresh())