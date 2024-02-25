# Read all lines from planets.txt
from urllib import request
from bs4 import BeautifulSoup

import ssl
import certifi

import csv


planets = []
with open('planets.txt', 'r') as file:
    planets = file.readlines()
    # TODO: replace all spaced and special chars w underscores etc

scraped_results = [["planet_name", "status"]]
with open("scraped_planets.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_results)
scraped_results = []

for (idx, planet) in enumerate(planets):
    # ignore any planet categories
    if "Category:" in planet:
        continue

    # clean the planet string of spaces and newlines
    planet = planet.replace(" ", "_").rstrip('\n')

    url = "https://memory-alpha.fandom.com/wiki/" + planet

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    planet_page = request.urlopen(url, context=ssl_context)
    page_html = planet_page.read()
    planet_page.close()
    html_soup = BeautifulSoup(page_html, 'html.parser')

    # The status always follows this html element:
    # <h3 class="pi-data-label pi-secondary-font">Status:</h3>
    status_label = html_soup.find('h3', class_='pi-data-label pi-secondary-font', string='Status:')

    # Ignore planets without status
    if status_label == None:
        continue

    status_div = status_label.find_next_sibling('div')
    status = status_div.text.strip().split()[0]

    scraped_results.append([planet, status])

    # write results to file every 100 planets
    if idx % 100 == 0:
        with open("scraped_planets.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(scraped_results)

        scraped_results = []

# write remaining planets
with open("scraped_planets.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(scraped_results)