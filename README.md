# Search Engines Scraper CSE
A fork of Search Engines Scraper by tasos_py. Intended to be run from 
the `multi_search` script.
## Supported search engines  

_[Duckduckgo](https://duckduckgo.com)_  
_[Startpage](https://www.startpage.com)_  
_[Mojeek](https://www.mojeek.com)_  
_[MetaGer](https://metager.org)_  

## Features  

 - Creates output text file of non-redundant hits (url, page title).
 - Uses random user agent when possible.
 - Python3.  

## Requirements  

_Python 3_ with  
_[Requests](http://docs.python-requests.org/en/master/)_ and  
_[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_ 

Developed in Python 3.8-3.9

## Installation  

Run the setup file from within the unzipped Search-Engines-Scraper-master folder:

`$ python3 setup.py install`

Done!  

## Usage  
Execute `multi_search` Python script from Terminal, enter search term at the prompt.
Example output:
```
Enter search term: gov forest policies

User agents used in this search
DuckDuckGo: search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper
Mojeek: search_engines/0.5 Repo: https://github.com/csecht/Search-Engines-Scraper
Startpage: Firefox/89.0
MetaGer: b'Opera/9.60 (Windows NT 6.0; U; uk) Presto/2.1.1'

Searching Duckduckgo
29 hits from DuckDuckGo (DDG)
Searching Mojeek
20 hits from Mojeek (M)
Searching Startpage
20 hits from Startpage (SP)
Searching MetaGer
19 hits from MetaGer (MG)
Found 88 hits.

There are 84 unique hits.
26 unique hits from (DDG)
19 unique hits from (M)
20 unique hits from (SP)
19 unique hits from (MG)

https://www.fs.usda.gov/about-agency/regulations-policies
(SP) Regulations & Policies | US Forest Service

https://fire.ca.gov
(MG) CAL FIRE - Home ->hosted by Scopia
```
...and the remaining results. All results would be printed to Terminal and writen to a file automatically titled: Results_gov+forest+policies.txt

Arguments: --help, --about, or --use.  `multi_search --use` provides example search term syntax.

User agents can be changed in the *_ua variables of the `multi_search` script.
