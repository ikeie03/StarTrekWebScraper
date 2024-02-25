# class = "category-page__member-link"
from bs4 import BeautifulSoup
from urllib.request import urlopen

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

planets_file = open("planets.txt", "a")

try:
    # the wiki has one page per letter, so we go through each one at a time
    for char in alphabet:
        url_to_scrape = f"https://memory-alpha.fandom.com/wiki/Category:Planets?from={char}"

        request_page = urlopen(url_to_scrape)

        page_html = request_page.read()

        request_page.close()

        html_soup = BeautifulSoup(page_html, 'html.parser')

        for planet_tag in html_soup.find_all('a', class_='category-page__member-link'):
            # get the planet name and write to file
            planet_name = planet_tag.get_text()
            planets_file.write(planet_name + '\n')

except Exception as e:
    print(e)

planets_file.close()