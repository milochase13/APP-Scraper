# APP-Scraper

Scraper for some elections documents on https://www.presidency.ucsb.edu/

Data collected from the following 5 subsections or "modes":
1. Campaign documents
2. Convention speeches
3. Debates
4. Party platforms
5. Transition documents

Documents from all modes were scraped in the same three general json formats:  

1. [mode].jsonlist
  {   
   &emsp;  - 'url' : url of html page data taken from  
   &emsp;  - 'speeches' : each new author/speaker creates a speech   
   &emsp;          - 'speaker' : author/speaker of speech  
   &emsp;          - 'paragraphs' : list of paragraphs in given speech (as String)  
   &emsp;          - 'tokenized_paragraphs' : tokenized paragraphs   
  }   
 
 2. metadata_[mode].jsonlist   
  {   
   &emsp;   - 'url' : url of html page data taken from   
   &emsp;   - 'date' : string representing creation date of data   
   &emsp;   - 'name' : title of document   
  }   
 
 3. raw_data_[mode].jsonlist   
  {  
  &emsp;   - 'url' : url of html page data taken from  
  &emsp;    - 'html' : raw html of data scraped (in String form)  
  }  
  
  
  
  
    
