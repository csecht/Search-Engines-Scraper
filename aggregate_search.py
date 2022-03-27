#!/usr/bin/env python3
"""
aggregate_search.py is a command-line web search aggregator in Python,
derived from the Search-Engines-Scraper repository at
https://github.com/tasos-py/Search-Engines-Scraper.

Non-redundant aggregated results from privacy-oriented search engines
are returned as URLs and their page titles to the Terminal and to
an auto-named text file. User agents for requests are randomized.

The intent is to provide easy comparisons among search engines, avoid
unintended search filtering, and automatically store results to file.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see https://www.gnu.org/licenses/.

See LICENCE file for additional licenses of repository components.
"""
__author__ = 'Craig Echt'
__copyright__ = 'Copyright (C) 2022 C.S. Echt'
__license__ = 'GNU General Public License'
__program_name__ = 'aggregate_search.py'
__project_url__ = 'https://github.com/csecht/Search-Engines-Scraper'
__version__ = '0.4.7'
__credits__ = 'Tasos M Adamopoulos (tasos-py) and Mario Vilas'
__dev_environment__ = 'Python 3.8'
__status__ = 'Development Status :: 1 - Alpha'

import argparse
import sys
import time
from datetime import datetime
from os import system
from pathlib import Path

import search_engines as se
from aggregate_search_utils import files, get_user_agent, reporting, vcheck

# Quit if Python interpreter version is earlier than required.
vcheck.minversion('3.6')

FileIt = files.results2file
RandoUA = get_user_agent.rando_function
ReportIt = reporting.report_results

# Assign a random user agent to each engine here.
# Bots are generally banned by SP; tua may be blocked by Moj.
dgg_UA = RandoUA(('bua', 'fua', 'tua', 'eua'))
sp_UA = RandoUA(('fua', 'wua'))
moj_UA = RandoUA(('bua', 'fua', 'eua', 'rua', 'rua'))
mg_UA = RandoUA(('bua', 'fua', 'pua', 'tua', 'eua', 'rua'))

# The duplicated result closest to end of the results list is the one
#   retained in the unique_results list, so engine order here matters
#   for engine-specific reporting of unique results metrics.
# Use only engines committed to privacy.
engines = {
    'DDG': se.Duckduckgo(dgg_UA),
    'Moj': se.Mojeek(moj_UA),
    'SP': se.Startpage(sp_UA),
    'MG': se.Metager(mg_UA),
}

engine_names = {
    'DDG': 'DuckDuckGo',
    'Moj': 'Mojeek',
    'SP': 'Startpage',
    'MG': 'MetaGer'
}

# Terminal output ANSI color options.
blue = '\x1b[1;38;5;33m'
orange = '\x1b[1;38;5;166m'
yellow = '\x1b[1;38;5;3m'
undo_color = '\x1b[0m'  # No color, reset to system default.

# Needed for Windows Command Prompt ANSI text formatting.
if sys.platform[:3] == 'win':
    system("color")


def search_this(search_term: str) -> None:
    """
    Run the input search term through engines specified in dict(engines).
    Print and write non-redundant results of urls and page titles.

    :param search_term: String with valid syntax on all or most engines.
    """

    combined_results = []
    for e_key, _engine in engines.items():
        # Limit each engine to ~20 max results.
        # MG returns 20-52 results/page depending on UA; DDG ~36.
        if e_key in 'DDG, MG':
            results = _engine.search(search_term, pages=1)
            links = results.links()[0:20]
            titles = results.titles()[0:20]
        else:
            # Mojeek and Startpage return 10 results/page.
            results = _engine.search(search_term, pages=2)
            links = results.links()
            titles = results.titles()

        # Prepend the engine tag, in parentheses, to each result title.
        for i, _title in enumerate(titles):
            titles[i] = f'({e_key}) {_title}'

        # Pack the link and its title into a list of tuples.
        e_result = list(zip(links, titles))
        combined_results.extend(e_result)

        e_count_msg = f'Keeping the first {len(links)} results from {engine_names[e_key]} ({e_key})'
        ReportIt(search_term, e_count_msg)

    # Filter unique urls, saving the last redundant hit from combined_results,
    #   where last is determined by the engines (dict) items' order.
    unique_results = list({tup[:1]: tup for tup in combined_results}.values())

    result_summary = (f'Kept {len(combined_results)} total results.\n\n'
                      f'There are {len(unique_results)} unique results.')
    ReportIt(search_term, result_summary)

    # Report number of unique hits retained from each engine.
    for tag in engine_names:
        tag = f'({tag})'
        num_uniq_hit = len([hit for hit in unique_results if tag in hit[1]])
        tag_msg = f'{num_uniq_hit} unique results retained from {tag}'
        ReportIt(search_term, tag_msg)

    # Need a brief delay before Terminal scrolls to last line of results
    #   so user can glimpse the last engine's, and final, unique count.
    time.sleep(2)

    # Finally, report url and page title from each tuple in results list.
    for tup in unique_results:
        result = f'\n{blue}{tup[0]}\n{yellow}{tup[1]}{undo_color}'
        ReportIt(search_term, result)

    print(f'\nResults were written or appended to {FileIt(search_term, "")}')
    ending_msg = f'\n{"=" * 26} END of {len(unique_results)} results {"=" * 26}\n'
    ReportIt(search_term, ending_msg)


def parse_args(assist: str = None) -> None:
    """Allow handling of common command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--about',
                        help='Provides description, version, GNU license.',
                        action='store_true',
                        default=False)
    parser.add_argument('--use',
                        help='Program execution and search term examples.',
                        action='store_true',
                        default=False)

    args = parser.parse_args()
    if args.about:
        print(__doc__)
        print(f'{"Author:".ljust(13)}', __author__)
        print(f'{"License:".ljust(13)}', __license__)
        print(f'{"Copyright:".ljust(13)}', __copyright__)
        print(f'{"Program:".ljust(13)}', __program_name__)
        print(f'{"url:".ljust(13)}', __project_url__)
        print(f'{"Version:".ljust(13)}', __version__)
        print(f'{"Credits:".ljust(13)}', __credits__)
        print(f'{"Dev Env:".ljust(13)}', __dev_environment__)
        print(f'{"Status:".ljust(13)}', __status__)
        print()
        sys.exit(0)

    if args.use or str(assist) in '-help, --help':
        print(f'USAGE: Run {__file__} without arguments,'
              ' then enter your search term at the prompt.\n')
        try:
            syntax = Path('aggregate_search_utils', 'use_syntax.txt').read_text(encoding='utf-8')
            print(syntax)
        except FileNotFoundError:
            print('Sorry, but the use_syntax.txt file is not in the aggregate_search_utils folder.')
        sys.exit(0)


def main() -> None:
    """
    Print parameters and header information to Terminal and file.
    Run the search if no arguments are given.
    """
    parse_args()
    term = input("\nEnter search term: ").lstrip()
    print()

    # In unlikely event the user seeks syntax assistance at input prompt...
    if term in '-help, --help':
        parse_args(term)

    # Remove spaces in term for better file naming; '+' doesn't affect search.
    term = term.replace(' ', '+')

    user_agents_used = (
        'User agent currently assigned to each search engine:\n'
        f'{"DuckDuckGo:".ljust(11)}{orange}{dgg_UA}{undo_color}\n'
        f'{"Mojeek:".ljust(11)}{orange}{moj_UA}{undo_color}\n'
        f'{"Startpage:".ljust(11)}{orange}{sp_UA}{undo_color}\n'
        f'{"MetaGer:".ljust(11)}{orange}{mg_UA}{undo_color}\n')

    file_header = (
        f'SEARCH TERM: {term}    TIME: {datetime.now().strftime("%x %X")}')
    FileIt(term, f'{file_header}\n\n')
    ReportIt(term, user_agents_used)

    search_this(term)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        # Note: Ctrl-c may not work with PyCharm Terminal interpreter when
        #   waiting for Terminal input; Ctrl-d does work.
        print(' *** Keyboard interrupt: User has quit the program ***\n')
        sys.exit()
