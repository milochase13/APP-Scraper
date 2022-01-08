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
     - 'speeches' : each new author/speaker creates a speech   
             - 'speaker' : author/speaker of speech  
             - 'paragraphs' : list of paragraphs in given speech (as String)  
             - 'tokenized_paragraphs' : tokenized paragraphs   
  }   
 
 2. metadata_[mode].jsonlist   
  {   
      - 'url' : url of html page data taken from   
      - 'date' : string representing creation date of data   
      - 'name' : title of document   
  }   
 
 3. raw_data_[mode].jsonlist   
  {  
      - 'url' : url of html page data taken from  
      - 'html' : raw html of data scraped (in String form)  
  }  
  
  
  
  
    
