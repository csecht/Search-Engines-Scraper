# Search Aggregator
Aggregates results from several search engines with an easily read text output. This is a fork of Search Engines Scraper by tasos_py. It is run from the `aggregate_search.py` Python script.
## Supported search engines  

- _[Duckduckgo](https://duckduckgo.com)_
- _[Startpage](https://www.startpage.com)_
- _[Mojeek](https://www.mojeek.com)_
- _[MetaGer](https://metager.org)_

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
Download the .zip code archive, extract the .zip file, open Terminal/Command Prompt in the Search-Engines-Scraper-master folder, run the setup file:

`python3 setup.py install`

Done!

## Usage  
From within the Search-Engines-Scraper-master folder, execute `aggregate_search.py` from Terminal/Command Prompt:
- Linux/MacOS: `python3 aggregate_search.py` or `./aggregate_search.py`
- Windows: `python3 aggregate_search.py` or `python aggregate_search.py` or `py aggregate_search.py`, depending on your system environment. 

then enter your search term at the prompt. Example output:
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
...and the remaining results. All results would be printed to Terminal and written to a file automatically titled: Results_gov+forest+policies.txt

Arguments: --help, --about, or --use. The command `aggregate_search.py --use` provides examples of search term syntax.

### Single engine search
The original command line client from Search-Engines_Scraper, `search_engines_cli.py` can be used for customized searches. For example, 
```
python3 search_engines_cli.py -q forestry -p 4 -e mojeek
```
will return four pages of url results for the query 'forestry' from the Mojeek engine. To see additional search and output options, use the help command,
```
python3 search_engines_cli.py -h
```