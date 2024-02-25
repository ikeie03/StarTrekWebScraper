# Read all lines from planets.txt
from urllib import request
from bs4 import BeautifulSoup

import ssl
import certifi

import csv

urls = ["https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(23rd_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(22nd_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(24th_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(25th_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(26th_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(29th_century)",
        "https://memory-alpha.fandom.com/wiki/Starfleet_personnel_(32nd_century)"]

def scrape_personnel_file(url):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    try:
        person_page = request.urlopen(url, context=ssl_context)
    except:
        return
    page_html = person_page.read()
    person_page.close()
    html_soup = BeautifulSoup(page_html, 'html.parser')


    # getting the rank
    rank_label = html_soup.find('h3', class_='pi-data-label pi-secondary-font', string='Rank:')
    if not rank_label:
        return
    rank_div = rank_label.find_next_sibling('div')

    rank = ""
    try:
        rank = rank_div.findChildren("a", recursive=False)[0].text.strip()
    except Exception as e:
        print(e)
        return

    # getting the name
    name_span = html_soup.find('span', class_='mw-page-title-main')
    if not name_span:
        return
    name = name_span.text.strip()

    # writing to file
    scraped_results = [name, rank]
    print(scraped_results)
    with open("scraped_ranks.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(scraped_results)

for url in urls:
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    planet_page = request.urlopen(url, context=ssl_context)
    page_html = planet_page.read()
    planet_page.close()
    html_soup = BeautifulSoup(page_html, 'html.parser')

    for personnel_list_item in html_soup.find_all('li'):
        # searching a specific individual
        personnel_link = personnel_list_item.findChildren("a", recursive=False)
        if personnel_link:
            personnel_link = personnel_link[0]
        else:
            continue

        personnel_url = personnel_link.get('href')
        print(personnel_url)

        scrape_personnel_file(personnel_url)