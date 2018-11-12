# Youtube Timer
### Goals:  
- Find and display the video lengths for all videos on a page along with a summary.  
- Create a website that does this rather than just run as a Python script from the CLI.

### Getting started:
To get this code running on your machine, you need to generate a youtube API key.  
 OAuth not required. Just a key.  
https://developers.google.com/youtube/registering_an_application

After you have a key, place it in a file called '.env' in the same directory as the other files.

Also, `pip install -r requirements.txt`

Lots of details about the youtube api:
https://developers.google.com/youtube/v3/getting-started

### Features wanted:
Generate audio files for all videos on page
Ability to run behind login

### Status:

11 November 2018  
Started website. Have working summary statistics

20 Oct 2018  
getstats.py - pulls out the time of a youtube video from a video id  
idhunter.py - finds all the video ids on a given page  
