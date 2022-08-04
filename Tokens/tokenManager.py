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

    print(update('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjlhZjJhOTMwYzEzN2QyMDk1ZDJhMWY3M2MyYzA3MjhmMDUwNzc0ODE1MGExMDQxZDA0MDAwNTMxNTNhZWViNDczZTg3NGI1NDYwN2QyOTQ1In0.eyJhdWQiOiIwMGEyY2ZiNmNkMTcwYzIwZTk3YmU1OGM4NmEwMGY3MSIsImp0aSI6IjlhZjJhOTMwYzEzN2QyMDk1ZDJhMWY3M2MyYzA3MjhmMDUwNzc0ODE1MGExMDQxZDA0MDAwNTMxNTNhZWViNDczZTg3NGI1NDYwN2QyOTQ1IiwiaWF0IjoxNjU5MDExOTgxLCJuYmYiOjE2NTkwMTE5ODEsImV4cCI6MTY2MTY5MDM4MSwic3ViIjoiMTU0MDI0ODciLCJzY29wZXMiOltdfQ.rWYwAZ1T7lI5ZfjkVFNrg43G4mOWEnUxSXnbZaNDW_UaWCLIAYRaqaLNXCmPrfw7J8B5Nj5IlRU0E4QjWnwm048cyeBL5M5GhluqOk92b3GTYGhuXtcOwgEXUaltSIXyUq0Dq65h4-Sq_RmKRRBF_Dz8Qqn3kNJgQiW1VvZELT4VO9j4M17r1MbadQUNZ_pHwB_sPp8QYllzpwc66Hd4bYRnsIaLr8rivWUqM3kqJHa5lPDMZmKBYh4icJm0vJvohNxmU7wYeIPc1UgNKIkMFmXxxFkhuxH-Y1lSvBptMNE4k-KaBQ75ygjtj_JiGvu665KWWJ--Bi147BsLLphA9w',
'00a2cfb6cd170c20e97be58c86a00f71',
'def50200bb0599305186e40f97377a86e0547d87dc92e097d3bcfcd2b11708a9771c0898300868e4c2687325771ee97066ec81e0b064c4fbea43cb00c05fffcc871a9e543d5890a351d3a89abd6bbbb2d2f5003472d23c6addcf1d0addd6b52b959ab958bfe96028ac2faac5e6dfc5a754619a02d1ccf1ffade7685a6cd77e0bea417e0d6dc233bcf3b026445762bb2177dd022dbd355e000d493d6343f05931058a1247b7047866e4c9db9222875a5502dafdb5a5c180759594470ca8fbd6efd471a5980fede0b8b1496d9b31e77fc935ef28fdccd0dee305719d17f967c2faa8362ee499ad5821f5107254ab1ae8bfe79049a92c0cc625e91c5051663c19d0c72eda25d4a2fa0f9d7ac621cb18194e34a0232c4cca2a8d1791113e073e2e1e72008b2f6097da03ba9a007ba095f387f41e219927548bb7a23d06d84d7134860095a562e9aad1777779b4292ee42fe6503203b38b0213f02fade806607daa35799482be21358751d8ce5e44262d1ce9422c23a03df1c0d8cd346a9c279c38a77bc83ba360e6792da4'))