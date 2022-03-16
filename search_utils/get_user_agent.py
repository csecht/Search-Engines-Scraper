#!/usr/bin/env python3
"""
Assigns engines a user agent as specified in multi_search.
Agent functions:
firefix_ver(): assigns a random Firefox browser version.
forked_agent(): this distribution's static agent.
python_agent(): the default Python used by the requests module.
random_agent(): a random full system-type agent from list of 4400+.
tasos_agent(): default agent of original Search-Engines-Scraper distribution.
"""
from pathlib import Path
from random import choice

import gzip


# NOTE: Using system's full user agent at the UA tends to give results
#   filtered to location and .com. Get system UA from http://my-user-agent.com/
# So use recent Firefox ver for all search engines to work.

# Search-Engines-Scraper uses its github url as the default ua;
#   works for all but Google. firefox_ver also works.


# ############ Modified from get_random_user_agent() in googlesearch
#    module of google package.
DEFAULT_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

# Load the list of valid user agents from the module's folder.
# The search order is:
#   * user_agents.txt.gz
#   * user_agents.txt
#   * default user agent.
try:
    try:
        user_agents_file = Path(Path(__file__).parent, 'user_agents.txt.gz') #
        with gzip.open(user_agents_file, 'rb') as fp:
            user_agents_list = [_.strip() for _ in fp.readlines()]

    except FileNotFoundError as err:
        print('user_agents.txt.gz could not be opened; trying user_agents.txt', err)
        user_agents_file = Path(Path(__file__).parent, 'user_agents.txt')
        with open(user_agents_file, encoding='utf-8') as fp:
            user_agents_list = [_.strip() for _ in fp.readlines()]
except FileNotFoundError:
    print('Could not open user_agents file for a random agent, so using default agent:')
    user_agents_list = [DEFAULT_AGENT]


def random_agent() -> bytes:
    """
    Get a random user agent byte string from file of over 4400 obtained
    from the googlesearch module of google package by Mario Vilas. See:
    https://python-googlesearch.readthedocs.io/en/latest/

    :return: Random full user agent string.
    """
    return choice(user_agents_list)

# ^^^^^^^^^^^^^^ Modified from from googlesearch module of google package.


def python_agent() -> str:
    """
    This static UA,'python-requests/2.27.1', is the Python default and
    works with all engines except DDG, where it is 403: Forbidden.

    :return: Default Python requests package header user agent.
    """
    # >>>import requests
    # >>>requests.utils.default_headers()
    # {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
    return 'python-requests/2.27.1'


def firefox_ver() -> str:
    """Generate a random Firefox version.
    Seems to work for all engines.
    """
    # Note: the 68 series are for mobile Firefox app.
    firefox_vers = (
        '53.0', '54.0', '55.0', '56.0', '57.0', '58.0', '59.0', '68.1', '68.2',
        '68.3', '68.4', '68.5', '68.6', '68.7', '68.8', '68.9', '68.10',
        '68.11', '70.0', '71.0', '72.0', '73.0', '74.0', '75.0', '76.0', '77.0',
        '78.0', '79.0', '80.0', '81.0', '82.0', '83.0', '84.0', '85.0', '86.0',
        '87.0', '88.0', '89.0', '90.0', '91.0', '92.0', '93.0', '94.0', '95.0',
        '96.0', '97.0'
    )
    return f'Firefox/{choice(firefox_vers)}'


def tasos_agent() -> str:
    """
    The original Search-Engine-Scraper default user agent:
    'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'
    Works with all engines except Google, which works with firefox_ver().

    :return: Original GitHub module and repository link as user agent.
    """
    return 'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'


def forked_agent() -> str:
    """
    The forked Search-Engine-Scraper default user agent:
    'search_engines/0.2 Repo: https://github.com/csecht/Search-Engines-Scraper'

    :return: csecht's GitHub module and repository link as user agent.
    """
    return 'search_engines/0.2 Repo: https://github.com/csecht/Search-Engines-Scraper'
