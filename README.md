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
Enter search term: gov income tax

User agents assigned for this search:
MegaGer:   Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
DuckDuckGo:Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
Startpage: Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/91.0
Mojeek:    Firefox/89.0

Searching Metager
Keeping the first 20 results from MetaGer (MG)
Searching Duckduckgo
Keeping the first 20 results from DuckDuckGo (DDG)
Searching Startpage
Keeping the first 20 results from Startpage (SP)
Searching Mojeek
Keeping the first 20 results from Mojeek (Moj)
Kept 80 total results.

There are 54 unique results.
6 unique results retained from (MG)
10 unique results retained from (DDG)
18 unique results retained from (SP)
20 unique results retained from (Moj)

https://www.incometax.gov.in/iec/foportal
(SP) Income Tax Department: Home
Please use e-mail ID “ITR.helpdesk@incometax.gov.in” for queries related to Income tax return (ITR 1 to ITR 7 for AY 21-22). Refer News & update for the ...

https://eportal.incometax.gov.in/iec/foservices/
(MG) e-Filing Home Page, Income Tax Department, Government of India


https://www.usa.gov/taxes
(SP) Taxes | USAGov
Find answers to top questions about filing federal income tax, paying, getting refunds, and more.

https://www.usa.gov/check-tax-status
(DDG) Where&#x27;s My Refund? Check the Status of My Tax Return - USA.gov
Check Your Federal Tax Refund Status. If you have filed your federal income taxes and expect to receive a refund, you can track its status. Have your Social Security number, filing status, and the exact whole dollar amount of your refund ready.

http://www.taxes.ca.gov/Income_Tax/
(Moj) Income Tax
CA.gov ... City/County Business Tax (CCBT) Program - Identifies individuals and businesses with certain filing requirements.
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
Page details are not being reported for MetaGer search results.