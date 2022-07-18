# Search Aggregator
Aggregates results from several search engines with output to Terminal and text file. This is a fork of Search Engines Scraper by tasos_py, but is run from the `aggregate_search.py` Python script.
## Supported search engines  

- _[Duckduckgo](https://duckduckgo.com)_
- _[Startpage](https://www.startpage.com)_
- _[Mojeek](https://www.mojeek.com)_
- _[MetaGer](https://metager.org)_

## Features
 - Uses search engines that are focused on user privacy.
 - Non-redundant results (URL, page title, page detail) are printed to the Terminal/console with easy-to-read colors and to an automatically named text file.
 - A random user agent is assigned from an appropriate set of options for each engine.

## Requirements
_Python 3_ with
_[Requests](http://docs.python-requests.org/en/master/)_ and
_[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_ 

Developed in Python 3.8-3.9

## Installation
Download the .zip code archive, extract the .zip file, open Terminal/Command Prompt in the search-aggregator-main folder, run the setup file:

`python3 setup.py install`

Done!

## Usage  
From within the search-aggregator-main folder, execute `aggregate_search.py` from Terminal/Command Prompt:
- Linux/MacOS: `python3 aggregate_search.py` or `./aggregate_search.py`
- Windows: `python3 aggregate_search.py` or `python aggregate_search.py` or `py aggregate_search.py`, depending on your system environment. 

then enter your search term at the prompt. Example output:
```
Enter search term: gov forest policy

User agents assigned for this search:
MegaGer:   Firefox/74.0
DuckDuckGo:aggregate_search/0.4 Repo: https://github.com/csecht/search-aggregator
Startpage: Firefox/82.0
Mojeek:    Opera/8.10 (Windows NT 5.1; U; en)

Search results multiplier: 1X
Searching Duckduckgo
Kept the first 28 results from DuckDuckGo
Searching Metager
Kept the first 21 results from MetaGer
Searching Startpage
Kept the first 20 results from Startpage
Searching Mojeek
Kept the first 20 results from Mojeek
89 total results

71 unique results retained:
14 from DuckDuckGo (DDG)
17 from MetaGer (MG)
20 from Startpage (SP)
20 from Mojeek (Moj)

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

Example of color-enhanced Terminal output:
![color_output](images/scrnshot_output.png)

ARGUMENTS: --help, --info, --use, or --x. 

The command `aggregate_search.py --use` provides examples of search term syntax, then exits.

The command `aggregate_search.py --x 2` doubles the number of results returned; `--x 3` triples results, etc., up to `--x 5`. Without an --x argument, ~60 -- 80 total unique results are returned. 

### Single engine search
The original command line client from Search-Engines-Scraper, `search_engines_cli.py` can be used for customized searches. For example, 
```
python3 search_engines_cli.py -q forestry -p 4 -e mojeek
```
will return four pages of url results for the query 'forestry' from the Mojeek engine. If no -e engine is specified, defaults to DuckDuckGo. To see additional search and output options, use the help command,
```
python3 search_engines_cli.py -h
```
## Known issues
As of July 2022, MetaGer searches return no results because scrapper queries
now require a CAPTCHA response, which aggregate_search.py does not provide.