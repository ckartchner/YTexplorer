"""
Youtube API Parts:
https://developers.google.com/youtube/v3/docs/videos/list

TODO:
get_ids_on_domain():
get_ids_x_links_away():
"""

import requests
import isodate
import os
from dotenv import load_dotenv  # installed with 'pip install python-dotenv'
import argparse
import datetime
import re


def sum_time(website):
    id_set = get_ids(website)
    total_time = datetime.timedelta(0)
    for video_id in id_set:
        total_time += stats(video_id)
    return total_time


def get_ids(website):
    """Find all youtube video ids input page"""
    html_page = requests.get(website)
    # TBD when this is ever hit...
    try:
        html_page.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        print("Error: " + str(e))
        return

    # positive lookbehind to find youtube 11 char ids
    regobj = re.compile(r'(?<=watch\?v=)(.){11}')
    matches = regobj.finditer(html_page.text)
    id_set = set([m.group(0) for m in matches])
    return id_set


def stats(videoid):
    # Load api key from environment variable
    load_dotenv(dotenv_path="./.env")
    apikey = os.environ.get('APIKEY')

    payload = {
        'id': videoid,
        'part': 'contentDetails, snippet',
        'key': apikey
    }
    r = requests.get('https://content.googleapis.com/youtube/v3/videos', params=payload)

    # Get the time
    # Duration is ISO8601 format
    # https://developers.google.com/youtube/v3/docs/videos

    duration = r.json()['items'][0]['contentDetails']['duration']
    title = r.json()['items'][0]['snippet']['title']
    pydur = isodate.parse_duration(duration)

    # Format duration as pretty string
    dur_str = str(pydur)
    print(f'Duration: {dur_str} || Title: {title}')
    return pydur


if __name__ == '__main__':
    # Args for debug purposes
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', help='Specify website used to get statistics. Expects full url.')
    parser.add_argument('--stats', help='Get stats for single youtube video id. Expects youtube id.')
    parser.add_argument('--ids', help='Get all youtube ids on a single page. Expects full url.')
    args = parser.parse_args()
    if args.site is not None:
        all_time = sum_time(args.site)
        print(f'All videos time: {all_time}')
    if args.ids is not None:
        ids = get_ids(args.ids)
        print(ids)
    if args.stats is not None:
        stats(args.stats)
