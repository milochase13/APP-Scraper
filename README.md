Scraper for some elections documents on https://www.presidency.ucsb.edu/


# APP-Scraper

Scraper for some elections documents on https://www.presidency.ucsb.edu/

UPDATE: Now specialized only for general election debates. Data scraped and 
tagged in the following format:

Documents from all modes were scraped in the same three general json formats:  

1. debates.jsonlist.  
  {   
   &nbsp;  - 'url' : url of html page data taken from  
   &nbsp;  - 'speeches' : each new author/speaker creates a speech   
   &emsp;&emsp;  - '{INTEGER}' : unique integer value for each paragraph    
   &emsp;&emsp;&emsp;&emsp;          - 'speaker' : author/speaker of speech    
   &emsp;&emsp;&emsp;&emsp;          - 'text' : list of paragraphs in given speech (as String)  
  }   
 
 2. metadata_debates.jsonlist   
  {   
   &nbsp;   - 'url' : url of html page data taken from   
   &nbsp;   - 'date' : string representing creation date of data   
   &nbsp;   - 'name' : title of document   
   &nbsp;   - 'incumbant' : name of incumbant if applicable  
   &nbsp;   - 'democrat' : name of democrat nominee if applicable   
   &nbsp;   - 'republican' : name of republican nominee if applicable   
  }   
 
 3. raw_data_debates.jsonlist   
  {  
  &nbsp;   - 'url' : url of html page data taken from  
  &nbsp;    - 'html' : raw html of data scraped (in String form)  
  }  

Notes:
1. Run `source env/bin/activate` to activate virtural environment
2. Run `deactivate` to deactivate
  
