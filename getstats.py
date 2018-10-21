import requests
import isodate
import os
from dotenv import load_dotenv  # installed with 'pip install python-dotenv'

# Youtube API Parts:
# https://developers.google.com/youtube/v3/docs/videos/list

# Load api key from environment variable
load_dotenv(dotenv_path="./.env")
apikey = os.environ.get('APIKEY')

id = 'Ov_znn3KHfE'  # Unique id for video to look at
payload = {
    'id': id,
    'part': 'contentDetails',
    'key': apikey
}
r = requests.get('https://content.googleapis.com/youtube/v3/videos', params = payload)
print(r.json())

# Get the time
# Duration is ISO8601 format
# https://developers.google.com/youtube/v3/docs/videos
# https://en.wikipedia.org/wiki/ISO_8601#Durations
duration = r.json()['items'][0]['contentDetails']['duration']
pydur = isodate.parse_duration(duration)

# Format duration as pretty string
dur_str = str(pydur)
print(f'Video duration: {dur_str}')
