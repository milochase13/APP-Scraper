import requests
from bs4 import BeautifulSoup
import json

def get_speeches(url, soup):
    body = soup.find(class_="field-docs-content")
    speeches = []
    turns = body.find_all("p")
    for turn in turns:
        speech = {"text" : [], "tokenized" : []}
        speaker = turn.find("b")
        if speaker:
            speech["speaker"] = speaker.text
            speech["text"].append(turn.contents[1].text) 
            speech["tokenized"].append(turn.contents[1].text.split()) 
            speeches.append(speech)
        else:
            speeches[-1]["text"].append(turn.text) 
            speeches[-1]["tokenized"].append(turn.text.split()) 
    del speeches[0:2]
    return speeches

def parse_debate(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # metadata
    name = soup.find(class_="field-ds-doc-title").text
    date = soup.find(class_="field-docs-start-date-time").text
    metadata = {
        "url" : url,
        "name" : name,
        "date" : date
    }
    
    # data
    speeches = get_speeches(url, soup)
    data = {
        "url" : url,
        "speeches" : speeches
    }
    return data, metadata

def build_file(data, file_name):
    with open(file_name, 'a+') as f:
        json.dump(data, f)
        f.write("\n")


#init_file(parse_debate("https://www.presidency.ucsb.edu/documents/presidential-debate-belmont-university-nashville-tennessee-0"), "data.jsonlist")
build_file(parse_debate("https://www.presidency.ucsb.edu/documents/democratic-candidates-debate-charleston-south-carolina-0"), "data.jsonlist")
build_file(parse_debate("https://www.presidency.ucsb.edu/documents/presidential-debate-belmont-university-nashville-tennessee-0"), "data.jsonlist")