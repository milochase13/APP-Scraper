import requests
from bs4 import BeautifulSoup
import json
import gzip
import get_data

def build_debate(url, mode):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    incumbant, dem, rep = get_data.get_candidates(soup)

    # metadata
    name = soup.find(class_="field-ds-doc-title")
    if name:
        name = name.text.replace("\n", '')
    else:
        name = url.split("/")[-1]

    date = soup.find(class_="date-display-single").text.replace("\n", '')
    metadata = {
        "url" : url,
        "name" : name,
        "date" : date,
        "incumbant" : incumbant,
        "democrat" : dem,
        "republican" : rep
    }
    
    # data
    debate = get_data.get_text(soup)
    debate = get_data.annotate_speakers(soup, debate)
    data = {
        "url" : url,
        "speeches" : debate
    }

    # raw data
    raw_data = {
        "url" : url,
        "html" : str(soup)
    }

    return data, metadata, raw_data

def build_file(data, file_name):
    with open(file_name, 'a+') as f:
        json.dump(data, f)
        f.write("\n")

def zip_file(filename):
    f_in = open(filename)
    f_out = gzip.open(filename + '.gz', 'wt')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()