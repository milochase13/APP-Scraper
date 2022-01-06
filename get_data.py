import requests
from bs4 import BeautifulSoup

def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    data = {}
    speeches = {}
    meta_data = {}
    
