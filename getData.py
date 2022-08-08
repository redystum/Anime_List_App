import requests
import json

from Tokens import tokenManager

def searchAnime(animeName):
    token = tokenManager.getClient()

    req = f'https://api.myanimelist.net/v2/anime?q={animeName}&limit=15'
    response = requests.get(req, headers={'X-MAL-CLIENT-ID': token})
    return response.json()['data']

def getAnimeData(animeId):
    token = tokenManager.getClient()

    req = f'https://api.myanimelist.net/v2/anime/{animeId}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,studios'
    response = requests.get(req, headers={'X-MAL-CLIENT-ID': token})

    return response.json()

def checkToken(clientId):
    token = clientId
    req = f'https://api.myanimelist.net/v2/anime?q=evangelionlimit=1'
    response = requests.get(req, headers={'X-MAL-CLIENT-ID': token})
    if response.status_code == 200:
        return {"status": "success"}

    return {"status": "error", "error": "Invalid token"}