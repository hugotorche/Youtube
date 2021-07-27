# Which RG edition (2014-2020) has most highlights?

import os
import re
import pandas as pd
from datetime import timedelta

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

    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')

    total_seconds = 0

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
            part='contentDetails',
            id=','.join(vid_ids)
        )

        vid_response = vid_request.execute()

        for item in vid_response['items']:
            duration = item['contentDetails']['duration']

            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(
                hours=hours,
                minutes=minutes,
                seconds=seconds
            ).total_seconds()

            total_seconds += video_seconds

        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break

    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)

    edition = edition + 1

    print(f'{edition} - {hours}:{minutes}:{seconds}')
