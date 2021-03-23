import requests
from bs4 import BeautifulSoup

SUBREDDIT = 'UIUC'
URL = 'https://www.reddit.com/r/' + SUBREDDIT + '/top/?t=all'
print(URL)
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.text)

URL = 'https://mobile.twitter.com/LACaldwellDC/status/1347148675588509696'
soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
print(soup.text)