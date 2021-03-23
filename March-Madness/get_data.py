import requests
import urllib.request
from bs4 import BeautifulSoup

def get_wikipedia_article(year, file_name = None, dest_dir = 'March-Madness/Wikipedia_Articles/'):
    # https://scipython.com/blog/scraping-a-wikipedia-table-with-beautiful-soup/
    year_str = str(year)
    URL = "https://en.wikipedia.org/wiki/" + year_str + "_NCAA_Division_I_Men's_Basketball_Tournament"
    req = urllib.request.urlopen(URL)
    article = req.read().decode()
    #f = open('myfile.dat', 'w+')
    if file_name == None:
        file_name = year_str + '.html'
    with open (dest_dir + file_name, 'w') as fo:
        fo.write(article)

    """
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='model-body')
    scorecard = soup.find(id='scorecards')
    """

def extract_wikipedia_articles(start_year = 1985, final_year = 2019, skip_years = []):
    for year in range(start_year, final_year + 1):
        if year not in skip_years:
            get_wikipedia_article(year)

def scrape_article(year, directory = 'March-Madness/Wikipedia_Articles/'):
    str_year = str(year)
    full_file_name = directory + str_year + '.html'
    article = open(full_file_name, "r")
    soup = BeautifulSoup(article, 'html.parser')
    tables = soup.find_all('table', class_='sortable')
    headings = None
    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        dA = 0
       # if (head)

def scrape_articles(directory = 'March-Madness/Wikipedia_Articles/', start_year = 1985, final_year = 2019, skip_years = []):
    for year in range(start_year, final_year + 1):
        if year not in skip_years:
            scrape_article(year, directory)

    article = open()

def get_data(extract_articles = False, start_year = 1985, final_year = 2019, skip_years = []):
    if (extract_articles):
        extract_wikipedia_articles()
    
    scrape_articles('March-Madness/Wikipedia_Articles/', start_year = start_year)
    

    

if __name__ == "__main__":
    get_data(False, 2000)