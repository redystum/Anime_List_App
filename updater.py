"""

this file besides being called by the main program must also be converted to .exe (pyinstaller) separately, because it acts as another program to be able to update the main .exe

"""

import zipfile
import os
import requests

def checkForUpdates(version, instal=0):
    currentVersion = version.split(".")
    response = requests.get("https://api.github.com/repos/redystum/Anime_List_App/releases")
    data = response.json()
    url = ''
    for i in data:
        ver = i['tag_name'].replace('V','').split('.')
        if ver[0] > currentVersion[0] or ver[1]  > currentVersion[1]:
            url = i
            break
    if url == '':
        return {'info': 'updated'}
    else:
        if instal == 1:
            return {'info': 'update', 'url': url['assets'][0]['browser_download_url']}
        return {'info': 'old', 'version': url['tag_name'], 'body': i['body']}

def updateApp():
    try:
        url = checkForUpdates("V0.0.0", 1)['url']
        r = requests.get(url)
        with open("animeApp.exe", "wb") as f:
            f.write(r.content)
        os.system(".\\animeApp.exe")
    except Exception as e:
        print('Something went wrong: ' + str(e))

if __name__ == "__main__":
    import os
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "update":
            print("Updating")
            updateApp()
            sys.exit()
        else:
            print("No valid arguments provided")
            sys.exit()
    else:
        print("No valid arguments provided")
        sys.exit()