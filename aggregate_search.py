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
__version__ = '0.4.16'
__credits__ = 'Tasos M Adamopoulos (tasos-py) and Mario Vilas'
__dev_environment__ = 'Python 3.8'
__status__ = 'Development Status :: 1 - Alpha'

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path

from aggregate_utils import files, get_user_agent, reporting, config as cfg
from search_engines import engines as se

FileIt = files.results2file
ReportIt = reporting.report_results

# Random user agents for each engine are assigned here;
#  assigned agents are also reported in main().
ddg_UA = get_user_agent.rando_function(cfg.DDG_UAs)
sp_UA = get_user_agent.rando_function(cfg.SP_UAs)
moj_UA = get_user_agent.rando_function(cfg.MOJ_UAs)
mg_UA = get_user_agent.rando_function(cfg.MG_UAs)


def search_this(search_term: str) -> None:
    """
    Run the input search term through engines specified in dict(engine).
    Report to Terminal and to file non-redundant results of urls and
    page titles.

    :param search_term: String with valid syntax on all or most engines.
    """

    # Any duplicated url closest to the end of the combined_results list will
    #   be retained in the unique_results list, so engine order here matters
    #   for engine-specific reporting of unique results counts.
    # Engine keys (tags) here should match those in config.py TAG_NAME.
    engines = {
        '(MG)': se.Metager(mg_UA),
        '(DDG)': se.Duckduckgo(ddg_UA),
        '(SP)': se.Startpage(sp_UA),
        '(Moj)': se.Mojeek(moj_UA),
    }

    combined_results = []
    for tag, _e in engines.items():
        # Limit each engine to ~20 max results.
        # MG returns ~20-60 results/page depending on UA; DDG ~36.
        if tag in '(DDG), (MG)':
            results = _e.search(search_term, pages=1)
            links = results.links()[0:20]
            titles = results.titles()[0:20]
            detail = results.text()[0:20]
        else:
            # Mojeek and Startpage return 10 results/page.
            results = _e.search(search_term, pages=2)
            links = results.links()
            titles = results.titles()
            detail = results.text()

        # Prepend the engine tag to each result title.
        for i, _title in enumerate(titles):
            titles[i] = f'{tag} {_title}'

        # Pack the result into a list of tuples.
        e_result = list(zip(links, titles, detail))
        combined_results.extend(e_result)

        e_count_msg = (f'Keeping the first {len(links)} results'
                       f' from {cfg.TAG_NAME[tag]} {tag}')
        ReportIt(search_term, e_count_msg)

    # Filter unique urls, saving the last redundant hit from combined_results,
    #   where last is determined by the dict(engine) items' order.
    # Note: in combined_results and unique_results, res[0] is the url,
    #   res[1] is the page title, res[2] is the detailed description.
    unique_results = tuple({res[0]: res for res in combined_results}.values())

    result_summary = (f'Kept {len(combined_results)} total results.\n\n'
                      f'There are {len(unique_results)} unique results.')
    ReportIt(search_term, result_summary)

    # Report number of unique results retained from each engine.
    for tag, _ in cfg.TAG_NAME.items():
        num_uniq = len([res for res in unique_results if f'{tag}' in res[1]])
        uniq_msg = f'{num_uniq} unique results retained from {tag}'
        ReportIt(search_term, uniq_msg)

    # Need a brief delay before Terminal scrolls to last line of results
    #   so user can glimpse the last engine's, and final, unique count.
    time.sleep(2)

    # Finally, report url, page title, and page detail from each result.
    for res in unique_results:
        (url, title, detail) = res
        url = f'\n{cfg.BLUE}{url}'
        title = f'\n{cfg.YELLOW}{title}{cfg.NC}'
        detail = f'\n{detail}'
        ReportIt(search_term, url+title+detail)

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
            syntax = Path('aggregate_utils', 'use_syntax.txt').read_text(encoding='utf-8')
            print(syntax)
        except FileNotFoundError:
            print('Sorry, but the use_syntax.txt file is not in the aggregate_utils folder.')
        sys.exit(0)


def main() -> None:
    """
    Print user agents and header information to Terminal and file.
    Run searches if no arguments are given.
    """

    parse_args()

    term = input("\nEnter search term: ").lstrip()
    print()

    # In the unlikely event user seeks assistance at input prompt...
    if term in '-help, --help, -h':
        parse_args(term)

    # Remove spaces in term for better file naming; '+' doesn't affect search.
    term = term.replace(' ', '+')

    user_agents_used = (
        'User agents assigned for this search:\n'
        f'{"MegaGer:".ljust(11)}{cfg.ORANGE}{mg_UA}{cfg.NC}\n'
        f'{"DuckDuckGo:".ljust(11)}{cfg.ORANGE}{ddg_UA}{cfg.NC}\n'
        f'{"Startpage:".ljust(11)}{cfg.ORANGE}{sp_UA}{cfg.NC}\n'
        f'{"Mojeek:".ljust(11)}{cfg.ORANGE}{moj_UA}{cfg.NC}\n'
    )

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
