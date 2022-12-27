#!/usr/bin/env python3
"""
Assigns engines a user agent as specified in aggregate_search.py.
Agent functions:
bot_agent: assigns one of three search engine bot agents.
firefox_ver(): assigns a random Firefox browser version.
fake_agent(): static, FAKE_USER_AGENT from config, works with Startpage.
github_agent(): assigns one of original GitHub repo or this fork.
python_agent(): static, default used by the requests module.
random_agent(): a random full system-type agent from list of 4400+.
winfire_agent(): original FAKE_USER_AGENT for Startpage, but with random
    assignment of Firefox version.
"""
import gzip
from pathlib import Path
from random import choice

from . import config as cfg

# Modified from get_random_user_agent() in googlesearch module of google package.
#   Can get current system's (browser's) UA from http://my-user-agent.com/
#   or from https://httpbin.org/headers
DEFAULT_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
AGENT_ARCHIVE: str = 'user_agents.txt.gz'


def bot_agent() -> str:
    """
    Generate a random agent from the three most common bot user agents.
    """
    bot = (
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)'
        )
    return choice(bot)


def firefox_agent() -> str:
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


def fake_agent() -> str:
    """
    The original FAKE_USER_AGENT in config.py:
    'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'
    Works with Startpage when nothing else will.

    :return: static user agent string.
    """

    # NOTE that the Firefox ver can be any from firefox_agent()
    return 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'


def github_agent() -> str:
    """
    A GitHub repository's custom user agent.
    Keep versions up-to-date.

    :return: The Search-Engines-Scraper or search-aggregator Repo.
    """
    github_repo = (
        'aggregate_search/0.4 Repo: https://github.com/csecht/search-aggregator',
        'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'
    )

    return choice(github_repo)


def python_agent() -> str:
    """
    This static UA,'python-requests/2.27.1', is the Python default and
    works with all engines except DDG, where it is 403: Forbidden.

    :return: Default Python requests package header user agent.
    """

    # Obtained from : >>>requests.utils.default_headers()
    return 'python-requests/2.27.1'


def random_agent() -> bytes:
    """
    Get a random user agent byte string from file of over 4400 obtained
    from the googlesearch module of google package by Mario Vilas. See:
    https://python-googlesearch.readthedocs.io/en/latest/

    :return: Random full user agent string.
    """
    # Load the list of ~4400 user agents to select from.
    try:
        rua_file = Path(Path(__file__).parent, f'{AGENT_ARCHIVE}')
        with gzip.open(rua_file, 'rt') as fp:
            user_agents_list = [_.strip() for _ in fp.readlines()]
    except FileNotFoundError:
        print('Could not open the random user agent file; using default agent...\n'
              f'Try downloading {AGENT_ARCHIVE} from {cfg.PROJECT}')
        user_agents_list = [DEFAULT_AGENT]
    # Note that all the browser versions in user_agents.txt are old,
    # so list probably needs an update to work more consistently.
    return choice(user_agents_list)


def winfire_agent() -> str:
    """
    Derivative of fake_agent(), appending random Firefox versions from
    firefox_agent().

    :return: A user agent that works with most engines most times.
    """

    return f'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 {firefox_agent()}'


def rando_function(agents: tuple) -> str:
    """
    Run one at user agent function at random from the group of functions
    provided by *agents*. Each search engine will have a certain group
    of UA functions that work consistently for it.
    Example USAGE:
    engine_agent = get_user_agent.rando_function(('fua', 'pua', 'rua'))

    :param agents: Tuple of handles for agent functions known to work
    for an engine. 'bua': bot_agent(),  'fua': firefox_agent(),
    'pua': python_agent(), 'gua': github_agent(), 'rua': random_agent(),
    'wua': winfire_agent()
    """
    select = choice(agents)

    r_agents = {
        'bua': bot_agent(),
        'gua': github_agent(),
        'fua': firefox_agent(),
        'pua': python_agent(),
        'rua': random_agent(),
        'wua': winfire_agent(),
    }

    return r_agents[select]
