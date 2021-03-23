import requests
import urllib.request
from bs4 import BeautifulSoup
import json

def get_wikipedia_article(year, month, dest_dir="Wikipedia-Deaths/", file_name = None):
    # https://scipython.com/blog/scraping-a-wikipedia-table-with-beautiful-soup/
    year_str = str(year)
    #https://en.wikipedia.org/wiki/Deaths_in_January_1997
    URL = "https://en.wikipedia.org/wiki/Deaths_in_" + month + "_" + year_str 
    print(URL)
    req = urllib.request.urlopen(URL)
    article = req.read().decode()
    #f = open('myfile.dat', 'w+')
    if file_name == None:
        file_name = year_str + '_' + month + '.html'
    with open (dest_dir + file_name, 'w') as fo:
        fo.write(article)

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def extract_wikipedia_articles(directory, start_year, final_year, skip_years = []):
    for year in range(start_year, final_year + 1):
        if year not in skip_years:
            for month in MONTHS:
                get_wikipedia_article(year, month, directory)

def scrape_article(year, month, directory = 'Wikipedia-Deaths/Wikipedia_Articles/'):
    str_year = str(year)
    full_file_name = directory + str_year + '_' + month + '.html'
    article = open(full_file_name, "r")
    soup = BeautifulSoup(article, 'html.parser')
    #tables = soup.find_all('table', class_='sortable')
    body = soup.find_all('body')[0]

    data_level = soup.find("div", class_ = "mw-parser-output")

    uls = data_level.find_all("ul")

    everything = data_level.find_all()
    h = data_level.find_all('h3')
    json_dict = {}
    day = None
    for f in everything:
        if f.name == 'h2':
            next_ = f.next
            if (next_.attrs['id'] == 'References'):
                break
        if f.name == 'h3':
            raw_day = f.text
            day = raw_day[:raw_day.index('[')]
            continue
        if day == None or f.name != 'ul':
            continue
        second_level = f.find_all('li')
        people = [] 
        if day == '31':
            dA = 0
        for ff in second_level:
            third_level = ff.find('a')
            if third_level != None:
                third_level_text = third_level.text
                people.append(third_level_text)
        json_dict[day] = people

    return json_dict

def write_json(json_obj, file_name):
    with open(file_name, "w") as write_file:
        json.dump(json_obj, write_file, indent=4)


def scrape_articles(directory = 'Wikipedia-Deaths/Wikipedia_Articles', start_year = 1997, final_year = 2019, skip_years = [], file_name = "Wikipedia-Deaths/Data/deaths.json"):
    year_dicts = {}
    #final_year = 1999 #@todo delete
    for year in range(start_year, final_year + 1):
        if year not in skip_years:
            print(year)
            month_dicts = []
            for month in MONTHS:
                print(month)
                days_dict = scrape_article(year, month, directory)
                month_dicts.append({month:days_dict})
            year_dicts[year] = month_dicts
    write_json(year_dicts, file_name)

def get_data(extract_articles = False, start_year = 1997, final_year = 2020, skip_years = []):
    
    scrape_articles('Wikipedia-Deaths/Wikipedia_Articles/', start_year = start_year)
    

    

if __name__ == "__main__":
    #extract_wikipedia_articles('Wikipedia-Deaths/Wikipedia_Articles/', 1997, 2020)

    get_data(True, 1997)