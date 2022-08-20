import requests
from bs4 import BeautifulSoup
import time
import json

def get_rally(rally,stem):
    data = {}
    url = stem + rally 
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    body = soup.find(class_="fl-callout-text")
    paragraphs = []
    chunks = body.find_all("p")
    for chunk in chunks:
        who = chunk.text.split(' ')
        speaker = who[0] + who[1]
        if speaker == 'DonaldTrump:':
            paragraphs.append(''.join(chunk.find("br").next_siblings))

    data["url"] = url
    data["speaker"] = "Donald Trump"
    data["speeches"] = paragraphs
    return data
        
def build_file(data, file_name):
    with open(file_name, 'a+') as f:
        json.dump(data, f)
        f.write("\n")

def main(stem, rally):
    build_file(get_rally(rally, stem), "trump_rally_4-19-16.json")
    


if __name__ == "__main__":
    stem = "https://www.rev.com/blog/transcripts/"
    rally = "donald-trump-michigan-speech-transcript-asks-black-voters-what-do-you-have-to-lose" #donald-trump-las-vegas-nevada-rally-transcript
    main(stem, rally)