"""

this file besides being called by the main program must also be converted to .exe (pyinstaller) separately, because it acts as another program to be able to update the main .exe

not anymore....

"""

import os
import requests


def checkForUpdates(version, instal=0):
    currentVersion = version.replace("V", "").split(".")
    response = requests.get(
        "https://api.github.com/repos/redystum/Anime_List_App/releases")
    data = response.json()
    url = ''
    for i in data:
        ver = i['tag_name'].replace('V', '').split('.')
        if ver[0] > currentVersion[0] or ver[1] > currentVersion[1]:
            url = i
            break
    if url == '':
        return {'info': 'updated'}
    else:
        if instal == 1:
            return {'info': 'update', 'url': url['assets'][0]['browser_download_url']}
        return {'info': 'old', 'version': url['tag_name'], 'body': i['body']}


def updateApp():
    url = checkForUpdates("V0.0.0", 1)['url']
    os.system("start " + url)

    # I make an automatic installer when I have nothing else to do, I have already spent about 5 hours testing and I give up... sorry

if __name__ == "__main__":
    import os
    import sys
    print(sys.argv)
    print('Running')
    os.system("pause")
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