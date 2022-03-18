# Search Engines Scraper CSE
A fork of Search Engines Scraper by tasos_py. Intended to be run from 
the `multi_search` script.
## Supported search engines  

_[Brave](https://brave.com)_
_[Duckduckgo](https://duckduckgo.com)_
_[Startpage](https://www.startpage.com)_
_[Mojeek](https://www.mojeek.com)_
_[MetaGer](https://metager.org)_

## Features  

 - Uses search engines that are focused on user privacy.
 - Creates output text file of non-redundant results (URL, page title).
 - Uses random user agent when possible.

## Requirements  

_Python 3_ with
_[Requests](http://docs.python-requests.org/en/master/)_ and
_[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_ 

Developed in Python 3.8-3.9

## Installation  

Download the .zip code archive, extract the .zip file, run the setup file from within the unzipped Search-Engines-Scraper-master folder:

`$ python3 setup.py install`

Done!

## Usage  
Execute `multi_search` Python script from Terminal, enter search term at the prompt.
Example output:
```
Enter search term: gov forest policies

User agents used in this search
Brave: Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0
DuckDuckGo: search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper
MetaGer: b'Opera/9.60 (Windows NT 6.0; U; uk) Presto/2.1.1'
Mojeek: search_engines/0.5 Repo: https://github.com/csecht/Search-Engines-Scraper
Startpage: Firefox/89.0

Searching Duckduckgo
29 hits from DuckDuckGo (DDG)
Searching Brave
20 hits from Brave (B)
Searching Mojeek
20 hits from Mojeek (M)
Searching Startpage
20 hits from Startpage (SP)
Searching metager.org
19 hits from MetaGer (MG)
Found 108 hits.

There are 102 unique hits.
26 unique hits from (DDG)
18 unique hits from (B)
19 unique hits from (M)
20 unique hits from (SP)
19 unique hits from (MG)

https://www.fs.usda.gov/about-agency/regulations-policies
(SP) Regulations & Policies | US Forest Service

https://fire.ca.gov
(MG) CAL FIRE - Home ->hosted by Scopia
```
...and the remaining results. All results would be printed to Terminal and written to a file automatically titled: Results_gov+forest+policies.txt

Arguments: --help, --about, or --use. The command `multi_search --use` provides examples of search term syntax.
