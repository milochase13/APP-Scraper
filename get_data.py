import requests
from bs4 import BeautifulSoup
import json
import math

def get_candidates(soup):
    f = open('./presidential_candidates_years.txt')
    candidates = json.load(f)
    f.close()
    date = soup.find(class_="date-display-single").text
    year = date[-2:]
    try:
        incumbant = candidates[year]['incumbant']
        dem = candidates[year]['d']
        rep = candidates[year]['r']
    except:
        incumbant = "NA NA"
        dem = "NA NA"
        rep = "NA NA"
    return incumbant, dem, rep

def get_text(soup):
    debate = {}
    body = soup.find(class_="field-docs-content")
    turns = body.find_all("p")
    for i in range(len(turns)):
        debate[i] = { "text" : turns[i].text }
    return debate

def annotate_speakers(soup, debate):
    president, democrat, republican = get_candidates(soup)
    democrat_split = democrat.split()
    republican_split = republican.split()
    speaker = "unknown"
    body = soup.find(class_="field-docs-content")
    turns = body.find_all("p")
    title = ""
    for i in range(len(turns)):
        partied = False
        remove_prompt = ""
        turn = turns[i]
        tokenized = turn.text.split()
        if len(tokenized) > 1:
            title = (tokenized[0] + tokenized[1]).lower()
        if turn.find("i") and ('republican' in turn.find("i").text.lower() or \
            'democrat' in turn.find("i").text.lower()):
            partied = True
            if 'republican' in turn.find("i").text.lower():
                speaker = republican
            else:
                speaker = democrat
            remove_prompt = turn.find("i").text
        elif turn.find("b"):
            speaker = turn.find("b").text
            remove_prompt = turn.find("b").text
        elif turn.find("strong"):
            speaker = turn.find("strong").text
            remove_prompt = turn.find("strong").text
        elif turn.find("i") and "laughter" not in turn.find("i").text.lower() \
            and "applause" not in turn.find("i").text.lower() and \
                len(turn.find("i").text.split())<8:
            speaker = turn.find("i").text
            remove_prompt = turn.find("i").text
        elif turn.find("em") and "laughter" not in turn.find("em").text.lower() \
            and "applause" not in turn.find("em").text.lower():
            speaker = turn.find("em").text
            remove_prompt = turn.find("em").text
        elif tokenized[0].isupper() and len(tokenized[0]) > 1 and "applause" not\
             in tokenized[0].lower():
            new_speaker = ""
            j = 0
            while len(tokenized) > j and tokenized[j].isupper() and tokenized[j]\
                != 'I' and tokenized[j] != 'I,' and tokenized[j] != 'A':
                if tokenized[j][-1] == ':':
                    break
                new_speaker = new_speaker + tokenized[j] + " "
                j += 1
            if new_speaker[-1] == ':':
                speaker = new_speaker
                remove_prompt = speaker
        elif len(tokenized) > 1 and ('.' in tokenized[0] or 'president' in \
            title or 'governor' in title or 'senator' in title) and '.' in \
                tokenized[1]:
            speaker = tokenized[0] + " " + tokenized[1]
            remove_prompt = speaker

        if 'president' in speaker.lower() and not partied:
            speaker = president
        elif democrat_split[0].lower() in speaker.lower() or \
            democrat_split[1].lower() in speaker.lower():
            speaker = democrat
        elif republican_split[0].lower() in speaker.lower() or \
            republican_split[1].lower() in speaker.lower():
            speaker = republican
        debate[i]["speaker"] = speaker
        debate[i]["text"] = debate[i]["text"].replace(remove_prompt, "", 1)
    return debate

# page = requests.get("https://www.presidency.ucsb.edu/documents/presidential-debate-washington-university-st-louis-missouri")
# soup = BeautifulSoup(page.content, "html.parser")
# debate = get_text(soup)
# debate = annotate_speakers(soup, debate)
# print(debate)