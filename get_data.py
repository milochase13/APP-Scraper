import requests
from bs4 import BeautifulSoup
import json

def get_speeches(url, soup, mode):
    pres = soup.find(class_="field-title").text.replace("\n", '')
    body = soup.find(class_="field-docs-content")
    speeches = []
    turns = body.find_all("p")
    for turn in turns:
        speech = {"text" : [], "tokenized" : []}
        speaker = ""
        if mode == "debates":
            if turn.find("b"):
                speaker = turn.find("b")
            elif turn.find("br"):
                speaker = turn.find("br")
        else:
            speaker = pres
        if speaker:
            if mode == "debates":
                speech["speaker"] = speaker.text
                paragraph = ""
                try:
                    paragraph = turn.contents[1].text
                except:
                    paragraph = turn.text
                speech["text"].append(paragraph) 
                speech["tokenized"].append(paragraph.split()) 
            else:
                speech["speaker"] = speaker
                unitalize = ''.join([e.strip() for e in turn if not e.name and e.strip()]) # remove italisized text
                speech["text"].append(unitalize) 
                speech["tokenized"].append(unitalize.split()) 
            speeches.append(speech)
        else:
            speeches[-1]["text"].append(turn.text) 
            speeches[-1]["tokenized"].append(turn.text.split()) 
    if mode == "debates":
        del speeches[0:2]
    return speeches

def get_docs(url, soup):
    body = soup.find(class_="field-docs-content")
    speaker = soup.find(class_="field-title").text.replace("\n", '')
    speeches = []
    turns = body.find_all("p")
    for turn in turns:
        speech = {"text" : [], "tokenized" : []}
        speech["speaker"] = speaker
        unitalize = ''.join([e.strip() for e in turn if not e.name and e.strip()]) # remove italisized text
        speech["text"].append(unitalize) 
        speech["tokenized"].append(unitalize.split()) 
        speeches.append(speech)
    if mode == "debate":
        del speeches[0:2]
    return speeches

def parse_debate(url, mode):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # metadata
    name = soup.find(class_="field-ds-doc-title").text.replace("\n", '')
    date = soup.find(class_="date-display-single").text.replace("\n", '')
    metadata = {
        "url" : url,
        "name" : name,
        "date" : date
    }
    
    # data
    speeches = get_speeches(url, soup, mode)
    data = {
        "url" : url,
        "speeches" : speeches
    }
    return data, metadata

def build_file(data, file_name):
    with open(file_name, 'a+') as f:
        json.dump(data, f)
        f.write("\n")

#build_file(parse_debate("https://www.presidency.ucsb.edu/documents/remarks-the-white-house-correspondents-association-dinner-12")[0], "test.jsonlist")