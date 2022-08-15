# # from urllib import response
# # import requests
# # import json
# # from Tokens import tokenManager

# # token = tokenManager.request('token')['Data']

# # animeName = "bunny girl senpai"
# # animeId = 35507
# # req = f'https://api.myanimelist.net/v2/anime?q={animeName}&limit=10'
# # # req = f'https://api.myanimelist.net/v2/anime/{animeId}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,studios,statistics'

# # response = requests.get(req, headers={'Authorization': 'Bearer ' + token})

# # with open('anime3.json', 'w') as f:
# #     json.dump(response.json(), f, indent=4)

# import globalVars
# globalVars.init()
# import sqlite3

# title, titleJp, animeID, image, notes, startDate, endDate, synopsis, episodes, globalScore, localScore, pictures, viewed, status, genres, background, studio, relatedAnime, relatedManga, averageEpDuration = "", "", 0, "", "", "", "", "", 0, 0, 0, [], False, "", "", "", "", "", "", ""

# conn = sqlite3.connect(globalVars.path + 'LocalStorage.db')
# c = conn.cursor()
# c.execute(f'''INSERT INTO anime (title, titleJp, animeID, image, notes, startDate, endDate, synopsis, episodes, globalScore, localScore, pictures, viewed, status, genres, background, studio, relatedAnime, relatedManga, averageEpDuration) VALUES ('Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV)', 'ようこそ実力至上主義の教室へ', '35507', 'https://api-cdn.myanimelist.net/images/anime/5/86830l.jpg', '', '2017-07-12', '2017-09-27', 'On the surface, Koudo Ikusei Senior High School is a utopia. The students enjoy an unparalleled amount of freedom, and it is ranked highly in Japan. However, the reality is less than ideal. Four classes, A through D, are ranked in order of merit, and only the top classes receive favorable treatment.\n\nKiyotaka Ayanokouji is a student of Class D, where the school dumps its worst. There he meets the unsociable Suzune Horikita, who believes she was placed in Class D by mistake and desires to climb all the way to Class A, and the seemingly amicable class idol Kikyou Kushida, whose aim is to make as many friends as possible.\n\nWhile class membership is permanent, class rankings are not; students in lower ranked classes can rise in rankings if they score better than those in the top ones. Additionally, in Class D, there are no bars on what methods can be used to get ahead. In this cutthroat school, can they prevail against the odds and reach the top?\n\n[Written by MAL Rewrite]', '12', '7.86', '0.0', '['https://api-cdn.myanimelist.net/images/anime/7/86829l.jpg', 'https://api-cdn.myanimelist.net/images/anime/5/86830l.jpg', 'https://api-cdn.myanimelist.net/images/anime/8/87022l.jpg']', 'False', 'finished_airing', 'Drama, Psychological, School', '', 'Lerche', "[{'node': {'id': 30813, 'title': 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/13/74160.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/13/74160l.jpg'}}, 'relation_type': 'other', 'relation_type_formatted': 'Other'}, {'node': {'id': 51096, 'title': 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV) 2nd Season', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/1010/124180.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/1010/124180l.jpg'}}, 'relation_type': 'sequel', 'relation_type_formatted': 'Sequel'}]", '[]', '1440')''')
# conn.commit()
# conn.close()

# a = "[{'node': {'id': 30813, 'title': 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/13/74160.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/13/74160l.jpg'}}, 'relation_type': 'other', 'relation_type_formatted': 'Other'}, {'node': {'id': 51096, 'title': 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e (TV) 2nd Season', 'main_picture': {'medium': 'https://api-cdn.myanimelist.net/images/anime/1010/124180.jpg', 'large': 'https://api-cdn.myanimelist.net/images/anime/1010/124180l.jpg'}}, 'relation_type': 'sequel', 'relation_type_formatted': 'Sequel'}]"



# a = [999]
# print(a[-1]) # 999


# import requests
# import json
# from Tokens import tokenManager

# token = ':)'

# animeName = "bunny girl senpai"
# animeId = 35507
# req = f'https://api.myanimelist.net/v2/anime?q={animeName}&limit=10'
# req = f'https://api.myanimelist.net/v2/anime/{animeId}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,studios,statistics'

# response = requests.get(req, headers={'X-MAL-CLIENT-ID': token})

# with open('anime3.json', 'w') as f:
#     json.dump(response.json(), f, indent=4)

# import requests
# import json
# token = ":)"

# req = f'https://api.myanimelist.net/v2/anime/ranking?ranking_type=all&limit=4'
# response = requests.get(req, headers={'X-MAL-CLIENT-ID': token})
# print(response.status_code)
# with open('anime3.json', 'w') as f:
#     json.dump(response.json(), f, indent=4)
 

# import os

# path = os.getenv('APPDATA') + '\\AnimeList\\data\\tokens.db'
# print(os.path.exists(path))

import requests
import json
response = requests.get("https://api.github.com/repos/redystum/Anime_List_App/releases")
with open('git.json', 'w') as f:
    json.dump(response.json(), f, indent=4)