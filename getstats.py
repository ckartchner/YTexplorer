import requests
import isodate
import os
from dotenv import load_dotenv  # installed with 'pip install python-dotenv'
import argparse
from bs4 import BeautifulSoup
import datetime
import requests
import re
# import

def get_ids(website):
    '''Find all youtube video ids input page'''
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
    tot_time = datetime.timedelta(0)
    for videoid in id_set:
        tot_time += stats(videoid)
    print(id_set)
    print(tot_time)

# Youtube API Parts:
# https://developers.google.com/youtube/v3/docs/videos/list

# Load api key from environment variable
def stats(videoid):
    load_dotenv(dotenv_path="./.env")
    apikey = os.environ.get('APIKEY')

    #id = 'Ov_znn3KHfE'  # Unique id for video to look at
    payload = {
        'id': videoid,
        'part': 'contentDetails',
        'key': apikey
    }
    r = requests.get('https://content.googleapis.com/youtube/v3/videos', params = payload)
    # print(r.json())

    # Get the time
    # Duration is ISO8601 format
    # https://developers.google.com/youtube/v3/docs/videos

    duration = r.json()['items'][0]['contentDetails']['duration']
    pydur = isodate.parse_duration(duration)

    # Format duration as pretty string
    dur_str = str(pydur)
    print(f'Video duration: {dur_str}')
    return pydur

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', help='input the url website')
    args = parser.parse_args()

    get_ids(args.site)
