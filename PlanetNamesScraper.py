planets_file = open("MyFile.txt", "w")
# class = "category-page__member-link"
from bs4 import BeautifulSoup
from urllib.request import urlopen

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in alphabet:
    url_to_scrape = f"https://memory-alpha.fandom.com/wiki/Category:Planets?from={char}"

    request_page = urlopen(url_to_scrape)

    page_html = request_page.read()

    request_page.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')

    for planet_tag in html_soup.find_all('a', class_='category-page__member-link'):
        planet_tag.get_text()



request_page = urlopen(url_to_scrape)

