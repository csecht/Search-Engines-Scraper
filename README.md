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
Enter search term: gov forest policy

User agents assigned for this search:
MegaGer:   Firefox/90.0
DuckDuckGo:Firefox/91.0
Startpage: Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/90.0
Mojeek:    b'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.7'

Searching Metager
Keeping the first 20 results from MetaGer (MG)
Searching Duckduckgo
Keeping the first 20 results from DuckDuckGo (DDG)
Searching Startpage
Keeping the first 19 results from Startpage (SP)
Searching Mojeek
Keeping the first 20 results from Mojeek (Moj)
Kept 79 total results.

There are 68 unique results.
12 unique results retained from (MG)
18 unique results retained from (DDG)
18 unique results retained from (SP)
20 unique results retained from (Moj)

https://www.fs.usda.gov/about-agency/regulations-policies
(SP) Regulations & Policies | US Forest Service
Federal agencies operate under the U.S. Code and the Code of Federal Regulations. These laws help form our directives and policies on how we manage national ...

https://www.fs.usda.gov/science-technology/forest-products-modernization/policy-updates
(MG) Policy Updates | US Forest Service - USDA
Timber sales production in the Chattahoochee National Forest, GA. (Forest Service photo by Cecilio Ricardo). The USDA Forest Service recently issued…

https://portal.ct.gov/DEEP/Forestry/Forest-Policy-and-Planning
(Moj) CT Forest Policy and Planning
Some of the features on CT.gov will not function properly with out javascript enabled. ... Get the latest updates on COVID-19 at ct.gov/coronavirus .

https://kingcounty.gov/services/environment/water-and-land/forestry/forest-policy.aspx
(DDG) Forest policy and planning - King County
The Forestry Program is guided by the King County Comprehensive Plan, which establishes policies on the management of rural land and the uses that are suitable to the rural area. The Comprehensive Plan directs that strategies be developed to maintain forest cover and support the practice of sustainable forestry.
```
...and all remaining results. All results are printed to Terminal and written to a file automatically titled: Results_gov+forest+policies.txt

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
## Known issues
Waiting for comments...