import requests
from bs4 import BeautifulSoup
import json

def get_links(gen_url, subsection, items = 5000):
    url = gen_url + subsection + "?items_per_page=" + str(items)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find(class_="view-content")
    sections = content.find_all("div", class_="views-row")
    links = []
    for section in sections:
        link = section.find("a")
        links.append(link['href'])
    return links
