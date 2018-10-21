'''
Goal: Find all youtube videos
1) on current page
2) one link away
3) on entire domain
'''

from bs4 import BeautifulSoup
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
    print(id_set)


# def get_ids_on_page():
#
# def get_ids_x_links_away():
#
# def get_ids_on_domain():

if __name__ == '__main__':
    get_ids('https://www.youtube.com/')
