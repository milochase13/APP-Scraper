Scraper for some elections documents on https://www.presidency.ucsb.edu/

UPDATE: Now specialized only for general election debates. Data scraped and 
tagged in the following format:

debates.jsonlist.
{
   - 'url' : url of html page data taken from
   - 'speeches' : each new author/speaker creates a speech
   - '{INTEGER}' : unique integer value for each paragraph
     - 'speaker' : author/speaker of speech
     - 'text' : list of paragraphs in given speech (as String)
}

metadata_debates.jsonlist
{
    - 'url' : url of html page data taken from
    - 'date' : string representing creation date of data
    - 'name' : title of document
    - 'incumbant' : name of incumbant if applicable
    - 'democrat' : name of democrat nominee if applicable
    - 'republican' : name of republican nominee if applicable
}

raw_data_debates.jsonlist
{
    - 'url' : url of html page data taken from
     - 'html' : raw html of data scraped (in String form)
}

Notes:

Run source env/bin/activate to activate virtural environment
Run deactivate to deactivate