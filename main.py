import requests
from bs4 import BeautifulSoup

general_URL = "https://www.presidency.ucsb.edu/documents/app-categories/elections-and-transitions/"
URL = "https://www.presidency.ucsb.edu/documents/app-categories/elections-and-transitions/debates"
URL_test = "https://www.presidency.ucsb.edu/documents/presidential-debate-belmont-university-nashville-tennessee-0"
page = requests.get(URL_test)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="field-docs-content")
paragraphs = results.find_all("p")

for p in range(10):
    print(paragraphs[p].text)
    print("******************")