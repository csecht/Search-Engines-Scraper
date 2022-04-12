#!/usr/bin/env python3
"""
aggregate_search.py is a command-line search engine aggregator written
in Python3. It is derived from the Search-Engines-Scraper repository at
https://github.com/tasos-py/Search-Engines-Scraper.

Non-redundant aggregated results from four privacy-focused search
engines. Results are returned as URLs, page titles, and page descriptions
printed to the Terminal/console and to an auto-named text file.

The intent is to provide broad searches and easy comparisons among
search engines, while minimizing or avoiding search silos. User agents
for HTTP requests are randomized for each engine within optimized sets.

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

import argparse
import time
from datetime import datetime
from sys import exit as sys_exit

from aggregate_utils import about, agents, files, reporting, config as cfg
from search_engines import engines as se

FileIt = files.results2file
ReportIt = reporting.report_results


def search_this(search_term: str, multiplier: int) -> None:
    """
    Run the input search term through engines specified in dict(engine).
    Report to Terminal and to file non-redundant results of urls and
    page titles and page text details.

    :param search_term: String with valid syntax for all or most engines.
    :param multiplier: Multiplication factor to increase search results.
    """

    # Any duplicated url closest to the end of the combined_results list
    #   will be retained in the unique_results list, so engines item
    #   order matters for the number of unique results from each engine.
    # For sensible reporting, item order should match among
    #   dict(agents), config.ENGINE_NAMES, and dict(engines)
    engines = {
        '(DDG)': se.Duckduckgo(agents['(DDG)']),
        '(MG)': se.Metager(agents['(MG)']),
        '(SP)': se.Startpage(agents['(SP)']),
        '(Moj)': se.Mojeek(agents['(Moj)']),
    }
    combined_results = []

    # For each engine, balance the number of initial results so that
    #   there are more equal numbers of unique results among engines.
    #   Keep in mind that fewer unique results are retained for engines
    #   earlier in the engines.items loop.
    # Depending on UA, DGG returns ~20-60 results/page, MG ~20-40;
    #   Mojeek and Startpage return 10 results/page.
    for tag, engine in engines.items():
        if tag in '(DDG), (MG)':
            results = engine.search(search_term, pages=(1 * multiplier))
            links = results.links()[0:(30 * multiplier)]
        else:
            results = engine.search(search_term, pages=(2 * multiplier))
            links = results.links()

        titles = results.titles()
        details = results.text()

        # Prepend the engine tag to each result title.
        for i, _title in enumerate(titles):
            titles[i] = f'{tag} {_title}'

        # Pack each engine's result into a list of tuples.
        combined_results.extend(list(zip(links, titles, details)))

        e_count_msg = (f'Kept the first {len(links)} results'
                       f' from {cfg.ENGINE_NAMES[tag]}')
        ReportIt(search_term, e_count_msg)

    # Filter unique urls, saving the last redundant hit from combined_results,
    #   where last is determined by the order of items in {engines}.
    # Note: in combined_results and unique_results, res[0] is the url,
    #   res[1] is the page title, res[2] is the detailed description.
    unique_results = tuple({res[0]: res for res in combined_results}.values())

    result_summary = (f'{len(combined_results)} total results\n\n'
                      f'{len(unique_results)} unique results retained:')
    ReportIt(search_term, result_summary)

    # Report number of unique results retained from each engine.
    for tag, engine in cfg.ENGINE_NAMES.items():
        num_uniq = sum(tag in res[1] for res in unique_results)
        uniq_msg = f'{num_uniq} from {engine} {tag}'
        ReportIt(search_term, uniq_msg)

    # Need a brief delay before Terminal scrolls to last line of results
    #   so user can glimpse the final engine's unique count.
    time.sleep(2)

    # Finally, report url, page title, and page detail from each result.
    for (_u, _t, _d) in unique_results:
        url = f'\n{cfg.BLUE}{_u}'
        title = f'\n{cfg.YELLOW}{_t}{cfg.NC}'
        detail = f'\n{_d}'
        ReportIt(search_term, url+title+detail)

    print(f'\nResults were written or appended to {FileIt(search_term, "")}')
    ending_msg = f'\n{"=" * 26} END of {len(unique_results)} results {"=" * 26}\n'
    ReportIt(search_term, ending_msg)


def manage_args(assist: str = None) -> int:
    """Allow handling of command line arguments.

    :param assist: Used if input search string is -h or --help.
    :return: Page request multiplier parameter for search_this().
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--info', '-i',
                        help='Provides description, version, GNU license.',
                        action='store_true',
                        default=False)
    parser.add_argument('--use', '-u',
                        help='Usage, search term syntax examples.',
                        action='store_true',
                        default=False)
    parser.add_argument('--x',
                        help='Result multiplication factor, N:'
                             ' %(choices)s (default: %(default)d).',
                        default=1,
                        choices=range(2, 6),
                        type=int,
                        metavar="N"
                        )

    args = parser.parse_args()
    # --info and --use will print, then exit.
    if args.info:
        about.info(__doc__)

    elif args.use or str(assist) in '-help, --help':
        about.usage()

    # The multiplier for number of results returned.
    return args.x


def main() -> None:
    """
    Check for arguments; print and exit for informational args.
    Obtain input search term.
    Print user agents and header information to Terminal and file.
    Run searches.
    """

    result_multiplier = manage_args()

    # Remove trailing spaces, replace internal spaces in term for better
    #    file naming; '+' doesn't affect search.
    term = input("\nEnter search term: ").lstrip().replace(' ', '+')
    print()

    # In the unlikely event user seeks assistance at input prompt...
    if term in '-help, --help, -h':
        manage_args(term)

    file_header = (
        f'SEARCH TERM: {term}    TIME: {datetime.now().strftime("%x %X")}')
    FileIt(term, f'{file_header}\n\n')

    reporting.report_agents(term)
    ReportIt(term, f'Search results multiplier: {result_multiplier}X')

    search_this(term, result_multiplier)


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print(' *** Keyboard interrupt: User has quit the program ***\n')
        sys_exit()
