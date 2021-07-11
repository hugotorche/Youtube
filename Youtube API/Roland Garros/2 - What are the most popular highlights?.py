# What are the most popular highlights of RG editions (2014-2020)?

import os
from googleapiclient.discovery import build

API_KEY = 'AIzaSyDpCCBy5UyJGAColealFVrXn6nScZqoALc'

youtube = build('youtube', 'v3', developerKey=API_KEY)

playlistIds = ['PLUK9NdagG_Cch6IoClOc707jBRBlZCP_B',
               'PLUK9NdagG_Cd6mKWojO3slW-snYsuffCW',
               'PLUK9NdagG_CchB-_onP9Ut38sIKFS8u6A',
               'PLUK9NdagG_CcfRhTtQ0z_LgkDrMApB12I',
               'PLUK9NdagG_CfVEWbQOzfXhoA8Zs7pWJjx',
               'PLUK9NdagG_CdksJ1cSNeZEa_a0gTI7myU',
               'PLUK9NdagG_CckS_BNghv-eEBUlXmkcZp4']

edition = 2013

for playlistId in playlistIds:

    videos = []

    edition = edition + 1

    nextPageToken = None
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlistId,
            maxResults=80,
            pageToken=nextPageToken
        )

        pl_response = pl_request.execute()

        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])

        vid_request = youtube.videos().list(
            part='statistics',
            id=','.join(vid_ids)
        )

        vid_response = vid_request.execute()

        for item in vid_response['items']:
            vid_views = item['statistics']['viewCount']

            vid_id = item['id']
            yt_link = f'https://youtu.be/{vid_id}'

            videos.append(
                {
                    'views': int(vid_views),
                    'url': yt_link
                }
            )

        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break

    videos.sort(key=lambda vid: vid['views'], reverse=True)

    for video in videos[:5]:
        print('{} - {} - {}'.format(edition, video['url'],
                                    video['views']))

    print()
