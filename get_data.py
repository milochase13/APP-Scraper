import requests
from bs4 import BeautifulSoup
import json
import gzip

def get_speeches(url, soup, mode):
    pres = soup.find(class_="field-title")
    if pres:
        pres = pres.text.replace("\n", '')
    else:
        pres = url.split("/")[-1]
    body = soup.find(class_="field-docs-content")
    speeches = []
    turns = body.find_all("p")
    speaker = "unknown"

    for turn in turns:
        speech = {"text" : [], "tokenized" : []}
        if mode == "debates":
            spkr = turn.text.split(':')[0]
            if turn.find("b"):
                speaker = turn.find("b").text
            elif turn.find("strong"):
                speaker = turn.find("strong").text
            elif spkr.isupper():
                speaker = spkr
        else:
            speaker = pres

        if speaker:
            if mode == "debates":
                speech["speaker"] = speaker
                paragraph = ""
                try:
                    paragraph = turn.contents[1].text
                except:
                    paragraph = turn.text
                speech["text"].append(paragraph) 
                speech["tokenized"].append(paragraph.split()) 
            else:
                speech["speaker"] = speaker
                speech["text"].append(turn.text) 
                speech["tokenized"].append(turn.text.split()) 
            speeches.append(speech)
        else:
            speeches[-1]["text"].append(turn.text) 
            speeches[-1]["tokenized"].append(turn.text.split()) 
        speaker = ""

    return speeches

def parse_debate(url, mode):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

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
        "date" : date
    }
    
    # data
    speeches = get_speeches(url, soup, mode)
    data = {
        "url" : url,
        "speeches" : speeches
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
