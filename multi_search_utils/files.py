#!/usr/bin/env python3
"""
File controller for multi_search.py. Writes and appends search results to
a file path and names the text file based on the search string.
"""

from pathlib import Path


def results2file(search_txt: str, data: str) -> Path:
    """
    Write a text file of search results.

    :param search_txt: The search string to use in the file name.
    :param data: The URL or info strings to save to file.
    :return: Name of file created/appended.
    """

    resultpath = Path('ResultsFiles/')
    resultpath.mkdir(parents=True, exist_ok=True)

    filename = f'Results_{search_txt}.txt'
    filepath = resultpath / filename
    with open(filepath, 'a', encoding='utf-8') as hits:
        hits.write(data)

    return filepath


def remove_file(search_txt: str) -> None:

    Path(results2file(search_txt, '')).unlink()
