# Read all lines from planets.txt
from urllib.request import urlopen
from bs4 import BeautifulSoup

planets = []
with open('planets.txt', 'r') as file:
    planets = file.readlines()
    # TODO: replace all spaced and special chars w underscores etc

for planet in planets:
    url = "https://memory-alpha.fandom.com/wiki/" + planet
    print(url)

    planet_page = urlopen(url)
    # page_html = planet_page.read()
    # planet_page.close()
    # html_soup = BeautifulSoup(page_html, 'html.parser')

    # # The status always follows this html element:
    # # <h3 class="pi-data-label pi-secondary-font">Status:</h3>
    # status_label = html_soup.find('h3', class_='pi-data-label pi-secondary-font')

    # status_div = status_label.find_next_sibling('div')

    # status = status_div.text.strip()

    # print(status)



